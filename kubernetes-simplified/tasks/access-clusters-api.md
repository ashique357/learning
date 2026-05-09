# Access Clusters Using the Kubernetes API

Think of the Kubernetes API like the **city hall's administrative system** - it's the official way to interact with all city services, submit requests, check status, and manage resources. You can access it through different methods, just like visiting city hall in person, calling, or using their website.

## Understanding the Kubernetes API

### API Structure
The Kubernetes API is like a **well-organized government office** with different departments:

```bash
# API structure: /api/v1 or /apis/GROUP/VERSION
/api/v1                           # Core API (pods, services, etc.)
/apis/apps/v1                     # Apps API (deployments, etc.)
/apis/networking.k8s.io/v1        # Networking API (ingress, etc.)
/apis/batch/v1                    # Batch API (jobs, cronjobs)

# Discover available APIs
kubectl api-versions
kubectl api-resources
```

### API Objects and Resources
Like different **types of city services and permits**:

```bash
# List all available resources
kubectl api-resources

# Get specific resource information
kubectl explain pod
kubectl explain deployment.spec
kubectl explain service.spec.ports
```

## Authentication Methods

### Using kubectl (Recommended)
Like having an **official city ID card**:

```bash
# kubectl automatically handles authentication
kubectl get pods
kubectl create deployment nginx --image=nginx
kubectl apply -f deployment.yaml

# Check current authentication
kubectl auth whoami
kubectl config current-context
kubectl config view --minify
```

### Service Account Tokens
Like having **department-specific access badges**:

```yaml
# Create service account
apiVersion: v1
kind: ServiceAccount
metadata:
  name: api-access-sa
  namespace: default

---
# Create role for API access
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list", "watch"]

---
# Bind role to service account
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: pod-reader-binding
subjects:
- kind: ServiceAccount
  name: api-access-sa
  namespace: default
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

```bash
# Get service account token
kubectl create token api-access-sa

# Use token for API access
TOKEN=$(kubectl create token api-access-sa)
curl -H "Authorization: Bearer $TOKEN" \
     -H "Accept: application/json" \
     https://kubernetes.default.svc/api/v1/namespaces/default/pods
```

### Client Certificates
Like having **official government credentials**:

```bash
# Create private key
openssl genrsa -out user.key 2048

# Create certificate signing request
openssl req -new -key user.key -out user.csr -subj "/CN=myuser/O=mygroup"

# Create CertificateSigningRequest in Kubernetes
cat <<EOF | kubectl apply -f -
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: myuser-csr
spec:
  request: $(cat user.csr | base64 | tr -d '\n')
  signerName: kubernetes.io/kube-apiserver-client
  usages:
  - client auth
EOF

# Approve the certificate
kubectl certificate approve myuser-csr

# Get the certificate
kubectl get csr myuser-csr -o jsonpath='{.status.certificate}' | base64 -d > user.crt

# Use certificate for authentication
curl --cert user.crt --key user.key --cacert ca.crt \
     https://kubernetes-api-server/api/v1/pods
```

## Direct API Access

### Using curl
Like **calling city hall directly**:

```bash
# Get API server URL
APISERVER=$(kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}')

# Get token
TOKEN=$(kubectl get secret $(kubectl get serviceaccount default -o jsonpath='{.secrets[0].name}') -o jsonpath='{.data.token}' | base64 -d)

# Make API calls
curl -H "Authorization: Bearer $TOKEN" \
     -H "Accept: application/json" \
     --insecure \
     $APISERVER/api/v1/namespaces/default/pods

# Create a pod via API
curl -X POST \
     -H "Authorization: Bearer $TOKEN" \
     -H "Content-Type: application/json" \
     --insecure \
     -d @pod.json \
     $APISERVER/api/v1/namespaces/default/pods
```

### Using kubectl proxy
Like having a **secure tunnel** to city hall:

```bash
# Start proxy (runs on localhost:8001 by default)
kubectl proxy &

# Now you can access API without authentication
curl http://localhost:8001/api/v1/namespaces/default/pods
curl http://localhost:8001/api/v1/nodes
curl http://localhost:8001/apis/apps/v1/deployments

# Custom port and address
kubectl proxy --port=8080 --address=0.0.0.0 --accept-hosts='.*'
```

### Using kubectl port-forward to API server
```bash
# Forward API server port (if accessible)
kubectl port-forward -n kube-system service/kubernetes 6443:443

# Access via forwarded port
curl -k https://localhost:6443/api/v1/namespaces/default/pods
```

## Programming Language Clients

### Python Client
Like building a **custom application** to interact with city services:

```python
# Install: pip install kubernetes
from kubernetes import client, config

# Load kubeconfig
config.load_kube_config()

# Create API client
v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()

# List pods
pods = v1.list_namespaced_pod(namespace="default")
for pod in pods.items:
    print(f"Pod: {pod.metadata.name}, Status: {pod.status.phase}")

# Create a pod
pod_manifest = {
    "apiVersion": "v1",
    "kind": "Pod",
    "metadata": {"name": "test-pod"},
    "spec": {
        "containers": [{
            "name": "test-container",
            "image": "nginx:latest",
            "ports": [{"containerPort": 80}]
        }]
    }
}

v1.create_namespaced_pod(namespace="default", body=pod_manifest)

# Watch for pod changes
from kubernetes import watch
w = watch.Watch()
for event in w.stream(v1.list_namespaced_pod, namespace="default"):
    print(f"Event: {event['type']}, Pod: {event['object'].metadata.name}")
```

### Go Client
```go
// go mod init k8s-client
// go get k8s.io/client-go@latest

package main

import (
    "context"
    "fmt"
    "path/filepath"
    
    metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
    "k8s.io/client-go/kubernetes"
    "k8s.io/client-go/tools/clientcmd"
    "k8s.io/client-go/util/homedir"
)

func main() {
    // Load kubeconfig
    kubeconfig := filepath.Join(homedir.HomeDir(), ".kube", "config")
    config, err := clientcmd.BuildConfigFromFlags("", kubeconfig)
    if err != nil {
        panic(err)
    }

    // Create client
    clientset, err := kubernetes.NewForConfig(config)
    if err != nil {
        panic(err)
    }

    // List pods
    pods, err := clientset.CoreV1().Pods("default").List(context.TODO(), metav1.ListOptions{})
    if err != nil {
        panic(err)
    }

    for _, pod := range pods.Items {
        fmt.Printf("Pod: %s, Status: %s\n", pod.Name, pod.Status.Phase)
    }
}
```

### JavaScript/Node.js Client
```javascript
// npm install @kubernetes/client-node

const k8s = require('@kubernetes/client-node');

// Load kubeconfig
const kc = new k8s.KubeConfig();
kc.loadFromDefault();

// Create API clients
const k8sApi = kc.makeApiClient(k8s.CoreV1Api);
const appsApi = kc.makeApiClient(k8s.AppsV1Api);

// List pods
async function listPods() {
    try {
        const res = await k8sApi.listNamespacedPod('default');
        res.body.items.forEach(pod => {
            console.log(`Pod: ${pod.metadata.name}, Status: ${pod.status.phase}`);
        });
    } catch (err) {
        console.error(err);
    }
}

// Create deployment
async function createDeployment() {
    const deployment = {
        apiVersion: 'apps/v1',
        kind: 'Deployment',
        metadata: { name: 'nginx-deployment' },
        spec: {
            replicas: 3,
            selector: { matchLabels: { app: 'nginx' } },
            template: {
                metadata: { labels: { app: 'nginx' } },
                spec: {
                    containers: [{
                        name: 'nginx',
                        image: 'nginx:1.21',
                        ports: [{ containerPort: 80 }]
                    }]
                }
            }
        }
    };

    try {
        await appsApi.createNamespacedDeployment('default', deployment);
        console.log('Deployment created successfully');
    } catch (err) {
        console.error(err);
    }
}

listPods();
```

## API Discovery and Exploration

### Exploring API Resources
Like **browsing city hall directories**:

```bash
# List all API groups and versions
kubectl api-versions

# List all resources
kubectl api-resources

# Get detailed resource information
kubectl explain pods
kubectl explain pods.spec
kubectl explain pods.spec.containers

# Get OpenAPI schema
kubectl get --raw /openapi/v2 | jq '.definitions.io.k8s.api.core.v1.Pod'
```

### Using API Discovery
```bash
# Discover API endpoints
curl http://localhost:8001/api
curl http://localhost:8001/apis

# Get specific API group info
curl http://localhost:8001/apis/apps
curl http://localhost:8001/apis/apps/v1

# List resources in API group
curl http://localhost:8001/apis/apps/v1 | jq '.resources'
```

## Advanced API Operations

### Server-Side Apply
Like submitting **official forms** that get processed by city hall:

```bash
# Server-side apply with kubectl
kubectl apply --server-side -f deployment.yaml

# Via API
curl -X PATCH \
     -H "Authorization: Bearer $TOKEN" \
     -H "Content-Type: application/apply-patch+yaml" \
     --data-binary @deployment.yaml \
     "$APISERVER/apis/apps/v1/namespaces/default/deployments/my-app?fieldManager=my-tool&force=true"
```

### Strategic Merge Patch
```bash
# Patch deployment replicas
kubectl patch deployment nginx-deployment -p '{"spec":{"replicas":5}}'

# Via API
curl -X PATCH \
     -H "Authorization: Bearer $TOKEN" \
     -H "Content-Type: application/strategic-merge-patch+json" \
     -d '{"spec":{"replicas":5}}' \
     "$APISERVER/apis/apps/v1/namespaces/default/deployments/nginx-deployment"
```

### JSON Patch
```bash
# JSON patch operations
curl -X PATCH \
     -H "Authorization: Bearer $TOKEN" \
     -H "Content-Type: application/json-patch+json" \
     -d '[{"op": "replace", "path": "/spec/replicas", "value": 3}]' \
     "$APISERVER/apis/apps/v1/namespaces/default/deployments/nginx-deployment"
```

## Watching Resources

### Using kubectl
```bash
# Watch for changes
kubectl get pods --watch
kubectl get events --watch

# Watch with output format
kubectl get pods --watch -o json
```

### Using API Directly
```bash
# Watch pods via API
curl -H "Authorization: Bearer $TOKEN" \
     "$APISERVER/api/v1/namespaces/default/pods?watch=true"

# Watch with resource version
curl -H "Authorization: Bearer $TOKEN" \
     "$APISERVER/api/v1/namespaces/default/pods?watch=true&resourceVersion=12345"
```

### Python Watch Example
```python
from kubernetes import client, config, watch

config.load_kube_config()
v1 = client.CoreV1Api()

w = watch.Watch()
for event in w.stream(v1.list_namespaced_pod, namespace="default"):
    print(f"Event: {event['type']}")
    print(f"Pod: {event['object'].metadata.name}")
    print(f"Status: {event['object'].status.phase}")
    print("---")
```

## Custom Resources and APIs

### Accessing Custom Resources
Like interacting with **specialized city departments**:

```bash
# List custom resource definitions
kubectl get crd

# Access custom resources
kubectl get mycustomresource
kubectl get mycustomresource -o yaml

# Via API
curl -H "Authorization: Bearer $TOKEN" \
     "$APISERVER/apis/mygroup.com/v1/namespaces/default/mycustomresources"
```

### Creating Custom Resource
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: websites.stable.example.com
spec:
  group: stable.example.com
  versions:
  - name: v1
    served: true
    storage: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            properties:
              gitRepo:
                type: string
              replicas:
                type: integer
  scope: Namespaced
  names:
    plural: websites
    singular: website
    kind: Website
```

## Security and RBAC

### Role-Based Access Control
Like setting **department permissions** in city hall:

```yaml
# Create role for API access
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: api-reader
rules:
- apiGroups: [""]
  resources: ["pods", "services"]
  verbs: ["get", "list", "watch"]
- apiGroups: ["apps"]
  resources: ["deployments"]
  verbs: ["get", "list", "watch", "create", "update", "patch"]

---
# Bind to user or service account
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: api-reader-binding
subjects:
- kind: User
  name: api-user
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: api-reader
  apiGroup: rbac.authorization.k8s.io
```

### Testing Permissions
```bash
# Check what you can do
kubectl auth can-i get pods
kubectl auth can-i create deployments
kubectl auth can-i '*' '*'

# Check for specific user
kubectl auth can-i get pods --as=system:serviceaccount:default:api-access-sa

# List all permissions
kubectl auth can-i --list
```

## Troubleshooting API Access

### Common Issues and Solutions

#### Authentication Failures
```bash
# Check current context and credentials
kubectl config current-context
kubectl config view --minify

# Verify token validity
kubectl auth whoami

# Test basic connectivity
kubectl cluster-info
```

#### Permission Denied
```bash
# Check RBAC permissions
kubectl auth can-i get pods
kubectl describe rolebinding
kubectl describe clusterrolebinding

# Check service account permissions
kubectl get serviceaccount
kubectl describe serviceaccount default
```

#### API Server Connectivity
```bash
# Check API server status
kubectl get componentstatuses

# Test direct connectivity
curl -k https://api-server-url/healthz

# Check proxy connectivity
kubectl proxy --port=8001 &
curl http://localhost:8001/healthz
```

## Best Practices

### 1. Authentication
```bash
# Use service accounts for applications
# Rotate tokens regularly
# Use least privilege principle
```

### 2. Error Handling
```python
# Always handle API errors gracefully
try:
    pods = v1.list_namespaced_pod(namespace="default")
except client.ApiException as e:
    print(f"Exception when calling API: {e}")
```

### 3. Rate Limiting
```python
# Implement backoff for rate limiting
import time
from kubernetes.client.rest import ApiException

def api_call_with_backoff(api_func, *args, **kwargs):
    for attempt in range(3):
        try:
            return api_func(*args, **kwargs)
        except ApiException as e:
            if e.status == 429:  # Too Many Requests
                time.sleep(2 ** attempt)
                continue
            raise
```

### 4. Resource Watching
```python
# Use resource versions for efficient watching
# Handle watch timeouts and reconnections
# Filter events to reduce processing
```

## Next Steps

After mastering Kubernetes API access:
1. **Build Custom Controllers**: Implement operators and controllers
2. **Learn Admission Controllers**: Validate and mutate resources
3. **Explore API Machinery**: Understand internals and extensions
4. **Practice Client Development**: Build tools and integrations
5. **Study Custom Resources**: Extend Kubernetes functionality

Remember: The Kubernetes API is like the central nervous system of your cluster - understanding how to interact with it properly enables you to build powerful automation, monitoring, and management tools!