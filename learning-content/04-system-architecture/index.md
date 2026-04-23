# System Architecture

Master architectural patterns, scalability, reliability, and distributed systems design.

## 📑 Topics

### Architecture Fundamentals
1. System Design Basics (Requirements, Constraints, Trade-offs)
2. System Design Interview Framework
    - Clarify Requirements (Functional, Non-Functional)
    - Back-of-Envelope Estimation (QPS, Storage, Bandwidth)
    - High-Level Design
    - Deep Dive
    - Bottlenecks & Trade-offs
3. Architectural Patterns Overview
4. Monolithic Architecture (Pros, Cons, When to Use)
5. Microservices Architecture (Pros, Cons, Decomposition Strategies)
6. Serverless Architecture (FaaS, BaaS, Cold Start, Limitations)
7. Event-Driven Architecture (Event Producers, Consumers, Event Bus)
8. Service-Oriented Architecture (SOA) (ESB, WSDL, SOA vs Microservices)

### Scalability
9. Horizontal vs Vertical Scaling (When to Use Which)
10. Load Balancing Concepts (Layer 4 vs Layer 7, Algorithms, Health Checks)
11. Caching Strategies
    - Cache-Aside (Lazy Loading)
    - Read-Through, Write-Through, Write-Behind
    - Cache Invalidation (TTL, Event-Based, Manual)
    - Cache Stampede Prevention
12. CDN Concepts (Edge Caching, Origin Shield, Cache Hit Ratio)
13. Database Scaling (Read Replicas, Sharding, Partitioning)
14. Stateless vs Stateful Design (Session Management, Sticky Sessions)
15. Auto-Scaling (Metrics-Based, Predictive, Scheduled)

### Reliability and Availability
16. High Availability (Active-Active, Active-Passive, Multi-AZ, Multi-Region)
17. Fault Tolerance (Graceful Degradation, Failover)
18. Disaster Recovery (RPO, RTO, Backup & Restore, Pilot Light, Warm Standby, Active-Active)
19. Redundancy (Data, Service, Infrastructure)
20. Failover Strategies (DNS Failover, Database Failover, Application Failover)
21. Circuit Breaker Pattern (Closed, Open, Half-Open States)
22. Retry and Backoff (Exponential Backoff, Jitter, Max Retries)
23. Bulkhead Pattern (Isolation, Resource Pools)

### Distributed Systems
24. Distributed System Basics (Fallacies of Distributed Computing)
25. Consistency Models (Strong, Eventual, Causal, Read-Your-Writes)
26. Eventual Consistency (Conflict Resolution, Last-Write-Wins, Vector Clocks)
27. Distributed Transactions (2PC Limitations, Saga Pattern)
28. Two-Phase Commit (Coordinator, Participants, Blocking Problem)
29. Saga Pattern (Choreography vs Orchestration, Compensating Transactions)
30. Consensus Algorithms (Paxos, Raft, Leader Election)
31. Consistent Hashing (Virtual Nodes, Ring-Based, Use Cases)
32. Distributed Locking (Redis Lock, ZooKeeper, Fencing Tokens)
33. Bloom Filters (Probabilistic Data Structure, False Positives, Use Cases)
34. Idempotency (Idempotency Keys, At-Least-Once + Idempotency = Exactly-Once)

### Communication Patterns
35. Synchronous vs Asynchronous (Trade-offs, When to Use)
36. Request-Response Pattern
37. Event-Driven Communication
38. Message-Based Communication (Point-to-Point, Pub/Sub)
39. Streaming Communication (Real-Time, Backpressure)

### Data Management
40. Data Partitioning (Horizontal, Vertical, Functional)
41. Data Replication (Sync, Async, Semi-Sync)
42. CQRS (Command Query Responsibility Segregation)
    - Separate Read/Write Models
    - Eventual Consistency Between Models
43. Event Sourcing (Event Store, Replay, Snapshots)
44. Database per Service (Data Isolation, Cross-Service Queries)
45. Shared Database (Simplicity vs Coupling)

### Performance
46. Performance Optimization (Profiling, Benchmarking)
47. Latency vs Throughput (Trade-offs, P50/P95/P99 Percentiles)
48. Bottleneck Identification (CPU, Memory, I/O, Network)
49. Rate Limiting (Token Bucket, Leaky Bucket, Fixed Window, Sliding Window)
50. Throttling (Client-Side, Server-Side, Graceful Degradation)
51. Connection Pooling (Database, HTTP, gRPC)

### Advanced Topics
52. Service Mesh (Sidecar Proxy, Istio, Linkerd, mTLS)
53. Backend for Frontend (BFF) (Per-Client API Layer)
54. Strangler Fig Pattern (Incremental Migration)
55. Multi-Tenancy (Shared DB, Schema per Tenant, DB per Tenant)
56. Multi-Region Architecture (Data Replication, Latency, Conflict Resolution)
57. Hybrid Architecture (On-Premise + Cloud, Connectivity)
58. Cell-Based Architecture (Blast Radius Reduction, Cell Routing)
59. API Gateway vs Load Balancer vs Reverse Proxy (Comparison)

### Classic System Design Problems
60. URL Shortener (Hashing, Base62, Redirection)
61. Rate Limiter (Algorithms, Distributed Rate Limiting)
62. Chat System / WhatsApp (WebSocket, Message Queue, Presence)
63. Social Media Feed / Twitter (Fan-Out on Write vs Read, Timeline)
64. Video Streaming / Netflix (CDN, Transcoding, Adaptive Bitrate)
65. Ride Sharing / Uber (Geospatial Index, Matching, ETA)
66. Notification System (Push, Email, SMS, Priority, Retry)
67. E-Commerce System (Catalog, Cart, Order, Payment, Inventory)
68. Search Autocomplete / Typeahead (Trie, Prefix Matching)
69. Distributed Cache Design
70. Distributed Job Scheduler

---

## 🎯 Solution Architect Perspective

System architecture knowledge is crucial for:
- **Design Decisions**: Choosing right architecture for requirements
- **Scalability**: Designing systems that grow with demand
- **Reliability**: Building fault-tolerant, highly available systems
- **Performance**: Optimizing for latency and throughput
- **Cost**: Balancing performance with infrastructure costs
- **Maintainability**: Creating systems easy to evolve and debug

---

← Previous: Database | Back to Main Index | Next: Docker →
