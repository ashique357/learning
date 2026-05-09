# Docker

Master containerization, Docker fundamentals, and container best practices.

## 📑 Topics

### Docker Fundamentals
1. What is Docker (Containerization, Why Docker)
2. Containers vs Virtual Machines (Architecture, Performance, Isolation)
3. Docker Architecture (Client, Daemon, Registry, Images, Containers)
4. Docker Engine (containerd, runc, shim)
5. Docker Installation and Setup

### Images
**6. Docker Images (Layers, Read-Only, Image ID, Digest)**
7. Dockerfile
    - FROM, RUN, CMD, ENTRYPOINT, COPY, ADD, WORKDIR, EXPOSE, ENV, ARG
    - CMD vs ENTRYPOINT (Difference, When to Use)
    - COPY vs ADD (Difference, Best Practice)
8. Dockerfile Best Practices
    - Minimize Layers
    - Order Instructions for Cache Optimization
    - Use .dockerignore
    - Non-Root User
    - Pin Base Image Versions
9. Multi-Stage Builds (Reduce Image Size, Build vs Runtime)
10. Image Layers (Layer Caching, Cache Busting)
11. Image Optimization (Minimal Base Images, Alpine, Distroless, Slim)
12. Base Images (Official Images, Custom Base Images)

### Containers
13. Container Lifecycle (Created, Running, Paused, Stopped, Removed)
14. Running Containers (docker run, -d, -it, --name, --rm, -p, -v, -e)
15. Container Commands (docker ps, logs, inspect, exec, cp, stats, top)
16. Container Logs (Log Drivers, JSON-file, Syslog, Fluentd)
17. Container Exec (Debugging Running Containers, Shell Access)
18. Container Resource Limits (--memory, --cpus, --pids-limit)

### Networking
19. Docker Networking Basics (Network Drivers, DNS Resolution)
20. Bridge Network (Default, Custom Bridge, Container Isolation)
21. Host Network (No Isolation, Performance)
22. Overlay Network (Multi-Host, Swarm, Encryption)
23. None Network (Complete Isolation)
24. Port Mapping (-p host:container, -P Random Port)
25. Container Communication (Same Network, Cross-Network, Links)

### Storage
26. Docker Volumes (Named Volumes, docker volume create/ls/rm/inspect)
27. Bind Mounts (Host Path Mapping, Development Use Case)
28. tmpfs Mounts (In-Memory, Temporary Data)
29. Volume Drivers (Local, NFS, Cloud Storage)
30. Data Persistence (Stateful Containers, Database Containers)

### Docker Compose
31. Docker Compose Basics (docker-compose.yml, Version)
32. Compose File Structure (services, networks, volumes, environment)
33. Multi-Container Applications (Web + DB + Cache)
34. Compose Networking (Default Network, Custom Networks, Aliases)
35. Compose Volumes (Named, Bind, Shared Between Services)
36. Compose Commands (up, down, build, logs, exec, ps, scale)
37. Compose Profiles and Overrides (docker-compose.override.yml)

### Registry
38. Docker Registry (Push, Pull, Registry API)
39. Docker Hub (Public, Private Repositories)
40. Private Registry (Self-Hosted, ECR, GCR, ACR)
41. Image Tagging (Semantic Versioning, latest, SHA)
42. Image Versioning (Immutable Tags, Tag Strategy)

### Security
43. Container Security (Principle of Least Privilege, Read-Only Filesystem)
44. Image Scanning (Trivy, Snyk, Docker Scout, CVE Detection)
45. User Namespaces (Non-Root Containers, USER Instruction)
46. Secrets Management (Docker Secrets, Environment Variables Pitfalls)
47. Security Best Practices
    - Don't Run as Root
    - Use Trusted Base Images
    - Scan Images in CI/CD
    - Limit Capabilities (--cap-drop, --cap-add)

### Production
48. Health Checks (HEALTHCHECK Instruction, Interval, Timeout, Retries)
49. Logging Strategies (Centralized Logging, Log Rotation)
50. Monitoring Containers (docker stats, cAdvisor, Prometheus)
51. Container Orchestration Basics (Why Orchestration, Options)
52. Docker Swarm (Services, Tasks, Overlay Network, Scaling)

### Advanced Topics
53. BuildKit (Parallel Builds, Cache Mounts, Secrets in Build)
54. Docker Content Trust (Image Signing, Notary)
55. Container Debugging (docker exec, nsenter, strace, tcpdump)
56. Performance Tuning (Storage Drivers, Overlay2, Resource Limits)
57. Docker vs Podman (Daemonless, Rootless, Compatibility)

### Interview Scenarios
58. How to Reduce Docker Image Size
59. How to Debug a Crashing Container
60. Docker Layer Caching — How It Works
61. How to Handle Persistent Data in Containers
62. Docker Networking — How Containers Communicate

---

## 🎯 Solution Architect Perspective

Docker knowledge is crucial for:
- **Application Packaging**: Consistent deployment across environments
- **Microservices**: Container per service pattern
- **CI/CD**: Build once, deploy anywhere
- **Resource Efficiency**: Better utilization than VMs
- **Scalability**: Quick startup, easy scaling
- **Development**: Dev/prod parity

---

← Previous: System Architecture | Back to Main Index | Next: Kubernetes →
