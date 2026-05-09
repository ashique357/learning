# Configure Pods and Containers

Think of configuring pods and containers like **setting up apartments** in a building. Each apartment (container) needs specific settings for utilities, security, storage, and resources, while the building (pod) provides shared infrastructure.

## Understanding Pod Configuration

### Basic Pod Structure
A pod is like an **apartment unit** that can house one or more containers:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web-app-pod
  labels:
    app: web-app
    tier: frontend
spec:
  containers:                    # Tenants in the apartment
  - name: web-server            # Primary tenant
    image: nginx:1.21
    ports:
    - containerPort: 80
  - name: log-collector         # Secondary tenant (sidecar)
    image: fluentd:latest
  restartPolicy: Always         # What to do if tenants leave
  nodeSelector:                 # Which building to place apartment
    disktype: ssd
```

## Container Configuration

### Basic Container Settings
Like setting up **utilities and appliances** for each tenant:

```yaml
spec:
  containers:
  - name: web-app
    image: nginx:1.21                    # Which software to install
    imagePullPolicy: Always              # When to update software
    
    # Resource allocation (like utility limits)
    resources:
      requests:                          # Minimum guaranteed
        memory: "64Mi"
        cpu: "250m"
      limits:                           # Maximum allowed
        memory: "128Mi"
        cpu: "500m"
    
    # Network configuration
    ports:
    - name: http
      containerPort: 80
      protocol: TCP
    
    # Health checks (like smoke detectors)
    livenessProbe:
      httpGet:
        path: /health
        port: 80
      initialDelaySeconds: 30
      periodSeconds: 10
    
    readinessProbe:
      httpGet:
        path: /ready
        port: 80
      initialDelaySeconds: 5
      periodSeconds: 5
```

### Environment Variables
Like setting **personal preferences** for each tenant:

```yaml
spec:
  containers:
  - name: web-app
    image: myapp:latest
    env:
    # Direct values
    - name: DATABASE_HOST
      value: "postgres.example.com"
    - name: DEBUG_MODE
      value: "false"
    
    # From ConfigMap (shared settings)
    - name: APP_CONFIG
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: config.properties
    
    # From Secret (private information)
    - name: DATABASE_PASSWORD
      valueFrom:
        secretKeyRef:
          name: db-secret
          key: password
    
    # All keys from ConfigMap
    envFrom:
    - configMapRef:
        name: app-config
    - secretRef:
        name: app-secrets
```

### Volume Mounts
Like connecting **storage units** to apartments:

```yaml
spec:
  containers:
  - name: web-app
    image: nginx:1.21
    volumeMounts:
    # Temporary storage (like a closet)
    - name: temp-storage
      mountPath: /tmp/cache
    
    # Persistent storage (like a garage)
    - name: data-storage
      mountPath: /var/lib/data
    
    # Configuration files (like instruction manuals)
    - name: config-volume
      mountPath: /etc/config
      readOnly: true
    
    # Secrets (like a safe)
    - name: secret-volume
      mountPath: /etc/secrets
      readOnly: true
  
  volumes:
  # Temporary storage
  - name: temp-storage
    emptyDir: {}
  
  # Persistent storage
  - name: data-storage
    persistentVolumeClaim:
      claimName: web-app-pvc
  
  # Configuration from ConfigMap
  - name: config-volume
    configMap:
      name: app-config
  
  # Secrets
  - name: secret-volume
    secret:
      secretName: app-secrets
```

## Advanced Container Configuration

### Security Context
Like setting **security rules** for the apartment:

```yaml
spec:
  # Pod-level security (building rules)
  securityContext:
    runAsUser: 1000                    # Default user ID
    runAsGroup: 3000                   # Default group ID
    fsGroup: 2000                      # File system group
    
  containers:
  - name: web-app
    image: nginx:1.21
    # Container-level security (apartment rules)
    securityContext:
      runAsNonRoot: true               # Don't run as admin
      runAsUser: 1001                  # Specific user for this container
      allowPrivilegeEscalation: false  # Can't gain more privileges
      readOnlyRootFilesystem: true     # Can't modify system files
      capabilities:
        drop:                          # Remove dangerous permissions
        - ALL
        add:                          # Add only needed permissions
        - NET_BIND_SERVICE
```

### Resource Management
Like setting **utility budgets** for each tenant:

```yaml
spec:
  containers:
  - name: web-app
    image: nginx:1.21
    resources:
      # Requests (guaranteed allocation)
      requests:
        memory: "64Mi"               # Minimum RAM
        cpu: "250m"                  # Minimum CPU (0.25 cores)
        ephemeral-storage: "1Gi"     # Minimum disk space
      
      # Limits (maximum allowed)
      limits:
        memory: "128Mi"              # Maximum RAM
        cpu: "500m"                  # Maximum CPU (0.5 cores)
        ephemeral-storage: "2Gi"     # Maximum disk space
        
  # Quality of Service classes
  # Guaranteed: requests = limits for all resources
  # Burstable: requests < limits
  # BestEffort: no requests or limits specified
```

### Startup and Lifecycle
Like setting **move-in and move-out procedures**:

```yaml
spec:
  containers:
  - name: web-app
    image: nginx:1.21
    
    # Startup probe (is the tenant ready to move in?)
    startupProbe:
      httpGet:
        path: /startup
        port: 80
      failureThreshold: 30           # Try 30 times
      periodSeconds: 10              # Every 10 seconds
    
    # Liveness probe (is the tenant still alive?)
    livenessProbe:
      httpGet:
        path: /health
        port: 80
      initialDelaySeconds: 30
      periodSeconds: 10
      timeoutSeconds: 5
      failureThreshold: 3
    
    # Readiness probe (is the tenant ready for visitors?)
    readinessProbe:
      httpGet:
        path: /ready
        port: 80
      initialDelaySeconds: 5
      periodSeconds: 5
    
    # Lifecycle hooks
    lifecycle:
      postStart:                     # After tenant moves in
        exec:
          command: ["/bin/sh", "-c", "echo 'Container started' > /tmp/started"]
      preStop:                       # Before tenant moves out
        exec:
          command: ["/bin/sh", "-c", "nginx -s quit; while killall -0 nginx; do sleep 1; done"]
```

## Multi-Container Pods

### Sidecar Pattern
Like having a **roommate** who provides support services:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web-with-logging
spec:
  containers:
  # Main application (primary tenant)
  - name: web-app
    image: nginx:1.21
    ports:
    - containerPort: 80
    volumeMounts:
    - name: shared-logs
      mountPath: /var/log/nginx
  
  # Logging sidecar (helpful roommate)
  - name: log-shipper
    image: fluentd:latest
    volumeMounts:
    - name: shared-logs
      mountPath: /var/log/nginx
      readOnly: true
    env:
    - name: FLUENTD_CONF
      value: "fluent.conf"
  
  volumes:
  - name: shared-logs
    emptyDir: {}
```

### Init Containers
Like **setup crew** that prepares the apartment before tenants move in:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web-with-setup
spec:
  # Setup containers (run before main containers)
  initContainers:
  - name: database-migration
    image: migrate/migrate:latest
    command: ['migrate', '-path', '/migrations', '-database', 'postgres://...', 'up']
    
  - name: config-setup
    image: busybox:latest
    command: ['sh', '-c', 'cp /config-template/* /shared-config/']
    volumeMounts:
    - name: shared-config
      mountPath: /shared-config
  
  # Main application containers
  containers:
  - name: web-app
    image: myapp:latest
    volumeMounts:
    - name: shared-config
      mountPath: /etc/config
  
  volumes:
  - name: shared-config
    emptyDir: {}
```

## Configuration Management

### Using ConfigMaps
Like having **shared building instructions** that all tenants can access:

```yaml
# Create ConfigMap
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  # Simple key-value pairs
  database_host: "postgres.example.com"
  database_port: "5432"
  debug_mode: "false"
  
  # Configuration files
  nginx.conf: |
    server {
        listen 80;
        server_name localhost;
        location / {
            root /usr/share/nginx/html;
            index index.html;
        }
    }
  
  app.properties: |
    spring.datasource.url=jdbc:postgresql://postgres:5432/mydb
    spring.jpa.hibernate.ddl-auto=update
    logging.level.com.myapp=DEBUG
```

```yaml
# Use ConfigMap in Pod
spec:
  containers:
  - name: web-app
    image: myapp:latest
    
    # Environment variables from ConfigMap
    envFrom:
    - configMapRef:
        name: app-config
    
    # Mount as files
    volumeMounts:
    - name: config-volume
      mountPath: /etc/config
    - name: nginx-config
      mountPath: /etc/nginx/nginx.conf
      subPath: nginx.conf
  
  volumes:
  - name: config-volume
    configMap:
      name: app-config
  - name: nginx-config
    configMap:
      name: app-config
      items:
      - key: nginx.conf
        path: nginx.conf
```

### Using Secrets
Like having **private safes** for sensitive information:

```yaml
# Create Secret
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
type: Opaque
data:
  # Base64 encoded values
  database-password: cGFzc3dvcmQxMjM=
  api-key: YWJjZGVmZ2hpams=
stringData:
  # Plain text (automatically encoded)
  username: myuser
  connection-string: "postgres://user:pass@host:5432/db"
```

```bash
# Create Secret from command line
kubectl create secret generic app-secrets \
  --from-literal=username=myuser \
  --from-literal=password=mypassword \
  --from-file=ssh-key=/path/to/ssh/key

# Create TLS Secret
kubectl create secret tls tls-secret \
  --cert=path/to/tls.crt \
  --key=path/to/tls.key
```

```yaml
# Use Secret in Pod
spec:
  containers:
  - name: web-app
    image: myapp:latest
    
    # Environment variables from Secret
    env:
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: app-secrets
          key: database-password
    
    # Mount as files
    volumeMounts:
    - name: secret-volume
      mountPath: /etc/secrets
      readOnly: true
  
  volumes:
  - name: secret-volume
    secret:
      secretName: app-secrets
      defaultMode: 0400              # Read-only for owner
```

## Pod Scheduling and Placement

### Node Selection
Like choosing **which building** to place your apartment:

```yaml
spec:
  # Simple node selection
  nodeSelector:
    disktype: ssd
    zone: us-west-1a
  
  # Advanced node affinity
  affinity:
    nodeAffinity:
      # Must be placed on nodes with these labels
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: kubernetes.io/arch
            operator: In
            values: ["amd64"]
          - key: node-type
            operator: NotIn
            values: ["spot"]
      
      # Prefer nodes with these labels
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 100
        preference:
          matchExpressions:
          - key: zone
            operator: In
            values: ["us-west-1a"]
```

### Pod Affinity and Anti-Affinity
Like deciding **which apartments should be near each other**:

```yaml
spec:
  affinity:
    # Pod affinity (place near similar pods)
    podAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: app
            operator: In
            values: ["database"]
        topologyKey: kubernetes.io/hostname
    
    # Pod anti-affinity (place away from similar pods)
    podAntiAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 100
        podAffinityTerm:
          labelSelector:
            matchExpressions:
            - key: app
              operator: In
              values: ["web-app"]
          topologyKey: kubernetes.io/hostname
```

### Tolerations and Taints
Like having **special permissions** to live in restricted areas:

```yaml
# Node with taint (restricted area)
# kubectl taint nodes node1 key1=value1:NoSchedule

spec:
  # Pod with toleration (special permission)
  tolerations:
  - key: "key1"
    operator: "Equal"
    value: "value1"
    effect: "NoSchedule"
  
  # Tolerate any value for a key
  - key: "environment"
    operator: "Exists"
    effect: "NoSchedule"
  
  # Tolerate for limited time
  - key: "node.kubernetes.io/unreachable"
    operator: "Exists"
    effect: "NoExecute"
    tolerationSeconds: 300
```

## Troubleshooting Pod Configuration

### Common Issues and Solutions

#### 1. ImagePullBackOff
```bash
# Problem: Can't download container image
# Check image name and registry access
kubectl describe pod my-pod

# Solution: Fix image name or add image pull secret
kubectl create secret docker-registry regcred \
  --docker-server=myregistry.com \
  --docker-username=myuser \
  --docker-password=mypass

# Add to pod spec
spec:
  imagePullSecrets:
  - name: regcred
```

#### 2. CrashLoopBackOff
```bash
# Problem: Container keeps crashing
# Check logs and events
kubectl logs my-pod --previous
kubectl describe pod my-pod

# Common causes:
# - Wrong command or entrypoint
# - Missing environment variables
# - Resource limits too low
# - Health check failures
```

#### 3. Pending Pods
```bash
# Problem: Pod stuck in Pending state
# Check scheduling issues
kubectl describe pod my-pod

# Common causes:
# - Insufficient resources
# - Node selector doesn't match any nodes
# - Taints without tolerations
# - Pod affinity/anti-affinity conflicts
```

#### 4. Configuration Issues
```bash
# Problem: ConfigMap or Secret not found
# Check if resources exist
kubectl get configmaps
kubectl get secrets

# Verify references in pod spec
kubectl get pod my-pod -o yaml | grep -A 5 configMap
```

## Best Practices

### 1. Resource Management
```yaml
# Always set resource requests and limits
resources:
  requests:
    memory: "64Mi"
    cpu: "100m"
  limits:
    memory: "128Mi"
    cpu: "200m"
```

### 2. Health Checks
```yaml
# Implement proper health checks
livenessProbe:
  httpGet:
    path: /health
    port: 8080
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
```

### 3. Security
```yaml
# Run as non-root user
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  readOnlyRootFilesystem: true
```

### 4. Configuration
```yaml
# Use ConfigMaps and Secrets for configuration
# Never hardcode sensitive data in images
envFrom:
- configMapRef:
    name: app-config
- secretRef:
    name: app-secrets
```

### 5. Logging
```yaml
# Configure proper logging
# Use structured logging (JSON)
# Log to stdout/stderr for container logs
```

## Next Steps

After mastering pod and container configuration:
1. **Learn Workload Controllers**: Deployments, StatefulSets, DaemonSets
2. **Understand Networking**: Services, Ingress, Network Policies
3. **Explore Storage**: Persistent Volumes, Storage Classes
4. **Study Security**: RBAC, Pod Security Standards, Network Policies
5. **Practice Troubleshooting**: Debug common pod and container issues

Remember: Good pod configuration is like good apartment management - it requires proper resource allocation, security measures, health monitoring, and clear organization!