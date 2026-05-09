# Extend Kubernetes

Think of extending Kubernetes like **adding new departments and services** to your city government. Just as a city can create specialized departments (like a tourism board or innovation lab), Kubernetes allows you to add custom functionality through various extension mechanisms.

## Understanding Kubernetes Extensibility

### Extension Points
Like different **ways to expand city services**:

1. **Custom Resources** - New types of city permits/licenses
2. **Controllers/Operators** - Automated city management systems
3. **Admission Controllers** - Quality control for city applications
4. **API Aggregation** - Adding specialized government offices
5. **Scheduler Extensions** - Custom resource allocation systems
6. **Network Plugins** - Custom communication infrastructure

```bash
# Check current extensions
kubectl get crd                    # Custom Resource Definitions
kubectl get apiservices           # API extensions
kubectl get mutatingwebhookconfigurations
kubectl get validatingwebhookconfigurations
```

## Custom Resource Definitions (CRDs)

### Basic CRD
Like creating a **new type of city permit**:

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
                description: "Git repository URL"
              replicas:
                type: integer
                minimum: 1
                maximum: 10
                default: 1
              domain:
                type: string
                pattern: '^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$'
          status:
            type: object
            properties:
              availableReplicas:
                type: integer
              conditions:
                type: array
                items:
                  type: object
                  properties:
                    type:
                      type: string
                    status:
                      type: string
                    reason:
                      type: string
                    message:
                      type: string
  scope: Namespaced
  names:
    plural: websites
    singular: website
    kind: Website
    shortNames:
    - ws
```

### Advanced CRD Features
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: databases.data.example.com
spec:
  group: data.example.com
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
              engine:
                type: string
                enum: ["postgresql", "mysql", "mongodb"]
              version:
                type: string
              storage:
                type: object
                properties:
                  size:
                    type: string
                    pattern: '^[0-9]+[KMGT]i$'
                  class:
                    type: string
              backup:
                type: object
                properties:
                  enabled:
                    type: boolean
                  schedule:
                    type: string
                  retention:
                    type: string
    # Additional printer columns for kubectl output
    additionalPrinterColumns:
    - name: Engine
      type: string
      jsonPath: .spec.engine
    - name: Version
      type: string
      jsonPath: .spec.version
    - name: Storage
      type: string
      jsonPath: .spec.storage.size
    - name: Age
      type: date
      jsonPath: .metadata.creationTimestamp
    # Subresources
    subresources:
      status: {}
      scale:
        specReplicasPath: .spec.replicas
        statusReplicasPath: .status.replicas
  scope: Namespaced
  names:
    plural: databases
    singular: database
    kind: Database
    shortNames:
    - db
```

### Using Custom Resources
```yaml
# Create a custom resource instance
apiVersion: stable.example.com/v1
kind: Website
metadata:
  name: my-blog
  namespace: default
spec:
  gitRepo: "https://github.com/user/blog.git"
  replicas: 3
  domain: "blog.example.com"
```

```bash
# Work with custom resources
kubectl apply -f website.yaml
kubectl get websites
kubectl get ws                    # Using short name
kubectl describe website my-blog
kubectl delete website my-blog
```

## Controllers and Operators

### Simple Controller
Like creating an **automated city service manager**:

```python
# Simple Python controller using kopf framework
import kopf
import kubernetes
from kubernetes import client, config

# Load Kubernetes config
config.load_incluster_config()  # When running in cluster
# config.load_kube_config()     # When running locally

v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()

@kopf.on.create('stable.example.com', 'v1', 'websites')
def create_website(spec, name, namespace, **kwargs):
    """Handle website creation"""
    
    # Create deployment for the website
    deployment = client.V1Deployment(
        metadata=client.V1ObjectMeta(
            name=f"{name}-deployment",
            namespace=namespace,
            labels={"app": name, "managed-by": "website-operator"}
        ),
        spec=client.V1DeploymentSpec(
            replicas=spec.get('replicas', 1),
            selector=client.V1LabelSelector(
                match_labels={"app": name}
            ),
            template=client.V1PodTemplateSpec(
                metadata=client.V1ObjectMeta(
                    labels={"app": name}
                ),
                spec=client.V1PodSpec(
                    containers=[
                        client.V1Container(
                            name="website",
                            image="nginx:latest",
                            ports=[client.V1ContainerPort(container_port=80)],
                            env=[
                                client.V1EnvVar(
                                    name="GIT_REPO",
                                    value=spec.get('gitRepo', '')
                                )
                            ]
                        )
                    ]
                )
            )
        )
    )
    
    # Create the deployment
    apps_v1.create_namespaced_deployment(namespace, deployment)
    
    # Create service
    service = client.V1Service(
        metadata=client.V1ObjectMeta(
            name=f"{name}-service",
            namespace=namespace,
            labels={"app": name, "managed-by": "website-operator"}
        ),
        spec=client.V1ServiceSpec(
            selector={"app": name},
            ports=[
                client.V1ServicePort(
                    port=80,
                    target_port=80
                )
            ]
        )
    )
    
    v1.create_namespaced_service(namespace, service)
    
    return {"message": f"Website {name} created successfully"}

@kopf.on.update('stable.example.com', 'v1', 'websites')
def update_website(spec, name, namespace, **kwargs):
    """Handle website updates"""
    
    # Update deployment replicas
    apps_v1.patch_namespaced_deployment_scale(
        name=f"{name}-deployment",
        namespace=namespace,
        body=client.V1Scale(
            spec=client.V1ScaleSpec(
                replicas=spec.get('replicas', 1)
            )
        )
    )
    
    return {"message": f"Website {name} updated successfully"}

@kopf.on.delete('stable.example.com', 'v1', 'websites')
def delete_website(name, namespace, **kwargs):
    """Handle website deletion"""
    
    # Delete deployment
    try:
        apps_v1.delete_namespaced_deployment(
            name=f"{name}-deployment",
            namespace=namespace
        )
    except client.ApiException:
        pass
    
    # Delete service
    try:
        v1.delete_namespaced_service(
            name=f"{name}-service",
            namespace=namespace
        )
    except client.ApiException:
        pass
    
    return {"message": f"Website {name} deleted successfully"}
```

### Go Controller using controller-runtime
```go
// controller.go
package main

import (
    "context"
    "fmt"
    
    appsv1 "k8s.io/api/apps/v1"
    corev1 "k8s.io/api/core/v1"
    metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
    "k8s.io/apimachinery/pkg/runtime"
    ctrl "sigs.k8s.io/controller-runtime"
    "sigs.k8s.io/controller-runtime/pkg/client"
    
    stablev1 "github.com/example/website-operator/api/v1"
)

type WebsiteReconciler struct {
    client.Client
    Scheme *runtime.Scheme
}

func (r *WebsiteReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
    // Fetch the Website instance
    website := &stablev1.Website{}
    err := r.Get(ctx, req.NamespacedName, website)
    if err != nil {
        return ctrl.Result{}, client.IgnoreNotFound(err)
    }

    // Create or update deployment
    deployment := &appsv1.Deployment{
        ObjectMeta: metav1.ObjectMeta{
            Name:      website.Name + "-deployment",
            Namespace: website.Namespace,
        },
        Spec: appsv1.DeploymentSpec{
            Replicas: &website.Spec.Replicas,
            Selector: &metav1.LabelSelector{
                MatchLabels: map[string]string{"app": website.Name},
            },
            Template: corev1.PodTemplateSpec{
                ObjectMeta: metav1.ObjectMeta{
                    Labels: map[string]string{"app": website.Name},
                },
                Spec: corev1.PodSpec{
                    Containers: []corev1.Container{
                        {
                            Name:  "website",
                            Image: "nginx:latest",
                            Ports: []corev1.ContainerPort{
                                {ContainerPort: 80},
                            },
                        },
                    },
                },
            },
        },
    }

    // Set owner reference
    ctrl.SetControllerReference(website, deployment, r.Scheme)

    // Create or update
    err = r.Client.Create(ctx, deployment)
    if err != nil {
        // If exists, update it
        existingDeployment := &appsv1.Deployment{}
        err = r.Get(ctx, client.ObjectKey{Name: deployment.Name, Namespace: deployment.Namespace}, existingDeployment)
        if err == nil {
            existingDeployment.Spec = deployment.Spec
            err = r.Update(ctx, existingDeployment)
        }
    }

    return ctrl.Result{}, err
}

func (r *WebsiteReconciler) SetupWithManager(mgr ctrl.Manager) error {
    return ctrl.NewControllerManagedBy(mgr).
        For(&stablev1.Website{}).
        Owns(&appsv1.Deployment{}).
        Complete(r)
}
```

## Admission Controllers

### Validating Admission Webhook
Like having **quality inspectors** for city permit applications:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingAdmissionWebhook
metadata:
  name: validate-pods
webhooks:
- name: pod-validator.example.com
  clientConfig:
    service:
      name: pod-validator
      namespace: default
      path: "/validate"
  rules:
  - operations: ["CREATE", "UPDATE"]
    apiGroups: [""]
    apiVersions: ["v1"]
    resources: ["pods"]
  admissionReviewVersions: ["v1", "v1beta1"]
  sideEffects: None
  failurePolicy: Fail
```

```python
# Validation webhook server
from flask import Flask, request, jsonify
import base64
import json

app = Flask(__name__)

@app.route('/validate', methods=['POST'])
def validate_pod():
    admission_review = request.get_json()
    
    # Extract pod from admission request
    pod = admission_review["request"]["object"]
    
    # Validation logic
    allowed = True
    message = ""
    
    # Check if pod has resource limits
    containers = pod.get("spec", {}).get("containers", [])
    for container in containers:
        resources = container.get("resources", {})
        if not resources.get("limits"):
            allowed = False
            message = f"Container {container['name']} must have resource limits"
            break
    
    # Check for security context
    security_context = pod.get("spec", {}).get("securityContext", {})
    if not security_context.get("runAsNonRoot"):
        allowed = False
        message = "Pod must run as non-root user"
    
    # Return admission response
    return jsonify({
        "apiVersion": "admission.k8s.io/v1",
        "kind": "AdmissionReview",
        "response": {
            "uid": admission_review["request"]["uid"],
            "allowed": allowed,
            "status": {"message": message} if not allowed else {}
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8443, ssl_context='adhoc')
```

### Mutating Admission Webhook
Like having **automatic form completion** services:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingAdmissionWebhook
metadata:
  name: pod-mutator
webhooks:
- name: pod-mutator.example.com
  clientConfig:
    service:
      name: pod-mutator
      namespace: default
      path: "/mutate"
  rules:
  - operations: ["CREATE"]
    apiGroups: [""]
    apiVersions: ["v1"]
    resources: ["pods"]
  admissionReviewVersions: ["v1"]
  sideEffects: None
```

```python
# Mutation webhook server
import json
import base64
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/mutate', methods=['POST'])
def mutate_pod():
    admission_review = request.get_json()
    pod = admission_review["request"]["object"]
    
    # Create patches to modify the pod
    patches = []
    
    # Add default labels
    if "labels" not in pod.get("metadata", {}):
        patches.append({
            "op": "add",
            "path": "/metadata/labels",
            "value": {}
        })
    
    patches.append({
        "op": "add",
        "path": "/metadata/labels/managed-by",
        "value": "admission-controller"
    })
    
    # Add sidecar container
    sidecar = {
        "name": "logging-sidecar",
        "image": "fluentd:latest",
        "volumeMounts": [{
            "name": "shared-logs",
            "mountPath": "/var/log"
        }]
    }
    
    patches.append({
        "op": "add",
        "path": "/spec/containers/-",
        "value": sidecar
    })
    
    # Add shared volume
    if "volumes" not in pod.get("spec", {}):
        patches.append({
            "op": "add",
            "path": "/spec/volumes",
            "value": []
        })
    
    patches.append({
        "op": "add",
        "path": "/spec/volumes/-",
        "value": {
            "name": "shared-logs",
            "emptyDir": {}
        }
    })
    
    # Encode patches
    patch_bytes = json.dumps(patches).encode()
    patch_b64 = base64.b64encode(patch_bytes).decode()
    
    return jsonify({
        "apiVersion": "admission.k8s.io/v1",
        "kind": "AdmissionReview",
        "response": {
            "uid": admission_review["request"]["uid"],
            "allowed": True,
            "patchType": "JSONPatch",
            "patch": patch_b64
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8443, ssl_context='adhoc')
```

## API Aggregation

### Custom API Server
Like creating a **specialized government office** with its own services:

```yaml
apiVersion: apiregistration.k8s.io/v1
kind: APIService
metadata:
  name: v1alpha1.metrics.k8s.io
spec:
  service:
    name: custom-metrics-apiserver
    namespace: custom-metrics
  group: metrics.k8s.io
  version: v1alpha1
  insecureSkipTLSVerify: true
  groupPriorityMinimum: 100
  versionPriority: 100
```

```go
// Custom API server example (simplified)
package main

import (
    "context"
    "fmt"
    "net/http"
    
    metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
    "k8s.io/apimachinery/pkg/runtime"
    "k8s.io/apiserver/pkg/registry/rest"
    genericapiserver "k8s.io/apiserver/pkg/server"
)

type CustomMetric struct {
    metav1.TypeMeta   `json:",inline"`
    metav1.ObjectMeta `json:"metadata,omitempty"`
    
    Value     float64 `json:"value"`
    Timestamp int64   `json:"timestamp"`
}

type CustomMetricList struct {
    metav1.TypeMeta `json:",inline"`
    metav1.ListMeta `json:"metadata,omitempty"`
    
    Items []CustomMetric `json:"items"`
}

// REST storage implementation
type MetricStorage struct{}

func (r *MetricStorage) New() runtime.Object {
    return &CustomMetric{}
}

func (r *MetricStorage) NewList() runtime.Object {
    return &CustomMetricList{}
}

func (r *MetricStorage) Get(ctx context.Context, name string, options *metav1.GetOptions) (runtime.Object, error) {
    // Implement metric retrieval logic
    return &CustomMetric{
        ObjectMeta: metav1.ObjectMeta{Name: name},
        Value:      42.0,
        Timestamp:  1234567890,
    }, nil
}

func (r *MetricStorage) List(ctx context.Context, options *metav1.ListOptions) (runtime.Object, error) {
    // Implement metric listing logic
    return &CustomMetricList{
        Items: []CustomMetric{
            {
                ObjectMeta: metav1.ObjectMeta{Name: "cpu-usage"},
                Value:      75.5,
                Timestamp:  1234567890,
            },
        },
    }, nil
}

func main() {
    // Set up custom API server
    config := genericapiserver.NewRecommendedConfig(Codecs)
    server, err := config.Complete().New("custom-metrics", genericapiserver.NewEmptyDelegate())
    if err != nil {
        panic(err)
    }
    
    // Register API group
    apiGroupInfo := genericapiserver.NewDefaultAPIGroupInfo("metrics.k8s.io", Scheme, metav1.ParameterCodec, Codecs)
    apiGroupInfo.VersionedResourcesStorageMap["v1alpha1"] = map[string]rest.Storage{
        "metrics": &MetricStorage{},
    }
    
    server.InstallAPIGroup(&apiGroupInfo)
    
    // Start server
    server.PrepareRun().Run(context.Background())
}
```

## Scheduler Extensions

### Custom Scheduler
Like creating a **specialized resource allocation system**:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: custom-scheduler-config
  namespace: kube-system
data:
  config.yaml: |
    apiVersion: kubescheduler.config.k8s.io/v1beta3
    kind: KubeSchedulerConfiguration
    profiles:
    - schedulerName: custom-scheduler
      plugins:
        score:
          enabled:
          - name: NodeResourcesFit
          - name: NodeAffinity
          disabled:
          - name: NodeResourcesLeastAllocated
      pluginConfig:
      - name: NodeResourcesFit
        args:
          scoringStrategy:
            type: MostAllocated

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: custom-scheduler
  namespace: kube-system
spec:
  replicas: 1
  selector:
    matchLabels:
      app: custom-scheduler
  template:
    metadata:
      labels:
        app: custom-scheduler
    spec:
      serviceAccountName: custom-scheduler
      containers:
      - name: kube-scheduler
        image: k8s.gcr.io/kube-scheduler:v1.28.0
        command:
        - kube-scheduler
        - --config=/etc/kubernetes/scheduler-config.yaml
        - --v=2
        volumeMounts:
        - name: config
          mountPath: /etc/kubernetes
      volumes:
      - name: config
        configMap:
          name: custom-scheduler-config
```

### Using Custom Scheduler
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-custom-scheduler
spec:
  schedulerName: custom-scheduler  # Use custom scheduler
  containers:
  - name: app
    image: nginx:latest
```

## Device Plugins

### Custom Device Plugin
Like managing **specialized city equipment**:

```go
// GPU device plugin example (simplified)
package main

import (
    "context"
    "net"
    "path"
    "time"
    
    "google.golang.org/grpc"
    pluginapi "k8s.io/kubelet/pkg/apis/deviceplugin/v1beta1"
)

type GPUDevicePlugin struct {
    socket string
    server *grpc.Server
}

func (m *GPUDevicePlugin) GetDevicePluginOptions(context.Context, *pluginapi.Empty) (*pluginapi.DevicePluginOptions, error) {
    return &pluginapi.DevicePluginOptions{}, nil
}

func (m *GPUDevicePlugin) ListAndWatch(e *pluginapi.Empty, s pluginapi.DevicePlugin_ListAndWatchServer) error {
    devices := []*pluginapi.Device{
        {ID: "gpu-0", Health: pluginapi.Healthy},
        {ID: "gpu-1", Health: pluginapi.Healthy},
    }
    
    s.Send(&pluginapi.ListAndWatchResponse{Devices: devices})
    
    for {
        time.Sleep(10 * time.Second)
        s.Send(&pluginapi.ListAndWatchResponse{Devices: devices})
    }
}

func (m *GPUDevicePlugin) Allocate(ctx context.Context, reqs *pluginapi.AllocateRequest) (*pluginapi.AllocateResponse, error) {
    responses := &pluginapi.AllocateResponse{}
    
    for _, req := range reqs.ContainerRequests {
        response := &pluginapi.ContainerAllocateResponse{
            Envs: map[string]string{
                "NVIDIA_VISIBLE_DEVICES": req.DevicesIDs[0],
            },
            Mounts: []*pluginapi.Mount{
                {
                    ContainerPath: "/dev/nvidia0",
                    HostPath:      "/dev/nvidia0",
                },
            },
        }
        responses.ContainerResponses = append(responses.ContainerResponses, response)
    }
    
    return responses, nil
}

func main() {
    plugin := &GPUDevicePlugin{
        socket: path.Join(pluginapi.DevicePluginPath, "gpu.sock"),
    }
    
    // Start gRPC server
    lis, err := net.Listen("unix", plugin.socket)
    if err != nil {
        panic(err)
    }
    
    plugin.server = grpc.NewServer()
    pluginapi.RegisterDevicePluginServer(plugin.server, plugin)
    
    go plugin.server.Serve(lis)
    
    // Register with kubelet
    conn, err := grpc.Dial(pluginapi.KubeletSocket, grpc.WithInsecure())
    if err != nil {
        panic(err)
    }
    defer conn.Close()
    
    client := pluginapi.NewRegistrationClient(conn)
    request := &pluginapi.RegisterRequest{
        Version:      pluginapi.Version,
        Endpoint:     "gpu.sock",
        ResourceName: "example.com/gpu",
    }
    
    _, err = client.Register(context.Background(), request)
    if err != nil {
        panic(err)
    }
    
    select {} // Keep running
}
```

## Operator Patterns

### Operator SDK Example
```bash
# Install Operator SDK
curl -LO https://github.com/operator-framework/operator-sdk/releases/download/v1.32.0/operator-sdk_linux_amd64
chmod +x operator-sdk_linux_amd64 && sudo mv operator-sdk_linux_amd64 /usr/local/bin/operator-sdk

# Create new operator project
operator-sdk init --domain=example.com --repo=github.com/example/database-operator

# Create API
operator-sdk create api --group=data --version=v1 --kind=Database --resource --controller

# Generate manifests
make manifests

# Build and deploy
make docker-build docker-push IMG=example.com/database-operator:v0.0.1
make deploy IMG=example.com/database-operator:v0.0.1
```

### Helm Operator
```yaml
# Create Helm-based operator
apiVersion: charts.helm.k8s.io/v1
kind: HelmChart
metadata:
  name: my-app
  namespace: default
spec:
  chart: stable/mysql
  targetNamespace: default
  valuesContent: |-
    mysqlUser: myuser
    mysqlPassword: mypassword
    mysqlDatabase: mydatabase
```

## Best Practices

### 1. CRD Design
```yaml
# Use proper validation
schema:
  openAPIV3Schema:
    type: object
    required: ["spec"]
    properties:
      spec:
        type: object
        required: ["replicas"]

# Add printer columns
additionalPrinterColumns:
- name: Status
  type: string
  jsonPath: .status.phase

# Use subresources
subresources:
  status: {}
  scale:
    specReplicasPath: .spec.replicas
    statusReplicasPath: .status.replicas
```

### 2. Controller Best Practices
```go
// Use controller-runtime patterns
// Implement proper error handling
// Use exponential backoff
// Set owner references
ctrl.SetControllerReference(parent, child, r.Scheme)

// Use finalizers for cleanup
if obj.DeletionTimestamp != nil {
    return r.handleDeletion(ctx, obj)
}
```

### 3. Security
```yaml
# Use RBAC for operators
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: database-operator
rules:
- apiGroups: ["data.example.com"]
  resources: ["databases"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
```

### 4. Testing
```bash
# Test CRDs
kubectl apply --dry-run=client -f crd.yaml

# Test controllers
go test ./controllers/...

# Integration testing
make test
```

## Troubleshooting Extensions

### CRD Issues
```bash
# Check CRD status
kubectl get crd
kubectl describe crd websites.stable.example.com

# Validate CRD schema
kubectl apply --dry-run=server -f custom-resource.yaml
```

### Controller Issues
```bash
# Check controller logs
kubectl logs -n system deployment/controller-manager

# Check RBAC permissions
kubectl auth can-i create deployments --as=system:serviceaccount:system:controller

# Debug controller behavior
kubectl get events --sort-by=.metadata.creationTimestamp
```

### Admission Controller Issues
```bash
# Check webhook configuration
kubectl get validatingwebhookconfigurations
kubectl get mutatingwebhookconfigurations

# Test webhook connectivity
kubectl run test-pod --image=nginx --dry-run=server

# Check webhook logs
kubectl logs -n webhook-system deployment/webhook-server
```

## Next Steps

After mastering Kubernetes extensions:
1. **Build Production Operators**: Implement complex business logic
2. **Learn OLM**: Operator Lifecycle Manager for operator distribution
3. **Explore Service Mesh**: Istio, Linkerd extensions
4. **Study GitOps**: ArgoCD, Flux operators
5. **Practice Security**: Policy engines like OPA Gatekeeper

Remember: Extending Kubernetes is like expanding your city's capabilities - start with simple extensions, follow established patterns, ensure proper security and testing, and always consider the impact on cluster stability and performance!