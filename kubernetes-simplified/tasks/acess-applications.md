# Access Applications in Cluster

Think of accessing applications in Kubernetes like **connecting to businesses** in a city. You need different types of connections - some for internal communication between businesses, others for customers from outside the city to visit.

## Understanding Kubernetes Networking

### Network Layers
Like different **communication systems** in a city:

1. **Pod Network** - Internal apartment building communication
2. **Service Network** - Business-to-business communication
3. **Ingress Network** - Public access from outside the city
4. **External Access** - Highways connecting to other cities

```bash
# Quick network overview
kubectl get pods -o wide          # See pod IPs
kubectl get services              # See service IPs  
kubectl get ingress               # See external access points
kubectl get nodes -o wide         # See node IPs
```

## Services: Internal Communication

### ClusterIP Service
Like an **internal business directory** - only accessible within the city:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-app-service
spec:
  type: ClusterIP                 # Default type (internal only)
  selector:
    app: web-app                  # Which pods to connect to
  ports:
  - name: http
    port: 80                      # Service port (what others connect to)
    targetPort: 8080              # Pod port (where app actually listens)
    protocol: TCP
```

```bash
# Create and test ClusterIP service
kubectl apply -f web-app-service.yaml
kubectl get service web-app-service

# Test internal connectivity
kubectl run debug --image=busybox --rm -it -- sh
# Inside debug pod:
# wget -qO- http://web-app-service
# nslookup web-app-service
```

### NodePort Service
Like having **designated entry points** at city gates:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-app-nodeport
spec:
  type: NodePort
  selector:
    app: web-app
  ports:
  - name: http
    port: 80                      # Service port
    targetPort: 8080              # Pod port
    nodePort: 30080               # External port (30000-32767)
    protocol: TCP
```

```bash
# Access via NodePort
kubectl get nodes -o wide        # Get node external IPs
curl http://<node-ip>:30080      # Access from outside cluster

# Let Kubernetes assign nodePort automatically
kubectl expose deployment web-app --type=NodePort --port=80 --target-port=8080
```

### LoadBalancer Service
Like having a **professional reception service** that distributes visitors:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-app-loadbalancer
spec:
  type: LoadBalancer
  selector:
    app: web-app
  ports:
  - name: http
    port: 80
    targetPort: 8080
    protocol: TCP
```

```bash
# Create LoadBalancer service
kubectl apply -f web-app-loadbalancer.yaml

# Check external IP (may take a few minutes)
kubectl get service web-app-loadbalancer --watch

# Access via external IP
curl http://<external-ip>
```

### ExternalName Service
Like having a **forwarding address** that redirects to external services:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: external-database
spec:
  type: ExternalName
  externalName: database.example.com
  ports:
  - port: 5432
```

```bash
# Use external service
kubectl run app --image=postgres:13 --rm -it -- psql -h external-database -p 5432
```

## Port Forwarding: Direct Access

### Local Port Forwarding
Like having a **private tunnel** directly to a specific business:

```bash
# Forward local port to pod
kubectl port-forward pod/web-app-pod 8080:80
# Now access: http://localhost:8080

# Forward to service (more reliable)
kubectl port-forward service/web-app-service 8080:80

# Forward to deployment
kubectl port-forward deployment/web-app 8080:80

# Background forwarding
kubectl port-forward service/web-app-service 8080:80 &

# Multiple ports
kubectl port-forward pod/web-app-pod 8080:80 9090:9090
```

### Advanced Port Forwarding
```bash
# Forward to specific container in multi-container pod
kubectl port-forward pod/web-app-pod 8080:80

# Forward with specific local IP
kubectl port-forward --address 0.0.0.0 service/web-app-service 8080:80

# Forward random local port
kubectl port-forward service/web-app-service :80
```

## Ingress: External Access Management

### Understanding Ingress
Like having a **smart city gateway** that routes visitors to the right businesses:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web-app-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
  - host: myapp.example.com           # Domain name
    http:
      paths:
      - path: /                       # URL path
        pathType: Prefix
        backend:
          service:
            name: web-app-service     # Which service to route to
            port:
              number: 80
```

### Advanced Ingress Configuration
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: advanced-ingress
  annotations:
    # SSL/TLS configuration
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
    # Rate limiting
    nginx.ingress.kubernetes.io/rate-limit: "100"
    # Authentication
    nginx.ingress.kubernetes.io/auth-type: basic
    nginx.ingress.kubernetes.io/auth-secret: basic-auth
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - myapp.example.com
    secretName: myapp-tls
  rules:
  - host: myapp.example.com
    http:
      paths:
      # Frontend application
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend-service
            port:
              number: 80
      # API backend
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 8080
      # Static files
      - path: /static
        pathType: Prefix
        backend:
          service:
            name: static-service
            port:
              number: 80
```

### Installing Ingress Controller
```bash
# Install NGINX Ingress Controller
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.1/deploy/static/provider/cloud/deploy.yaml

# Verify installation
kubectl get pods -n ingress-nginx
kubectl get service -n ingress-nginx

# Install Traefik (alternative)
helm repo add traefik https://helm.traefik.io/traefik
helm install traefik traefik/traefik
```

## DNS and Service Discovery

### Internal DNS
Like having a **city phone book** that automatically updates:

```bash
# Service DNS format: <service-name>.<namespace>.svc.cluster.local

# Test DNS resolution
kubectl run debug --image=busybox --rm -it -- sh
# Inside pod:
# nslookup web-app-service
# nslookup web-app-service.default.svc.cluster.local
# nslookup kubernetes.default.svc.cluster.local

# Check DNS configuration
kubectl get configmap coredns -n kube-system -o yaml
```

### Custom DNS Configuration
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: custom-dns-pod
spec:
  dnsPolicy: "None"
  dnsConfig:
    nameservers:
    - 8.8.8.8
    - 8.8.4.4
    searches:
    - example.com
    options:
    - name: ndots
      value: "2"
  containers:
  - name: app
    image: busybox
    command: ["sleep", "3600"]
```

## Network Policies: Access Control

### Basic Network Policy
Like setting **security rules** for business communications:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: web-app-netpol
spec:
  podSelector:
    matchLabels:
      app: web-app
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 8080
  egress:
  - to:
    - podSelector:
        matchLabels:
          app: database
    ports:
    - protocol: TCP
      port: 5432
```

### Advanced Network Policies
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: advanced-netpol
spec:
  podSelector:
    matchLabels:
      tier: backend
  policyTypes:
  - Ingress
  - Egress
  ingress:
  # Allow from same namespace
  - from:
    - namespaceSelector:
        matchLabels:
          name: production
  # Allow from specific pods
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 8080
  egress:
  # Allow DNS
  - to: []
    ports:
    - protocol: UDP
      port: 53
  # Allow external HTTPS
  - to: []
    ports:
    - protocol: TCP
      port: 443
```

## Service Mesh: Advanced Networking

### Istio Service Mesh
Like having an **intelligent traffic management system** for the entire city:

```yaml
# Install Istio
# curl -L https://istio.io/downloadIstio | sh -
# istioctl install --set values.defaultRevision=default

# Enable sidecar injection
apiVersion: v1
kind: Namespace
metadata:
  name: production
  labels:
    istio-injection: enabled

---
# Virtual Service for traffic routing
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: web-app-vs
spec:
  hosts:
  - web-app-service
  http:
  - match:
    - headers:
        version:
          exact: v2
    route:
    - destination:
        host: web-app-service
        subset: v2
  - route:
    - destination:
        host: web-app-service
        subset: v1
      weight: 90
    - destination:
        host: web-app-service
        subset: v2
      weight: 10

---
# Destination Rule for load balancing
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: web-app-dr
spec:
  host: web-app-service
  trafficPolicy:
    loadBalancer:
      simple: LEAST_CONN
  subsets:
  - name: v1
    labels:
      version: v1
  - name: v2
    labels:
      version: v2
```

## Practical Access Scenarios

### Scenario 1: Development Environment
```bash
# Quick local access for development
kubectl port-forward service/web-app 8080:80 &
kubectl port-forward service/database 5432:5432 &

# Access applications
curl http://localhost:8080
psql -h localhost -p 5432 -U user database
```

### Scenario 2: Staging Environment
```yaml
# NodePort for team access
apiVersion: v1
kind: Service
metadata:
  name: staging-web-app
spec:
  type: NodePort
  selector:
    app: web-app
    environment: staging
  ports:
  - port: 80
    targetPort: 8080
    nodePort: 30080
```

### Scenario 3: Production Environment
```yaml
# LoadBalancer with Ingress
apiVersion: v1
kind: Service
metadata:
  name: prod-web-app
spec:
  type: ClusterIP
  selector:
    app: web-app
    environment: production
  ports:
  - port: 80
    targetPort: 8080

---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: prod-ingress
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
    nginx.ingress.kubernetes.io/rate-limit: "1000"
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - app.company.com
    secretName: app-tls
  rules:
  - host: app.company.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: prod-web-app
            port:
              number: 80
```

## Troubleshooting Access Issues

### Service Connectivity Problems
```bash
# 1. Check service exists and has endpoints
kubectl get service web-app-service
kubectl get endpoints web-app-service

# 2. Verify pod labels match service selector
kubectl get pods --show-labels
kubectl describe service web-app-service

# 3. Test internal connectivity
kubectl run debug --image=busybox --rm -it -- sh
# wget -qO- http://web-app-service
# telnet web-app-service 80

# 4. Check DNS resolution
# nslookup web-app-service
# nslookup web-app-service.default.svc.cluster.local
```

### Ingress Issues
```bash
# 1. Check ingress controller is running
kubectl get pods -n ingress-nginx

# 2. Verify ingress configuration
kubectl describe ingress web-app-ingress

# 3. Check ingress controller logs
kubectl logs -n ingress-nginx deployment/ingress-nginx-controller

# 4. Test backend service
kubectl port-forward service/web-app-service 8080:80
curl http://localhost:8080
```

### Network Policy Debugging
```bash
# 1. Check if network policies are applied
kubectl get networkpolicy

# 2. Describe network policy
kubectl describe networkpolicy web-app-netpol

# 3. Test connectivity with and without policies
kubectl run test-pod --image=busybox --rm -it -- sh
# wget -qO- http://web-app-service

# 4. Check CNI plugin logs (varies by plugin)
kubectl logs -n kube-system -l k8s-app=calico-node
```

## Security Best Practices

### 1. Principle of Least Privilege
```yaml
# Only allow necessary connections
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all-default
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
```

### 2. TLS Everywhere
```yaml
# Use TLS for all external connections
spec:
  tls:
  - hosts:
    - myapp.example.com
    secretName: myapp-tls
```

### 3. Authentication and Authorization
```yaml
# Add authentication to ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/auth-type: basic
    nginx.ingress.kubernetes.io/auth-secret: basic-auth
```

### 4. Rate Limiting
```yaml
# Protect against abuse
metadata:
  annotations:
    nginx.ingress.kubernetes.io/rate-limit: "100"
    nginx.ingress.kubernetes.io/rate-limit-window: "1m"
```

## Next Steps

After mastering application access:
1. **Learn advanced networking**: Service mesh, CNI plugins
2. **Implement security**: mTLS, authentication, authorization
3. **Set up monitoring**: Network metrics, tracing
4. **Practice troubleshooting**: Network debugging tools
5. **Explore multi-cluster**: Cross-cluster communication

Remember: Good application access is like having a well-designed city transportation system - it should be secure, efficient, reliable, and easy to navigate for both residents and visitors!