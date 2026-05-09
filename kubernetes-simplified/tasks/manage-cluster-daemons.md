# Manage Cluster Daemons

Think of cluster daemons like **essential city services** that need to run on every street corner or building - like street lights, traffic signals, or security cameras. In Kubernetes, DaemonSets ensure these critical services run on every node (or selected nodes) in your cluster.

## Understanding DaemonSets

### What are DaemonSets?
Like having **city maintenance crews** that must be present in every district:

- **One pod per node** - Each node gets exactly one copy
- **Automatic scheduling** - New nodes automatically get the daemon
- **System-level services** - Monitoring, logging, networking, security
- **Node lifecycle management** - Pods are cleaned up when nodes are removed

```bash
# Check existing DaemonSets
kubectl get daemonsets --all-namespaces
kubectl get ds -n kube-system

# Common system DaemonSets you might see:
# - kube-proxy (networking)
# - calico-node (CNI networking)
# - fluentd (logging)
# - node-exporter (monitoring)
```

## Basic DaemonSet Configuration

### Simple DaemonSet
Like deploying **street cleaning crews** to every neighborhood:

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: log-collector
  namespace: kube-system
  labels:
    app: log-collector
spec:
  selector:
    matchLabels:
      app: log-collector
  template:
    metadata:
      labels:
        app: log-collector
    spec:
      containers:
      - name: log-collector
        image: fluentd:v1.14
        resources:
          requests:
            memory: "64Mi"
            cpu: "100m"
          limits:
            memory: "128Mi"
            cpu: "200m"
        volumeMounts:
        - name: varlog
          mountPath: /var/log
          readOnly: true
        - name: varlibdockercontainers
          mountPath: /var/lib/docker/containers
          readOnly: true
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
      - name: varlibdockercontainers
        hostPath:
          path: /var/lib/docker/containers
      terminationGracePeriodSeconds: 30
```

### Node Selection
Like assigning **specialized services** only to certain districts:

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: gpu-monitoring
spec:
  selector:
    matchLabels:
      app: gpu-monitoring
  template:
    metadata:
      labels:
        app: gpu-monitoring
    spec:
      # Only run on nodes with GPUs
      nodeSelector:
        accelerator: nvidia-tesla-k80
      
      # Alternative: use node affinity
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: node-type
                operator: In
                values: ["gpu-node"]
      
      containers:
      - name: gpu-monitor
        image: nvidia/gpu-monitoring:latest
        resources:
          requests:
            nvidia.com/gpu: 1
```

## Common DaemonSet Use Cases

### 1. Log Collection
Like having **information gathering services** in every district:

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd-elasticsearch
  namespace: kube-system
spec:
  selector:
    matchLabels:
      name: fluentd-elasticsearch
  template:
    metadata:
      labels:
        name: fluentd-elasticsearch
    spec:
      serviceAccountName: fluentd
      tolerations:
      # Allow running on master nodes
      - key: node-role.kubernetes.io/master
        effect: NoSchedule
      containers:
      - name: fluentd-elasticsearch
        image: quay.io/fluentd_elasticsearch/fluentd:v2.5.2
        env:
        - name: FLUENTD_SYSTEMD_CONF
          value: disable
        - name: FLUENTD_PROMETHEUS_CONF
          value: disable
        resources:
          requests:
            memory: 200Mi
            cpu: 100m
          limits:
            memory: 500Mi
            cpu: 200m
        volumeMounts:
        - name: varlog
          mountPath: /var/log
        - name: varlibdockercontainers
          mountPath: /var/lib/docker/containers
          readOnly: true
        - name: config-volume
          mountPath: /etc/fluent/config.d
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
      - name: varlibdockercontainers
        hostPath:
          path: /var/lib/docker/containers
      - name: config-volume
        configMap:
          name: fluentd-config
```

### 2. Node Monitoring
Like having **health inspectors** check every building:

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-exporter
  namespace: monitoring
spec:
  selector:
    matchLabels:
      app: node-exporter
  template:
    metadata:
      labels:
        app: node-exporter
    spec:
      hostNetwork: true
      hostPID: true
      containers:
      - name: node-exporter
        image: prom/node-exporter:v1.6.0
        args:
        - --path.procfs=/host/proc
        - --path.sysfs=/host/sys
        - --path.rootfs=/host/root
        - --collector.filesystem.mount-points-exclude=^/(sys|proc|dev|host|etc)($$|/)
        ports:
        - containerPort: 9100
          hostPort: 9100
          name: metrics
        resources:
          requests:
            memory: "64Mi"
            cpu: "50m"
          limits:
            memory: "128Mi"
            cpu: "100m"
        volumeMounts:
        - name: proc
          mountPath: /host/proc
          readOnly: true
        - name: sys
          mountPath: /host/sys
          readOnly: true
        - name: root
          mountPath: /host/root
          mountPropagation: HostToContainer
          readOnly: true
      volumes:
      - name: proc
        hostPath:
          path: /proc
      - name: sys
        hostPath:
          path: /sys
      - name: root
        hostPath:
          path: /
```

### 3. Network Management
Like managing **communication infrastructure** in every area:

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: calico-node
  namespace: kube-system
spec:
  selector:
    matchLabels:
      k8s-app: calico-node
  template:
    metadata:
      labels:
        k8s-app: calico-node
    spec:
      hostNetwork: true
      tolerations:
      - effect: NoSchedule
        operator: Exists
      - key: CriticalAddonsOnly
        operator: Exists
      - effect: NoExecute
        operator: Exists
      serviceAccountName: calico-node
      containers:
      - name: calico-node
        image: calico/node:v3.26.0
        env:
        - name: DATASTORE_TYPE
          value: "kubernetes"
        - name: WAIT_FOR_DATASTORE
          value: "true"
        - name: NODENAME
          valueFrom:
            fieldRef:
              fieldPath: spec.nodeName
        - name: CALICO_NETWORKING_BACKEND
          value: "bird"
        - name: CLUSTER_TYPE
          value: "k8s,bgp"
        - name: IP
          value: "autodetect"
        - name: CALICO_IPV4POOL_IPIP
          value: "Always"
        securityContext:
          privileged: true
        resources:
          requests:
            cpu: 250m
        volumeMounts:
        - mountPath: /lib/modules
          name: lib-modules
          readOnly: true
        - mountPath: /run/xtables.lock
          name: xtables-lock
        - mountPath: /var/run/calico
          name: var-run-calico
        - mountPath: /var/lib/calico
          name: var-lib-calico
      volumes:
      - name: lib-modules
        hostPath:
          path: /lib/modules
      - name: var-run-calico
        hostPath:
          path: /var/run/calico
      - name: var-lib-calico
        hostPath:
          path: /var/lib/calico
      - name: xtables-lock
        hostPath:
          path: /run/xtables.lock
          type: FileOrCreate
```

### 4. Security Monitoring
Like having **security guards** patrol every district:

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: security-monitor
  namespace: security
spec:
  selector:
    matchLabels:
      app: security-monitor
  template:
    metadata:
      labels:
        app: security-monitor
    spec:
      serviceAccountName: security-monitor
      containers:
      - name: falco
        image: falcosecurity/falco:0.35.0
        args:
        - /usr/bin/falco
        - --cri=/run/containerd/containerd.sock
        - --k8s-api=https://kubernetes.default.svc.cluster.local
        - --k8s-api-cert=/var/run/secrets/kubernetes.io/serviceaccount/ca.crt
        - --k8s-api-token=/var/run/secrets/kubernetes.io/serviceaccount/token
        securityContext:
          privileged: true
        resources:
          requests:
            memory: "128Mi"
            cpu: "100m"
          limits:
            memory: "256Mi"
            cpu: "200m"
        volumeMounts:
        - mountPath: /host/var/run/docker.sock
          name: docker-socket
        - mountPath: /host/dev
          name: dev-fs
        - mountPath: /host/proc
          name: proc-fs
          readOnly: true
        - mountPath: /host/boot
          name: boot-fs
          readOnly: true
        - mountPath: /host/lib/modules
          name: lib-modules
          readOnly: true
        - mountPath: /host/usr
          name: usr-fs
          readOnly: true
      volumes:
      - name: docker-socket
        hostPath:
          path: /var/run/docker.sock
      - name: dev-fs
        hostPath:
          path: /dev
      - name: proc-fs
        hostPath:
          path: /proc
      - name: boot-fs
        hostPath:
          path: /boot
      - name: lib-modules
        hostPath:
          path: /lib/modules
      - name: usr-fs
        hostPath:
          path: /usr
```

## Advanced DaemonSet Features

### Rolling Updates
Like **gradually upgrading city infrastructure** without disrupting services:

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: log-collector
spec:
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1          # Update one node at a time
      maxSurge: 0               # Don't create extra pods
  selector:
    matchLabels:
      app: log-collector
  template:
    metadata:
      labels:
        app: log-collector
    spec:
      containers:
      - name: log-collector
        image: fluentd:v1.15      # Updated version
        # ... rest of container spec
```

### Tolerations for Special Nodes
Like allowing **emergency services** to operate in restricted areas:

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: system-monitor
spec:
  selector:
    matchLabels:
      app: system-monitor
  template:
    metadata:
      labels:
        app: system-monitor
    spec:
      tolerations:
      # Run on master nodes
      - key: node-role.kubernetes.io/master
        operator: Exists
        effect: NoSchedule
      # Run on tainted nodes
      - key: dedicated
        operator: Equal
        value: gpu
        effect: NoSchedule
      # Run on nodes being drained
      - key: node.kubernetes.io/unschedulable
        operator: Exists
        effect: NoSchedule
      # Handle node problems
      - key: node.kubernetes.io/not-ready
        operator: Exists
        effect: NoExecute
        tolerationSeconds: 300
      containers:
      - name: monitor
        image: system-monitor:latest
```

### Init Containers in DaemonSets
Like **preparation crews** that set up before main services start:

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: network-setup
spec:
  selector:
    matchLabels:
      app: network-setup
  template:
    metadata:
      labels:
        app: network-setup
    spec:
      initContainers:
      - name: setup-network
        image: busybox:latest
        command: ['sh', '-c']
        args:
        - |
          echo "Setting up network configuration..."
          # Configure network interfaces
          ip link set dev eth0 mtu 1500
          # Set up routing rules
          ip route add 10.0.0.0/8 via 192.168.1.1
          echo "Network setup complete"
        securityContext:
          privileged: true
        volumeMounts:
        - name: host-network
          mountPath: /host/etc/network
      containers:
      - name: network-daemon
        image: network-daemon:latest
        securityContext:
          privileged: true
      volumes:
      - name: host-network
        hostPath:
          path: /etc/network
```

## Managing DaemonSets

### Deployment and Updates
```bash
# Create DaemonSet
kubectl apply -f daemonset.yaml

# Check DaemonSet status
kubectl get daemonset log-collector
kubectl describe daemonset log-collector

# Check pods created by DaemonSet
kubectl get pods -l app=log-collector -o wide

# Update DaemonSet (triggers rolling update)
kubectl set image daemonset/log-collector log-collector=fluentd:v1.16

# Check update progress
kubectl rollout status daemonset/log-collector

# View rollout history
kubectl rollout history daemonset/log-collector

# Rollback to previous version
kubectl rollout undo daemonset/log-collector
```

### Scaling and Node Management
```bash
# DaemonSets automatically scale with nodes
# Add node selector to limit deployment
kubectl patch daemonset log-collector -p '{"spec":{"template":{"spec":{"nodeSelector":{"logging":"enabled"}}}}}'

# Label nodes to control DaemonSet placement
kubectl label node worker-1 logging=enabled
kubectl label node worker-2 logging=enabled

# Remove DaemonSet from specific node
kubectl label node worker-3 logging-

# Cordon node (prevents new pods, including DaemonSet pods)
kubectl cordon worker-1

# Drain node (removes DaemonSet pods)
kubectl drain worker-1 --ignore-daemonsets
```

## Troubleshooting DaemonSets

### Common Issues and Solutions

#### Pods Not Scheduling
```bash
# Check DaemonSet status
kubectl describe daemonset my-daemon

# Common causes:
# 1. Node selector doesn't match any nodes
kubectl get nodes --show-labels
kubectl describe daemonset my-daemon | grep -A 5 "Node-Selectors"

# 2. Tolerations missing for tainted nodes
kubectl describe nodes | grep -A 3 Taints
kubectl describe daemonset my-daemon | grep -A 10 Tolerations

# 3. Resource constraints
kubectl describe nodes | grep -A 5 "Allocated resources"
kubectl top nodes
```

#### Pods Failing to Start
```bash
# Check pod logs
kubectl logs -l app=my-daemon --tail=50

# Check pod events
kubectl get events --field-selector involvedObject.kind=Pod

# Common issues:
# 1. Image pull errors
# 2. Volume mount failures (hostPath permissions)
# 3. Security context issues
# 4. Resource limits too low
```

#### Update Issues
```bash
# Check rollout status
kubectl rollout status daemonset/my-daemon

# Check update strategy
kubectl describe daemonset my-daemon | grep -A 5 "Update Strategy"

# Force update if stuck
kubectl patch daemonset my-daemon -p '{"spec":{"template":{"metadata":{"annotations":{"date":"'$(date +'%s')'"}}}}}' 

# Check for pod disruption budgets
kubectl get pdb
```

### Debugging DaemonSet Pods
```bash
# Get shell access to DaemonSet pod
kubectl exec -it $(kubectl get pods -l app=my-daemon -o jsonpath='{.items[0].metadata.name}') -- /bin/bash

# Check host filesystem access
kubectl exec -it daemon-pod -- ls -la /host/var/log

# Check network connectivity
kubectl exec -it daemon-pod -- netstat -tulpn

# Check process information
kubectl exec -it daemon-pod -- ps aux
```

## Best Practices

### 1. Resource Management
```yaml
# Always set resource requests and limits
resources:
  requests:
    memory: "64Mi"
    cpu: "50m"
  limits:
    memory: "128Mi"
    cpu: "100m"
```

### 2. Security
```yaml
# Use least privilege
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  readOnlyRootFilesystem: true

# Only use privileged when absolutely necessary
securityContext:
  privileged: true  # Only for system-level daemons
```

### 3. Monitoring and Logging
```yaml
# Add health checks
livenessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 30
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
```

### 4. Update Strategy
```yaml
# Configure safe rolling updates
updateStrategy:
  type: RollingUpdate
  rollingUpdate:
    maxUnavailable: 1  # Update one node at a time
```

### 5. Node Affinity and Tolerations
```yaml
# Be explicit about node requirements
nodeSelector:
  kubernetes.io/os: linux

# Handle node conditions gracefully
tolerations:
- key: node.kubernetes.io/not-ready
  operator: Exists
  effect: NoExecute
  tolerationSeconds: 300
```

## Monitoring DaemonSets

### Metrics and Alerting
```yaml
# ServiceMonitor for Prometheus
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: daemonset-monitor
spec:
  selector:
    matchLabels:
      app: my-daemon
  endpoints:
  - port: metrics
    interval: 30s
    path: /metrics
```

### Health Checks
```bash
# Check DaemonSet health across cluster
kubectl get daemonset --all-namespaces
kubectl get pods -l app=my-daemon -o wide

# Monitor DaemonSet metrics
kubectl top pods -l app=my-daemon
kubectl describe daemonset my-daemon | grep -A 10 "Pods Status"
```

## Next Steps

After mastering DaemonSet management:
1. **Learn Operators**: Build custom controllers for complex daemon management
2. **Implement Monitoring**: Set up comprehensive daemon monitoring
3. **Practice Security**: Secure daemon communications and access
4. **Study Performance**: Optimize daemon resource usage
5. **Explore Service Mesh**: Integrate daemons with service mesh infrastructure

Remember: Managing cluster daemons is like maintaining essential city services - they need to be reliable, secure, properly monitored, and updated carefully to avoid disrupting the entire system!