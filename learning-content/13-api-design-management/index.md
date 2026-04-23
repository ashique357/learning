# API Design & Management

Master API design principles, protocols, and management for building scalable, maintainable APIs.

## 📑 Topics

### API Fundamentals
1. What is an API (Interface Contract, Producer, Consumer)
2. API Types (REST, GraphQL, gRPC, SOAP, WebSocket)
3. API Design Principles (Consistency, Simplicity, Discoverability)
4. API First Design (Contract First, Mock, Generate, Implement)
5. API Lifecycle (Design, Develop, Test, Deploy, Monitor, Deprecate)

### REST API
6. REST Basics (Representational State Transfer, Stateless, Resource-Based)
7. REST Principles (Uniform Interface, Client-Server, Stateless, Cacheable, Layered)
8. HTTP Methods
    - GET (Read, Idempotent, Cacheable)
    - POST (Create, Non-Idempotent)
    - PUT (Full Update, Idempotent)
    - PATCH (Partial Update)
    - DELETE (Remove, Idempotent)
    - HEAD, OPTIONS (Metadata, CORS Preflight)
9. HTTP Status Codes
    - 2xx (200 OK, 201 Created, 204 No Content)
    - 3xx (301 Moved, 304 Not Modified)
    - 4xx (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 409 Conflict, 429 Too Many Requests)
    - 5xx (500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable, 504 Gateway Timeout)
10. REST Resource Naming (Nouns, Plural, Hierarchical, Consistent)
11. REST URL Design (/users, /users/{id}, /users/{id}/orders, Query Parameters)
12. HATEOAS (Hypermedia Links, Self-Discoverable API)
13. REST Best Practices (Versioning, Pagination, Filtering, Error Format)
14. Idempotency in APIs (Idempotency Keys, Safe Methods, Retry Safety)

### GraphQL
15. GraphQL Basics (Query Language, Schema-Driven, Single Endpoint)
16. GraphQL Schema (Types, Fields, Scalars, Enums, Input Types)
17. Queries and Mutations (Read vs Write, Variables, Fragments)
18. GraphQL Resolvers (Field Resolution, Data Fetching, N+1 Problem)
19. GraphQL Subscriptions (Real-Time, WebSocket, Pub/Sub)
20. GraphQL vs REST (Over-Fetching, Under-Fetching, Flexibility vs Caching)
21. GraphQL Best Practices (Pagination, Error Handling, Depth Limiting, Complexity Analysis)

### gRPC
22. gRPC Basics (HTTP/2, Binary Protocol, High Performance)
23. Protocol Buffers (Schema Definition, Code Generation, Backward Compatibility)
24. gRPC Services (Unary, Server Streaming, Client Streaming, Bidirectional)
25. gRPC vs REST (Performance, Streaming, Browser Support, Tooling)

### API Design
26. API Versioning
    - URL Versioning (/v1/users)
    - Header Versioning (Accept-Version)
    - Query Parameter Versioning (?version=1)
    - Versioning Strategy Selection
27. Pagination
    - Offset-Based (page, limit, Total Count)
    - Cursor-Based (next_cursor, Efficient for Large Datasets)
    - Keyset-Based (WHERE id > last_id)
    - Pagination Strategy Comparison
28. Filtering and Sorting (?status=active&sort=created_at:desc)
29. Search APIs (Full-Text, Fuzzy, Faceted, Autocomplete)
30. Bulk Operations (Batch Create, Batch Update, Partial Failure Handling)
31. Async APIs (202 Accepted, Polling, Callback, Status Endpoint)
32. Webhooks (Event Notification, Retry, Signature Verification, Idempotency)
33. Long Polling (Client Waits, Server Responds When Data Available)
34. Server-Sent Events (SSE) (One-Way Stream, Text-Based, Auto-Reconnect)
35. WebSockets (Full-Duplex, Persistent Connection, Use Cases)
36. API Error Response Design (Error Code, Message, Details, Trace ID)
37. API Backward Compatibility (Additive Changes, Deprecation, Migration)

### API Documentation
38. API Documentation Basics (Why, What to Document, Examples)
39. OpenAPI/Swagger (Specification, YAML/JSON, Code Generation)
40. API Specification (Request/Response Schema, Examples, Error Codes)
41. Interactive Documentation (Swagger UI, ReDoc, Try-It-Out)
42. API Examples (cURL, Postman Collections, SDK Examples)

### API Security
43. API Security Basics (Authentication, Authorization, Encryption)
44. Authentication (API Keys, OAuth 2.0, JWT, mTLS)
45. Authorization (Scopes, Roles, Resource-Level Permissions)
46. API Rate Limiting (Token Bucket, Sliding Window, Per-User, Per-IP)
47. API Throttling (Graceful Degradation, 429 Response, Retry-After Header)
48. CORS (Cross-Origin Resource Sharing)
    - Preflight Request (OPTIONS)
    - Access-Control-Allow-Origin, Methods, Headers
    - Credentials, Wildcard Limitations
49. API Security Best Practices (HTTPS, Input Validation, Output Encoding)
50. OWASP API Security Top 10 (Broken Object Level Auth, Mass Assignment, Injection)

### API Gateway
51. API Gateway Basics (Single Entry Point, Cross-Cutting Concerns)
52. API Gateway Features (Routing, Auth, Rate Limiting, Caching, Transformation)
53. AWS API Gateway (REST, HTTP, WebSocket, Stages, Usage Plans)
54. Kong (Plugins, Routes, Services, Consumers, Declarative Config)
55. Apigee (Proxies, Policies, Analytics, Developer Portal)
56. Azure API Management (Policies, Products, Subscriptions)

### API Management
57. API Management Basics (Lifecycle, Governance, Analytics)
58. API Catalog (Discovery, Self-Service, Developer Portal)
59. API Governance (Standards, Review, Linting, Style Guide)
60. API Lifecycle Management (Versioning, Deprecation, Sunset)
61. API Deprecation (Sunset Header, Migration Guide, Timeline)

### API Performance
62. API Performance Optimization (Response Time, Payload Size)
63. Caching Strategies (HTTP Cache Headers, ETag, Last-Modified, CDN)
64. Response Compression (gzip, Brotli, Content-Encoding)
65. Connection Pooling (HTTP Keep-Alive, Connection Reuse)
66. API Load Testing (k6, JMeter, Gatling, Locust)

### API Monitoring
67. API Monitoring Basics (Availability, Latency, Error Rate)
68. API Metrics (P50, P95, P99 Latency, Request Rate, Error Rate)
69. API Logging (Request/Response Logging, Correlation ID, Sampling)
70. API Analytics (Usage Patterns, Top Consumers, Trending Endpoints)
71. Error Tracking (4xx vs 5xx, Error Grouping, Alerting)
72. API Health Checks (Liveness, Readiness, Dependency Checks)

### API Testing
73. API Testing Basics (Functional, Performance, Security)
74. Unit Testing APIs (Controller Tests, Service Tests, Mocking)
75. Integration Testing (End-to-End, Database, External Services)
76. Contract Testing (Pact, Consumer-Driven, Provider Verification)
77. API Test Automation (Postman, Newman, REST Assured, pytest)

### Advanced Topics
78. API Composition (Aggregation, Orchestration, BFF)
79. Backend for Frontend (BFF) (Per-Client API, Mobile vs Web)
80. API Orchestration (Saga, Choreography, Step Functions)
81. API Monetization (Freemium, Pay-Per-Use, Tiered Plans)
82. Public vs Private APIs (Internal, Partner, Open, Security Considerations)

### Interview Scenarios
83. Design a REST API for an E-Commerce Platform
84. How to Handle API Versioning Without Breaking Clients
85. Pagination — Offset vs Cursor — Trade-offs
86. How to Secure a Public API
87. REST vs GraphQL vs gRPC — When to Use Which

---

## 🎯 Solution Architect Perspective

API Design & Management is crucial for:
- **Integration**: Connect systems and services
- **Developer Experience**: Easy to use, well-documented APIs
- **Scalability**: Handle growing traffic and users
- **Security**: Protect data and prevent abuse
- **Versioning**: Evolve APIs without breaking clients
- **Monitoring**: Track usage, performance, and errors

---

← Previous: Message Queues & Streaming | Back to Main Index | Next: Java →
