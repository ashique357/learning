# Monitor, Debug and Troubleshoot

Think of monitoring and troubleshooting Kubernetes like being a **city manager** who needs to keep track of all services, identify problems quickly, and fix issues before they affect citizens (users).

## Understanding Kubernetes Observability

### The Three Pillars of Observability
Like having **different types of city monitoring systems**:

1. **Metrics** - Like traffic counters and utility meters
2. **Logs** - Like security camera recordings and incident reports
3. **Traces** - Like following a delivery truck's complete route through the city

```bash
# Quick health check commands (like city dashboard)
kubectl get nodes                    # Check infrastructure health
kubectl get pods --all-namespaces   # Check all services
kubectl top nodes                    # Resource usage overview
kubectl top pods                     # Application resource usage
```

## Basic Monitoring Commands

### Checking Cluster Health
Like doing **daily city inspections**:

```bash
# Overall cluster status
kubectl cluster-info
kubectl get componentstatuses

# Node health and resources
kubectl get nodes -o wide
kubectl describe node <node-name>
kubectl top nodes

# System pods health
kubectl get pods -n kube-system
kubectl get events --sort-by=.metadata.creationTimestamp
```

### Monitoring Applications
Like checking on **individual businesses** in your city:

```bash
# Check application status
kubectl get pods -l app=web-app
kubectl get deployments
kubectl get services

# Resource usage
kubectl top pods -l app=web-app
kubectl top pods --containers        # Per-container metrics

# Real-time monitoring
kubectl get pods --watch             # Live updates
kubectl get events --watch           # Live events
```

## Debugging Techniques

### Pod Troubleshooting
Like investigating **business problems** in your city:

```bash
# 1. Check pod status and events
kubectl get pods
kubectl describe pod <pod-name>

# 2. Check logs
kubectl logs <pod-name>                    # Current logs
kubectl logs <pod-name> --previous         # Previous container logs
kubectl logs <pod-name> -c <container>     # Specific container
kubectl logs <pod-name> --tail=50          # Last 50 lines
kubectl logs <pod-name> --since=1h         # Last hour

# 3. Interactive debugging
kubectl exec -it <pod-name> -- /bin/bash   # Get shell access
kubectl exec <pod-name> -- ps aux          # Run single command
```

### Common Pod States and Solutions

#### Pending Pods
Like **construction permits stuck in approval**:

```bash
# Check why pod is pending
kubectl describe pod <pod-name>

# Common causes and solutions:
# 1. Insufficient resources
kubectl top nodes
kubectl describe nodes

# 2. Node selector issues
kubectl get nodes --show-labels
kubectl get pod <pod-name> -o yaml | grep nodeSelector

# 3. Taints and tolerations
kubectl describe nodes | grep -i taint
```

#### ImagePullBackOff
Like **supply delivery problems**:

```bash
# Check image pull issues
kubectl describe pod <pod-name>

# Common solutions:
# 1. Fix image name/tag
kubectl get pod <pod-name> -o yaml | grep image

# 2. Add image pull secrets
kubectl create secret docker-registry regcred \
  --docker-server=<registry> \
  --docker-username=<username> \
  --docker-password=<password>

# 3. Check registry connectivity
kubectl run debug --image=busybox --rm -it -- nslookup <registry-url>
```

#### CrashLoopBackOff
Like **businesses that keep failing to open**:

```bash
# Investigate crash causes
kubectl logs <pod-name> --previous
kubectl describe pod <pod-name>

# Common causes:
# 1. Application errors - check logs
# 2. Resource limits too low
# 3. Missing configuration
# 4. Failed health checks

# Debug with different image
kubectl run debug-pod --image=busybox --rm -it -- sh
```

#### OOMKilled (Out of Memory)
Like **businesses running out of space**:

```bash
# Check memory usage and limits
kubectl top pod <pod-name> --containers
kubectl describe pod <pod-name> | grep -i memory

# Solutions:
# 1. Increase memory limits
# 2. Optimize application memory usage
# 3. Check for memory leaks
```

## Advanced Debugging

### Network Troubleshooting
Like investigating **communication problems** in the city:

```bash
# 1. Check service connectivity
kubectl get services
kubectl describe service <service-name>

# 2. Test DNS resolution
kubectl run debug --image=busybox --rm -it -- nslookup <service-name>
kubectl run debug --image=busybox --rm -it -- nslookup <service-name>.<namespace>.svc.cluster.local

# 3. Test network connectivity
kubectl run debug --image=nicolaka/netshoot --rm -it -- bash
# Inside the debug pod:
# ping <service-ip>
# telnet <service-ip> <port>
# curl http://<service-name>:<port>

# 4. Check endpoints
kubectl get endpoints <service-name>
kubectl describe endpoints <service-name>
```

### Storage Issues
Like investigating **warehouse and storage problems**:

```bash
# Check persistent volumes
kubectl get pv
kubectl get pvc
kubectl describe pvc <pvc-name>

# Check storage class
kubectl get storageclass
kubectl describe storageclass <class-name>

# Debug volume mounts
kubectl describe pod <pod-name> | grep -A 10 Mounts
kubectl exec <pod-name> -- df -h
kubectl exec <pod-name> -- ls -la /path/to/mount
```

### Configuration Issues
Like checking **business licenses and permits**:

```bash
# Check ConfigMaps and Secrets
kubectl get configmaps
kubectl get secrets
kubectl describe configmap <config-name>
kubectl describe secret <secret-name>

# Verify environment variables
kubectl exec <pod-name> -- env
kubectl get pod <pod-name> -o yaml | grep -A 20 env

# Check volume mounts for config
kubectl exec <pod-name> -- ls -la /etc/config
kubectl exec <pod-name> -- cat /etc/config/app.properties
```

## Monitoring Tools and Techniques

### Built-in Monitoring
Like having **basic city monitoring systems**:

```bash
# Resource usage monitoring
kubectl top nodes
kubectl top pods --all-namespaces
kubectl top pods --containers

# Event monitoring
kubectl get events --sort-by=.metadata.creationTimestamp
kubectl get events --field-selector type=Warning

# Continuous monitoring
watch kubectl get pods
watch kubectl top nodes
```

### Using Metrics Server
Like installing **advanced monitoring equipment**:

```bash
# Install metrics server (if not present)
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

# Verify metrics server
kubectl get deployment metrics-server -n kube-system
kubectl top nodes
kubectl top pods
```

### Custom Monitoring Setup
Like setting up **specialized monitoring systems**:

```yaml
# Prometheus monitoring example
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus-config
data:
  prometheus.yml: |
    global:
      scrape_interval: 15s
    scrape_configs:
    - job_name: 'kubernetes-pods'
      kubernetes_sd_configs:
      - role: pod
      relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: prometheus
spec:
  replicas: 1
  selector:
    matchLabels:
      app: prometheus
  template:
    metadata:
      labels:
        app: prometheus
    spec:
      containers:
      - name: prometheus
        image: prom/prometheus:latest
        ports:
        - containerPort: 9090
        volumeMounts:
        - name: config
          mountPath: /etc/prometheus
      volumes:
      - name: config
        configMap:
          name: prometheus-config
```

## Logging and Log Analysis

### Container Logs
Like reading **business activity reports**:

```bash
# Basic log viewing
kubectl logs <pod-name>
kubectl logs <pod-name> -c <container-name>

# Advanced log options
kubectl logs <pod-name> --tail=100           # Last 100 lines
kubectl logs <pod-name> --since=2h           # Last 2 hours
kubectl logs <pod-name> --since-time=2023-01-01T10:00:00Z
kubectl logs <pod-name> -f                   # Follow logs (tail -f)
kubectl logs <pod-name> --previous           # Previous container instance

# Multiple pods
kubectl logs -l app=web-app                  # All pods with label
kubectl logs deployment/web-app              # All pods in deployment
```

### Centralized Logging
Like having a **city-wide incident reporting system**:

```yaml
# Fluentd DaemonSet for log collection
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd
  namespace: kube-system
spec:
  selector:
    matchLabels:
      name: fluentd
  template:
    metadata:
      labels:
        name: fluentd
    spec:
      containers:
      - name: fluentd
        image: fluent/fluentd-kubernetes-daemonset:v1-debian-elasticsearch
        env:
        - name: FLUENT_ELASTICSEARCH_HOST
          value: "elasticsearch.logging.svc.cluster.local"
        - name: FLUENT_ELASTICSEARCH_PORT
          value: "9200"
        volumeMounts:
        - name: varlog
          mountPath: /var/log
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
```

## Performance Troubleshooting

### Resource Analysis
Like analyzing **city resource consumption**:

```bash
# CPU and Memory analysis
kubectl top nodes --sort-by=cpu
kubectl top pods --sort-by=cpu
kubectl top pods --sort-by=memory

# Detailed resource usage
kubectl describe node <node-name> | grep -A 5 "Allocated resources"
kubectl get pods -o custom-columns=NAME:.metadata.name,CPU-REQ:.spec.containers[*].resources.requests.cpu,MEM-REQ:.spec.containers[*].resources.requests.memory

# Resource quotas and limits
kubectl get resourcequota --all-namespaces
kubectl describe resourcequota <quota-name>
```

### Application Performance
Like monitoring **business performance metrics**:

```bash
# Check application metrics endpoints
kubectl port-forward pod/<pod-name> 8080:8080
curl http://localhost:8080/metrics

# Load testing
kubectl run load-test --image=busybox --rm -it -- sh
# Inside pod: while true; do wget -q -O- http://service-name; done

# Database connection testing
kubectl exec -it <db-pod> -- psql -U user -d database -c "SELECT version();"
```

## Troubleshooting Workflows

### Systematic Debugging Approach
Like following a **standard investigation procedure**:

```bash
# 1. Identify the problem scope
kubectl get pods --all-namespaces | grep -v Running
kubectl get events --sort-by=.metadata.creationTimestamp | tail -20

# 2. Gather information
kubectl describe pod <problematic-pod>
kubectl logs <problematic-pod> --tail=100

# 3. Check dependencies
kubectl get services
kubectl get configmaps
kubectl get secrets
kubectl get pvc

# 4. Test connectivity
kubectl run debug --image=busybox --rm -it -- sh

# 5. Check resources
kubectl top nodes
kubectl top pods
kubectl describe nodes
```

### Emergency Response
Like handling **city emergencies**:

```bash
# Quick cluster health check
kubectl get nodes
kubectl get pods --all-namespaces | grep -v Running

# Emergency pod restart
kubectl delete pod <pod-name>  # Let deployment recreate it
kubectl rollout restart deployment/<deployment-name>

# Scale down problematic application
kubectl scale deployment <deployment-name> --replicas=0
kubectl scale deployment <deployment-name> --replicas=3

# Emergency resource cleanup
kubectl delete pods --field-selector=status.phase=Failed
kubectl delete pods --field-selector=status.phase=Succeeded
```

## Monitoring Best Practices

### 1. Proactive Monitoring
```yaml
# Set up proper health checks
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

### 2. Resource Monitoring
```yaml
# Always set resource requests and limits
resources:
  requests:
    memory: "64Mi"
    cpu: "250m"
  limits:
    memory: "128Mi"
    cpu: "500m"
```

### 3. Alerting Setup
```yaml
# Example alert rules (Prometheus)
groups:
- name: kubernetes-alerts
  rules:
  - alert: PodCrashLooping
    expr: rate(kube_pod_container_status_restarts_total[15m]) > 0
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "Pod {{ $labels.pod }} is crash looping"
      
  - alert: NodeNotReady
    expr: kube_node_status_condition{condition="Ready",status="true"} == 0
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: "Node {{ $labels.node }} is not ready"
```

### 4. Log Management
```bash
# Structured logging in applications
{
  "timestamp": "2023-01-01T10:00:00Z",
  "level": "ERROR",
  "message": "Database connection failed",
  "service": "web-app",
  "pod": "web-app-123",
  "namespace": "production"
}
```

## Troubleshooting Tools

### Essential Debug Images
```bash
# Network debugging
kubectl run netshoot --image=nicolaka/netshoot --rm -it -- bash

# General purpose debugging
kubectl run debug --image=busybox --rm -it -- sh

# Advanced debugging with tools
kubectl run debug-tools --image=praqma/network-multitool --rm -it -- bash
```

### Useful kubectl Plugins
```bash
# Install krew (kubectl plugin manager)
curl -fsSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/krew.tar.gz"

# Useful plugins
kubectl krew install debug      # Enhanced debugging
kubectl krew install tail       # Tail logs from multiple pods
kubectl krew install tree       # Show resource relationships
kubectl krew install top        # Enhanced resource usage
```

## Next Steps

After mastering monitoring and troubleshooting:
1. **Set up comprehensive monitoring**: Prometheus, Grafana, AlertManager
2. **Implement centralized logging**: ELK stack or similar
3. **Learn distributed tracing**: Jaeger or Zipkin
4. **Practice chaos engineering**: Intentionally break things to learn
5. **Automate incident response**: Create runbooks and automation

Remember: Good monitoring and troubleshooting is like having a well-organized emergency response system - it requires preparation, the right tools, systematic approaches, and continuous improvement based on lessons learned!