# TLS (Transport Layer Security)

Think of TLS in Kubernetes like the **security system for your city** - it ensures all communications are encrypted, identities are verified, and sensitive information is protected as it travels between different parts of your infrastructure.

## Understanding TLS in Kubernetes

### TLS Basics
Like having **secure communication channels** in your city government:

1. **Encryption** - Scrambling messages so only intended recipients can read them
2. **Authentication** - Verifying who you're talking to (like checking ID cards)
3. **Integrity** - Ensuring messages haven't been tampered with during transit
4. **Non-repudiation** - Proving who sent what and when

```bash
# Check TLS certificates in cluster
kubectl get secrets --all-namespaces | grep tls
kubectl describe secret <tls-secret-name>

# Check certificate details
openssl x509 -in certificate.crt -text -noout
```

## Certificate Management

### Manual Certificate Creation
Like **issuing official city ID cards** manually:

```bash
# 1. Create private key
openssl genrsa -out server.key 2048

# 2. Create certificate signing request (CSR)
openssl req -new -key server.key -out server.csr -subj "/CN=myapp.example.com/O=myorg"

# 3. Create self-signed certificate (for testing)
openssl x509 -req -in server.csr -signkey server.key -out server.crt -days 365

# 4. Create Kubernetes TLS secret
kubectl create secret tls myapp-tls --cert=server.crt --key=server.key

# 5. Verify the secret
kubectl describe secret myapp-tls
```

### Certificate Signing Request (CSR) in Kubernetes
Like having an **official certificate authority** in your city:

```yaml
# Create CSR in Kubernetes
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: myapp-csr
spec:
  request: LS0tLS1CRUdJTi... # Base64 encoded CSR
  signerName: kubernetes.io/kube-apiserver-client
  usages:
  - client auth
  - server auth
```

```bash
# Create and approve CSR
kubectl apply -f csr.yaml
kubectl certificate approve myapp-csr

# Get the signed certificate
kubectl get csr myapp-csr -o jsonpath='{.status.certificate}' | base64 -d > myapp.crt

# Create secret with signed certificate
kubectl create secret tls myapp-tls --cert=myapp.crt --key=myapp.key
```

## cert-manager: Automated Certificate Management

### Installing cert-manager
Like setting up an **automated ID card system**:

```bash
# Install cert-manager
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.0/cert-manager.yaml

# Verify installation
kubectl get pods -n cert-manager
kubectl get crd | grep cert-manager
```

### ClusterIssuer Configuration
```yaml
# Let's Encrypt ClusterIssuer (staging)
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-staging
spec:
  acme:
    server: https://acme-staging-v02.api.letsencrypt.org/directory
    email: admin@example.com
    privateKeySecretRef:
      name: letsencrypt-staging
    solvers:
    - http01:
        ingress:
          class: nginx
    - dns01:
        cloudflare:
          email: admin@example.com
          apiTokenSecretRef:
            name: cloudflare-api-token
            key: api-token

---
# Let's Encrypt ClusterIssuer (production)
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: admin@example.com
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
    - http01:
        ingress:
          class: nginx
```

### Self-Signed ClusterIssuer
```yaml
# Self-signed issuer for internal services
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: selfsigned-issuer
spec:
  selfSigned: {}

---
# CA Issuer for internal PKI
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: ca-issuer
spec:
  ca:
    secretName: ca-key-pair
```

## TLS for Ingress

### Basic TLS Ingress
Like securing the **main entrance** to your city services:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: myapp-ingress
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - myapp.example.com
    - api.example.com
    secretName: myapp-tls
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: myapp-service
            port:
              number: 80
  - host: api.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 8080
```

### Advanced TLS Configuration
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: secure-ingress
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    nginx.ingress.kubernetes.io/ssl-protocols: "TLSv1.2 TLSv1.3"
    nginx.ingress.kubernetes.io/ssl-ciphers: "ECDHE-RSA-AES128-GCM-SHA256,ECDHE-RSA-AES256-GCM-SHA384"
    nginx.ingress.kubernetes.io/hsts: "true"
    nginx.ingress.kubernetes.io/hsts-max-age: "31536000"
    nginx.ingress.kubernetes.io/hsts-include-subdomains: "true"
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - secure.example.com
    secretName: secure-tls
  rules:
  - host: secure.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: secure-service
            port:
              number: 443
```

## TLS for Services

### Service-to-Service TLS
Like securing **internal government communications**:

```yaml
# Certificate for internal service
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: internal-service-cert
  namespace: default
spec:
  secretName: internal-service-tls
  issuerRef:
    name: ca-issuer
    kind: ClusterIssuer
  commonName: internal-service.default.svc.cluster.local
  dnsNames:
  - internal-service
  - internal-service.default
  - internal-service.default.svc
  - internal-service.default.svc.cluster.local
```

### Pod with TLS Configuration
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secure-app
spec:
  containers:
  - name: app
    image: nginx:latest
    ports:
    - containerPort: 443
      name: https
    volumeMounts:
    - name: tls-certs
      mountPath: /etc/ssl/certs
      readOnly: true
    - name: nginx-config
      mountPath: /etc/nginx/nginx.conf
      subPath: nginx.conf
  volumes:
  - name: tls-certs
    secret:
      secretName: internal-service-tls
  - name: nginx-config
    configMap:
      name: nginx-tls-config

---
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-tls-config
data:
  nginx.conf: |
    events {}
    http {
        server {
            listen 443 ssl;
            server_name internal-service.default.svc.cluster.local;
            
            ssl_certificate /etc/ssl/certs/tls.crt;
            ssl_certificate_key /etc/ssl/certs/tls.key;
            ssl_protocols TLSv1.2 TLSv1.3;
            ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384;
            
            location / {
                return 200 "Secure Hello World\n";
                add_header Content-Type text/plain;
            }
        }
    }
```

## Mutual TLS (mTLS)

### Client Certificate Authentication
Like requiring **both parties to show ID** in secure communications:

```yaml
# Client certificate
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: client-cert
spec:
  secretName: client-tls
  issuerRef:
    name: ca-issuer
    kind: ClusterIssuer
  commonName: client
  usages:
  - client auth

---
# Server with client certificate verification
apiVersion: v1
kind: ConfigMap
metadata:
  name: mtls-nginx-config
data:
  nginx.conf: |
    events {}
    http {
        server {
            listen 443 ssl;
            server_name secure-service.default.svc.cluster.local;
            
            # Server certificates
            ssl_certificate /etc/ssl/server/tls.crt;
            ssl_certificate_key /etc/ssl/server/tls.key;
            
            # Client certificate verification
            ssl_client_certificate /etc/ssl/ca/ca.crt;
            ssl_verify_client on;
            
            ssl_protocols TLSv1.2 TLSv1.3;
            
            location / {
                # Pass client certificate info to backend
                proxy_set_header X-SSL-Client-Cert $ssl_client_cert;
                proxy_set_header X-SSL-Client-DN $ssl_client_s_dn;
                proxy_pass http://backend-service;
            }
        }
    }
```

### Service Mesh mTLS (Istio)
```yaml
# Enable automatic mTLS in Istio
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: production
spec:
  mtls:
    mode: STRICT

---
# Destination rule for mTLS
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: mtls-destination
spec:
  host: "*.production.svc.cluster.local"
  trafficPolicy:
    tls:
      mode: ISTIO_MUTUAL
```

## Certificate Lifecycle Management

### Automatic Certificate Renewal
Like having **automatic ID card renewal**:

```yaml
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: auto-renew-cert
spec:
  secretName: auto-renew-tls
  issuerRef:
    name: letsencrypt-prod
    kind: ClusterIssuer
  commonName: app.example.com
  dnsNames:
  - app.example.com
  - www.app.example.com
  duration: 2160h # 90 days
  renewBefore: 360h # 15 days before expiry
```

### Certificate Monitoring
```bash
# Check certificate status
kubectl get certificates
kubectl describe certificate myapp-cert

# Check certificate expiry
kubectl get secret myapp-tls -o jsonpath='{.data.tls\.crt}' | base64 -d | openssl x509 -noout -dates

# Monitor certificate events
kubectl get events --field-selector involvedObject.kind=Certificate
```

### Certificate Rotation
```yaml
# Force certificate renewal
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: force-renew-cert
  annotations:
    cert-manager.io/issue-temporary-certificate: "true"
spec:
  secretName: force-renew-tls
  issuerRef:
    name: letsencrypt-prod
    kind: ClusterIssuer
  commonName: app.example.com
```

## TLS Best Practices

### Security Configuration
```yaml
# Strong TLS configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: secure-tls-config
data:
  tls.conf: |
    # Use only strong protocols
    ssl_protocols TLSv1.2 TLSv1.3;
    
    # Strong cipher suites
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;
    
    # Security headers
    add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload";
    add_header X-Content-Type-Options nosniff;
    add_header X-Frame-Options DENY;
    add_header X-XSS-Protection "1; mode=block";
    
    # OCSP stapling
    ssl_stapling on;
    ssl_stapling_verify on;
```

### Certificate Storage Security
```yaml
# Secure certificate storage
apiVersion: v1
kind: Secret
metadata:
  name: secure-tls-secret
  annotations:
    # Restrict access
    kubernetes.io/service-account.name: "tls-service-account"
type: kubernetes.io/tls
data:
  tls.crt: LS0tLS1CRUdJTi... # Base64 encoded certificate
  tls.key: LS0tLS1CRUdJTi... # Base64 encoded private key
```

### RBAC for Certificate Management
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: cert-manager
rules:
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
- apiGroups: ["cert-manager.io"]
  resources: ["certificates", "certificaterequests"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]

---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: cert-manager-binding
subjects:
- kind: ServiceAccount
  name: cert-manager
  namespace: cert-manager
roleRef:
  kind: Role
  name: cert-manager
  apiGroup: rbac.authorization.k8s.io
```

## Troubleshooting TLS

### Certificate Issues
```bash
# Check certificate details
openssl x509 -in certificate.crt -text -noout

# Verify certificate chain
openssl verify -CAfile ca.crt certificate.crt

# Check certificate expiry
openssl x509 -in certificate.crt -noout -dates

# Test TLS connection
openssl s_client -connect myapp.example.com:443 -servername myapp.example.com

# Check certificate in Kubernetes
kubectl get secret myapp-tls -o yaml
kubectl describe certificate myapp-cert
```

### cert-manager Troubleshooting
```bash
# Check cert-manager logs
kubectl logs -n cert-manager deployment/cert-manager

# Check certificate request status
kubectl get certificaterequests
kubectl describe certificaterequest myapp-cert-xyz

# Check ACME challenge status
kubectl get challenges
kubectl describe challenge myapp-cert-xyz-123

# Check issuer status
kubectl describe clusterissuer letsencrypt-prod
```

### Common TLS Problems

#### Certificate Not Trusted
```bash
# Problem: Certificate not trusted by clients
# Solution: Check certificate chain and CA

# Verify certificate chain
curl -I https://myapp.example.com
openssl s_client -connect myapp.example.com:443 -showcerts

# Check if intermediate certificates are included
kubectl get secret myapp-tls -o jsonpath='{.data.tls\.crt}' | base64 -d | openssl certs -text
```

#### ACME Challenge Failures
```bash
# Problem: Let's Encrypt challenges failing
# Check ingress controller and DNS

# Verify HTTP-01 challenge
curl http://myapp.example.com/.well-known/acme-challenge/test

# Check DNS-01 challenge
dig TXT _acme-challenge.myapp.example.com

# Check challenge pods
kubectl get pods -l acme.cert-manager.io/http01-solver=true
```

#### Certificate Renewal Issues
```bash
# Problem: Certificates not renewing automatically
# Check cert-manager configuration and permissions

# Force certificate renewal
kubectl annotate certificate myapp-cert cert-manager.io/issue-temporary-certificate="true"

# Check renewal logs
kubectl logs -n cert-manager deployment/cert-manager | grep myapp-cert
```

## Advanced TLS Scenarios

### Multi-Domain Certificates
```yaml
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: multi-domain-cert
spec:
  secretName: multi-domain-tls
  issuerRef:
    name: letsencrypt-prod
    kind: ClusterIssuer
  commonName: example.com
  dnsNames:
  - example.com
  - www.example.com
  - api.example.com
  - admin.example.com
  - "*.staging.example.com"  # Wildcard certificate
```

### External Certificate Integration
```yaml
# Use external certificate (e.g., from AWS ACM)
apiVersion: v1
kind: Secret
metadata:
  name: external-cert
  annotations:
    external-dns.alpha.kubernetes.io/hostname: myapp.example.com
type: kubernetes.io/tls
data:
  tls.crt: # Certificate from external CA
  tls.key: # Private key (if available)
```

### Certificate Backup and Recovery
```bash
# Backup certificates
kubectl get secrets -o yaml | grep -A 10 -B 5 "type: kubernetes.io/tls" > tls-backup.yaml

# Restore certificates
kubectl apply -f tls-backup.yaml

# Export certificate for external use
kubectl get secret myapp-tls -o jsonpath='{.data.tls\.crt}' | base64 -d > myapp.crt
kubectl get secret myapp-tls -o jsonpath='{.data.tls\.key}' | base64 -d > myapp.key
```

## Next Steps

After mastering TLS in Kubernetes:
1. **Implement Service Mesh**: Istio/Linkerd for automatic mTLS
2. **Set up PKI**: Internal certificate authority management
3. **Learn Security Scanning**: Certificate vulnerability assessment
4. **Practice Compliance**: Meet regulatory requirements (PCI DSS, HIPAA)
5. **Automate Security**: Policy-as-code for certificate management

Remember: TLS security is like having a comprehensive security system for your city - it requires proper planning, regular maintenance, monitoring for issues, and staying updated with security best practices!