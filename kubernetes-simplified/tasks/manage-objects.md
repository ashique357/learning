                          # Manage Kubernetes Objects

Think of Kubernetes objects as **LEGO building blocks** - each piece has a specific purpose, and you combine them to build complex applications. Managing these objects is like being an **architect** who designs, builds, and maintains structures.

## Understanding Kubernetes Objects

### What are Kubernetes Objects?
Objects are like **blueprints and actual buildings**:
- **Desired State**: What you want (the blueprint)
- **Current State**: What actually exists (the building)
- **Controller**: The construction crew that makes reality match the blueprint

```yaml
# Every object has this structure
apiVersion: v1        # Which version of the blueprint format
kind: Pod            # What type of building (Pod, Service, etc.)
metadata:            # Name tag and labels
  name: my-app
  labels:
    app: web-server
spec:                # The blueprint (what you want)
  containers:
  - name: web
    image: nginx
status:              # Current reality (Kubernetes fills this)
  phase: Running
```

## Object Management Approaches

### 1. Imperative Commands
Like giving **direct orders** to a construction crew:

```bash
# Create objects directly
kubectl create deployment nginx --image=nginx
kubectl expose deployment nginx --port=80 --type=LoadBalancer
kubectl scale deployment nginx --replicas=3

# Quick and easy for:
# - Learning and experimentation
# - One-time tasks
# - Emergency fixes
```

### 2. Imperative Object Configuration
Like handing **written instructions** to the crew:

```bash
# Create from file
kubectl create -f deployment.yaml

# Update existing object
kubectl replace -f deployment.yaml

# Delete using file
kubectl delete -f deployment.yaml

# Good for:
# - Simple configurations
# - When you need to see exactly what changed
```

### 3. Declarative Object Configuration
Like having a **smart construction system** that reads blueprints and builds automatically:

```bash
# Apply configuration (create or update)
kubectl apply -f deployment.yaml
kubectl apply -f ./configs/          # Apply entire directory
kubectl apply -k ./kustomization/    # Apply with Kustomize

# Best for:
# - Production environments
# - GitOps workflows
# - Complex applications
```

## Working with Object Files

### Basic YAML Structure
Think of YAML as a **structured recipe card**:

```yaml
# deployment.yaml - Recipe for a web application
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app                    # Name of your dish
  labels:
    app: web-app                   # Category tag
    version: v1.0                  # Version tag
spec:
  replicas: 3                      # How many servings
  selector:                        # How to identify your dish
    matchLabels:
      app: web-app
  template:                        # Recipe for each serving
    metadata:
      labels:
        app: web-app
    spec:
      containers:
      - name: web                  # Main ingredient
        image: nginx:1.21          # Specific brand/version
        ports:
        - containerPort: 80        # Serving port
        resources:                 # Resource requirements
          requests:
            memory: "64Mi"
            cpu: "250m"
          limits:
            memory: "128Mi"
            cpu: "500m"
```

### Managing Multiple Objects
Like managing a **restaurant menu** with multiple dishes:

```yaml
# multi-object.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
spec:
  # ... deployment spec
---                               # Separator between objects
apiVersion: v1
kind: Service
metadata:
  name: frontend-service
spec:
  # ... service spec
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  database_url: "postgres://db:5432/myapp"
```

## Common Object Operations

### Creating Objects
Like **opening new businesses** in your city:

```bash
# From command line (imperative)
kubectl create deployment web --image=nginx
kubectl create service clusterip web --tcp=80:80

# From files (declarative)
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# From directories
kubectl apply -f ./k8s-configs/

# With dry-run (test without creating)
kubectl apply -f deployment.yaml --dry-run=client -o yaml
```

### Viewing Objects
Like **checking on your businesses**:

```bash
# List objects
kubectl get pods                          # All pods
kubectl get pods -l app=web              # Pods with specific label
kubectl get pods -o wide                 # More details
kubectl get pods -o yaml                 # Full YAML output

# Detailed information
kubectl describe pod my-pod              # Like a detailed inspection report
kubectl describe deployment web          # Deployment details

# Watch for changes (live updates)
kubectl get pods --watch                 # Like a security camera feed
```

### Updating Objects
Like **renovating your businesses**:

```bash
# Edit directly (opens editor)
kubectl edit deployment web

# Update from file
kubectl apply -f updated-deployment.yaml

# Patch specific fields
kubectl patch deployment web -p '{"spec":{"replicas":5}}'

# Update image
kubectl set image deployment/web container=nginx:1.22

# Rolling update with annotation
kubectl annotate deployment web deployment.kubernetes.io/revision=2
```

### Deleting Objects
Like **closing businesses** you no longer need:

```bash
# Delete specific objects
kubectl delete pod my-pod
kubectl delete deployment web
kubectl delete service web-service

# Delete from file
kubectl delete -f deployment.yaml

# Delete by label
kubectl delete pods -l app=web

# Delete all objects of a type
kubectl delete deployments --all

# Force delete (emergency)
kubectl delete pod stuck-pod --force --grace-period=0
```

## Labels and Selectors

### Understanding Labels
Labels are like **business categories and tags**:

```yaml
metadata:
  labels:
    app: web-server              # What type of business
    version: v2.1                # Which version
    environment: production      # Which environment
    team: frontend              # Which team owns it
    cost-center: engineering    # Billing information
```

### Using Selectors
Selectors are like **search filters** to find specific businesses:

```bash
# Equality-based selectors
kubectl get pods -l app=web                    # Exact match
kubectl get pods -l app!=web                   # Not equal
kubectl get pods -l 'app in (web,api)'        # Multiple values

# Set-based selectors
kubectl get pods -l 'environment'              # Has label
kubectl get pods -l '!debug'                   # Doesn't have label

# Multiple conditions (AND)
kubectl get pods -l app=web,environment=prod

# Complex selectors in YAML
selector:
  matchLabels:
    app: web
  matchExpressions:
  - key: version
    operator: In
    values: ["v1.0", "v1.1"]
  - key: environment
    operator: NotIn
    values: ["development"]
```

## Annotations

### Understanding Annotations
Annotations are like **detailed notes** attached to objects:

```yaml
metadata:
  annotations:
    kubernetes.io/created-by: "deployment-controller"
    deployment.kubernetes.io/revision: "3"
    company.com/contact: "team-alpha@company.com"
    company.com/documentation: "https://wiki.company.com/web-app"
    nginx.ingress.kubernetes.io/rewrite-target: "/"
```

### Common Use Cases
```bash
# Add annotation
kubectl annotate pod my-pod description="Web server for user authentication"

# Update annotation
kubectl annotate pod my-pod version=v2.0 --overwrite

# Remove annotation
kubectl annotate pod my-pod version-

# View annotations
kubectl get pod my-pod -o yaml | grep -A 10 annotations
```

## Field Management

### Understanding Field Ownership
Like tracking **who made which changes** to a building:

```bash
# See who manages each field
kubectl get deployment web -o yaml --show-managed-fields

# Apply with specific field manager
kubectl apply -f deployment.yaml --field-manager=my-tool

# Force ownership of fields
kubectl apply -f deployment.yaml --force-conflicts --field-manager=my-tool
```

### Server-Side Apply
Like having a **smart building system** that handles conflicts:

```bash
# Use server-side apply (recommended for tools)
kubectl apply --server-side -f deployment.yaml

# With conflict resolution
kubectl apply --server-side --force-conflicts -f deployment.yaml
```

## Advanced Object Management

### Using Kustomize
Like having **templates** for similar buildings:

```yaml
# kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
- deployment.yaml
- service.yaml

patchesStrategicMerge:
- production-patch.yaml

images:
- name: nginx
  newTag: 1.22

replicas:
- name: web-deployment
  count: 5
```

```bash
# Apply with Kustomize
kubectl apply -k ./overlays/production/
```

### Helm Charts
Like using **architectural blueprints** that can be customized:

```bash
# Install from Helm chart
helm install my-app ./my-chart

# Upgrade application
helm upgrade my-app ./my-chart --set replicas=5

# See what Kubernetes objects would be created
helm template my-app ./my-chart
```

### GitOps Workflow
Like having **version control** for your city planning:

```bash
# 1. Make changes to YAML files in Git
git add deployment.yaml
git commit -m "Update web app to v2.1"
git push origin main

# 2. GitOps tool (ArgoCD/Flux) automatically applies changes
# 3. Kubernetes updates to match Git repository
```

## Troubleshooting Object Management

### Common Issues and Solutions

#### 1. Object Already Exists
```bash
# Problem: "already exists" error
# Solution: Use apply instead of create
kubectl apply -f deployment.yaml

# Or replace existing object
kubectl replace -f deployment.yaml
```

#### 2. Field Conflicts
```bash
# Problem: "field managed by other field manager"
# Solution: Force apply or use server-side apply
kubectl apply -f deployment.yaml --force-conflicts
kubectl apply --server-side -f deployment.yaml
```

#### 3. Validation Errors
```bash
# Problem: Invalid YAML or missing required fields
# Solution: Validate before applying
kubectl apply -f deployment.yaml --dry-run=client --validate=true

# Check YAML syntax
kubectl apply -f deployment.yaml --dry-run=server -o yaml
```

#### 4. Resource Quotas
```bash
# Problem: "exceeded quota" error
# Solution: Check resource usage
kubectl describe quota
kubectl top nodes
kubectl top pods
```

## Best Practices

### 1. File Organization
```
k8s-configs/
├── base/                    # Common configurations
│   ├── deployment.yaml
│   └── service.yaml
├── overlays/               # Environment-specific
│   ├── development/
│   ├── staging/
│   └── production/
└── components/             # Reusable pieces
    ├── database/
    └── monitoring/
```

### 2. Naming Conventions
```yaml
metadata:
  name: web-app-frontend     # app-component-role
  labels:
    app.kubernetes.io/name: web-app
    app.kubernetes.io/component: frontend
    app.kubernetes.io/version: "1.2.3"
    app.kubernetes.io/managed-by: helm
```

### 3. Resource Management
```yaml
spec:
  containers:
  - name: web
    resources:
      requests:              # Minimum needed
        memory: "64Mi"
        cpu: "100m"
      limits:               # Maximum allowed
        memory: "128Mi"
        cpu: "200m"
```

### 4. Security Practices
```yaml
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    fsGroup: 2000
  containers:
  - name: web
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop:
        - ALL
```

## Next Steps

After mastering object management:
1. **Learn about Workloads**: Deployments, StatefulSets, DaemonSets
2. **Understand Services**: How to expose and connect applications
3. **Explore Configuration**: ConfigMaps and Secrets
4. **Practice GitOps**: Version control your Kubernetes configurations
5. **Study Operators**: Advanced object management patterns

Remember: Good object management is like good city planning - it requires clear organization, consistent naming, proper documentation, and regular maintenance!