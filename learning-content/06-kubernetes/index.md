# Kubernetes

Master container orchestration, Kubernetes architecture, and cloud-native application deployment.

## 📑 Topics

### Kubernetes Fundamentals
1. What is Kubernetes (Container Orchestration, Why K8s)
2. Kubernetes Architecture
    - Control Plane (API Server, etcd, Scheduler, Controller Manager)
    - Node Components (kubelet, kube-proxy, Container Runtime)
3. Control Plane Components Deep-Dive
    - API Server (RESTful, Authentication, Admission Controllers)
    - etcd (Distributed Key-Value Store, Raft Consensus)
    - Scheduler (Filtering, Scoring, Binding)
    - Controller Manager (Reconciliation Loop, Desired vs Actual State)
4. Node Components Deep-Dive (kubelet, kube-proxy iptables/IPVS)
5. kubectl Basics (get, describe, apply, delete, logs, exec, port-forward)

### Core Concepts
6. Pods (Smallest Unit, Multi-Container Pods, Pod Lifecycle)
7. ReplicaSets (Desired State, Selector, Scaling)
8. Deployments (Rolling Updates, Rollback, Strategy)
9. Services (Stable Networking, Service Discovery, Endpoints)
10. Namespaces (Isolation, Resource Scoping, Default Namespaces)
11. Labels and Selectors (Equality-Based, Set-Based, Matching)
12. Annotations (Metadata, Non-Identifying Information)

### Workload Resources
13. StatefulSets (Ordered Deployment, Stable Network Identity, Persistent Storage)
14. DaemonSets (One Pod per Node, Use Cases: Logging, Monitoring)
15. Jobs (Run-to-Completion, Parallelism, Backoff Limit)
16. CronJobs (Scheduled Jobs, Cron Syntax, Concurrency Policy)
17. Init Containers (Sequential Execution, Dependency Setup)
18. Sidecar Containers (Logging, Proxy, Config Reload)

### Networking
19. Kubernetes Networking Model (Pod-to-Pod, Pod-to-Service, External)
    - Every Pod Gets Its Own IP
    - CNI Plugins (Calico, Flannel, Cilium, Weave)
20. Service Types
    - ClusterIP (Internal Only)
    - NodePort (External via Node Port)
    - LoadBalancer (Cloud Provider LB)
    - ExternalName (DNS CNAME)
21. Ingress (HTTP/HTTPS Routing, Path-Based, Host-Based)
22. Ingress Controllers (Nginx, Traefik, ALB Ingress Controller)
23. Network Policies (Ingress/Egress Rules, Pod Selector, Namespace Selector)
24. DNS in Kubernetes (CoreDNS, Service Discovery, Pod DNS)

### Storage
25. Volumes (emptyDir, hostPath, configMap, secret, PVC)
26. Persistent Volumes (PV) (Lifecycle, Reclaim Policy, Access Modes)
27. Persistent Volume Claims (PVC) (Binding, Dynamic Provisioning)
28. Storage Classes (Provisioner, Parameters, Default Class)
29. StatefulSet Storage (volumeClaimTemplates, Stable Storage)

### Configuration
30. ConfigMaps (Key-Value, File-Based, Environment Variables, Volume Mount)
31. Secrets (Opaque, TLS, Docker Registry, Base64 Encoding)
32. Environment Variables (Static, ConfigMap Ref, Secret Ref, Field Ref)
33. Resource Requests and Limits (CPU, Memory, QoS Classes: Guaranteed, Burstable, BestEffort)
34. LimitRanges (Default Limits, Min/Max per Container)
35. ResourceQuotas (Namespace-Level Limits, CPU, Memory, Object Count)

### Scheduling
36. Scheduling Basics (Predicates, Priorities, Binding)
37. Node Selectors (Simple Label Matching)
38. Node Affinity (Required, Preferred, Operators)
39. Pod Affinity and Anti-Affinity (Co-Location, Spread, Topology Key)
40. Taints and Tolerations (NoSchedule, PreferNoSchedule, NoExecute)
41. Priority Classes (Preemption, System Critical Pods)

### Scaling
42. Manual Scaling (kubectl scale, Replicas)
43. Horizontal Pod Autoscaler (HPA) (CPU, Memory, Custom Metrics)
44. Vertical Pod Autoscaler (VPA) (Right-Sizing, Recommendations)
45. Cluster Autoscaler (Node Scaling, Scale-Up/Down, Cloud Integration)
46. KEDA (Event-Driven Autoscaling, Scalers, ScaledObject)

### Security
47. RBAC (Role-Based Access Control)
    - Role, ClusterRole, RoleBinding, ClusterRoleBinding
    - Service Account Permissions
48. Service Accounts (Default, Custom, Token Mounting)
49. Pod Security Standards (Privileged, Baseline, Restricted)
50. Network Policies (Default Deny, Allow Specific Traffic)
51. Secrets Management (External Secrets Operator, Sealed Secrets, Vault Integration)

### Observability
52. Logging (Container Logs, Sidecar Logging, EFK/ELK Stack)
53. Monitoring with Prometheus (ServiceMonitor, PodMonitor, Prometheus Operator)
54. Metrics Server (Resource Metrics, HPA Integration)
55. Health Checks
    - Liveness Probe (Restart on Failure)
    - Readiness Probe (Remove from Service)
    - Startup Probe (Slow Starting Containers)
    - HTTP, TCP, Exec Probe Types
56. Distributed Tracing (Jaeger, Zipkin, OpenTelemetry)

### Deployment Strategies
57. Rolling Updates (maxSurge, maxUnavailable, Progress Deadline)
58. Blue-Green Deployment (Service Switching, Label Selector)
59. Canary Deployment (Traffic Splitting, Weighted Routing)
60. Rollback (kubectl rollout undo, Revision History)

### Package Management
61. Helm (Package Manager, Chart Repository)
62. Helm Charts (Chart.yaml, values.yaml, Templates, Hooks)
63. Kustomize (Overlays, Patches, Base + Environment)
64. Operators (Custom Controllers, Operator SDK, Operator Lifecycle Manager)
65. Custom Resource Definitions (CRDs) (Extending K8s API, Custom Resources)

### Managed Kubernetes
66. EKS (AWS) (Node Groups, Fargate Profiles, IAM Integration, ALB Controller)
67. GKE (Google Cloud) (Autopilot, Node Auto-Provisioning)
68. AKS (Azure) (Node Pools, Azure AD Integration)
69. EKS vs GKE vs AKS Comparison

### Advanced Topics
70. Service Mesh (Istio, Linkerd)
    - Traffic Management, mTLS, Observability
    - Sidecar Injection, Virtual Services, Destination Rules
71. Multi-Cluster Management (Federation, Submariner)
72. GitOps with ArgoCD (Application CRD, Sync, Auto-Heal)
73. GitOps with Flux (Source Controller, Kustomize Controller)

### Troubleshooting & Interview Scenarios
74. Pod in CrashLoopBackOff — How to Debug
75. Pod Stuck in Pending — Common Causes
76. Service Not Reachable — Troubleshooting Steps
77. Node Not Ready — Diagnosis
78. How to Perform Zero-Downtime Deployment
79. How to Right-Size Resource Requests and Limits

---

## 🎯 Solution Architect Perspective

Kubernetes knowledge is crucial for:
- **Container Orchestration**: Automated deployment, scaling, management
- **High Availability**: Self-healing, automatic failover
- **Scalability**: Horizontal scaling, load distribution
- **Resource Optimization**: Efficient resource utilization
- **Cloud Native**: Portable across cloud providers
- **DevOps**: GitOps, CI/CD integration

---

← Previous: Docker | Back to Main Index | Next: AWS →
