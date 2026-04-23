# FastAPI

Master FastAPI for building high-performance, modern Python APIs.

## 📑 Topics

### FastAPI Fundamentals
1. FastAPI Overview (Async, Type Hints, Auto-Docs, High Performance)
2. FastAPI vs Django vs Flask
    - Django (Batteries-Included, ORM, Admin, Monolithic)
    - Flask (Minimal, Flexible, Extensions)
    - FastAPI (Async, Pydantic, OpenAPI, Performance)
    - When to Use Which
3. Installation and Setup (pip install fastapi uvicorn, Project Structure)
4. First API (app = FastAPI(), @app.get, uvicorn.run)
5. Path Operations (@app.get, @app.post, @app.put, @app.delete, @app.patch)
6. HTTP Methods (GET, POST, PUT, PATCH, DELETE, OPTIONS, HEAD)

### Request Handling
7. Path Parameters (/items/{item_id}, Type Validation, Enum)
8. Query Parameters (?skip=0&limit=10, Optional, Default Values)
9. Request Body (Pydantic Model, JSON Parsing, Nested Models)
10. Form Data (Form(...), File + Form Together)
11. File Uploads (UploadFile, Multiple Files, File Size Limits)
12. Headers (Header(...), Custom Headers, Auto-Conversion)
13. Cookies (Cookie(...), Set Cookie, Delete Cookie)

### Response Handling
14. Response Models (response_model, Exclude, Include, By Alias)
15. Status Codes (status.HTTP_201_CREATED, Custom Status)
16. Response Headers (Response.headers, Custom Headers)
17. JSON Response (JSONResponse, Custom Encoder)
18. File Response (FileResponse, StreamingResponse)
19. Streaming Response (StreamingResponse, Generator, Large Files)

### Pydantic Models
20. Pydantic Basics (BaseModel, Field Types, Validation, Serialization)
21. Data Validation (Type Coercion, Strict Mode, Custom Types)
22. Field Validation (Field(..., min_length, max_length, ge, le, regex))
23. Custom Validators (@field_validator, @model_validator, Before/After)
24. Nested Models (Model Composition, List of Models, Optional Nested)
25. Pydantic v2 Changes (model_validate, model_dump, ConfigDict, Performance)

### Dependency Injection
26. Dependencies Basics (Depends(), Function Dependencies)
27. Dependency Functions (Database Session, Auth User, Config)
28. Class Dependencies (Callable Classes, __call__)
29. Sub-dependencies (Dependency Chain, Caching, Scope)
30. Global Dependencies (app = FastAPI(dependencies=[...]))

### Database Integration
31. SQLAlchemy Integration (Engine, SessionLocal, Base, Dependency)
32. Database Models (Declarative Base, Columns, Relationships)
33. CRUD Operations (Create, Read, Update, Delete, Session Management)
34. Async Database (asyncpg, databases, async SQLAlchemy)
35. Database Sessions (Dependency Injection, Session Lifecycle, Commit/Rollback)
36. Alembic Migrations (alembic init, revision, upgrade, downgrade, Auto-Generate)
37. SQLModel (SQLAlchemy + Pydantic, Simplified ORM, FastAPI Integration)

### Authentication & Security
38. Security Basics (OAuth2PasswordBearer, SecurityScopes)
39. OAuth2 with Password Flow (Token Endpoint, Login, Password Hashing)
40. JWT Tokens (python-jose, Encode, Decode, Expiry, Refresh)
41. API Keys (Header-Based, Query-Based, Dependency Validation)
42. CORS (CORSMiddleware, Origins, Methods, Headers, Credentials)
43. HTTPS (TLS Termination, Reverse Proxy, Redirect)

### Advanced Features
44. Background Tasks (BackgroundTasks, add_task, Email, Cleanup)
45. Celery Integration (Task Definition, Worker, Broker, Result Backend)
46. WebSockets (WebSocket Endpoint, Accept, Send, Receive, Close)
47. Server-Sent Events (SSE) (EventSourceResponse, Streaming, sse-starlette)
48. Webhooks (Receiving, Sending, Signature Verification)
49. GraphQL (Strawberry, Ariadne, Schema, Resolvers)
50. Middleware (BaseHTTPMiddleware, Request/Response Processing, Timing)
51. Events (Startup, Shutdown, Lifespan Context Manager)
52. Sub Applications (Mounting, Prefix, Independent Apps)
53. Request Lifecycle (Middleware → Dependency → Route → Response)

### API Documentation
54. Automatic Documentation (Swagger UI at /docs, ReDoc at /redoc)
55. OpenAPI Schema (/openapi.json, Customization, Tags, Description)
56. Swagger UI (Try-It-Out, Authorization, Request Examples)
57. ReDoc (Clean Layout, Nested Models, Code Samples)
58. Custom Documentation (Custom OpenAPI Schema, Hiding Endpoints)

### Caching with FastAPI
59. Redis as Cache Backend (aioredis, redis-py, Dependency Injection)
60. Cache Strategies in FastAPI (fastapi-cache2, TTL, Key Builder)

### Testing
61. Testing Basics (TestClient, pytest, Async Tests)
62. Test Client (from starlette.testclient import TestClient, Requests-Like API)
63. Async Testing (httpx.AsyncClient, pytest-asyncio)
64. Mocking (Dependency Override, app.dependency_overrides, Mock DB)
65. Test Coverage (coverage.py, pytest-cov, Branch Coverage)

### Performance
66. Async/Await (Event Loop, Coroutines, When to Use async def vs def)
67. Concurrency (Async I/O, Thread Pool for Sync, run_in_executor)
68. Async vs Sync Performance (I/O-Bound vs CPU-Bound, Benchmarks)
69. Response Compression (GZipMiddleware, Brotli)
70. Performance Optimization (Connection Pooling, Caching, Profiling)

### Error Handling
71. Exception Handling (@app.exception_handler, HTTPException)
72. Custom Exceptions (Custom Exception Classes, Custom Handlers)
73. Error Responses (Detail, Status Code, Headers, RFC 7807)
74. Validation Errors (RequestValidationError, Custom Error Format)

### Deployment
75. Production Settings (Environment Variables, .env, pydantic-settings)
76. ASGI Servers
    - Uvicorn (Default, Workers, --reload, --host, --port)
    - Hypercorn (HTTP/2, HTTP/3)
    - Gunicorn + Uvicorn Workers (Process Management)
77. Docker Deployment (Dockerfile, Multi-Stage, Health Check)
78. Kubernetes Deployment (Deployment, Service, Ingress, Health Probes)
79. Cloud Deployment (AWS Lambda + Mangum, ECS, Azure, GCP Cloud Run)

### Best Practices
80. Project Structure (Routers, Schemas, Models, Services, Dependencies)
81. API Versioning (URL Prefix, Router Mounting, Header-Based)
82. Logging (Python logging, Structured Logging, Correlation ID)
83. Monitoring (Prometheus, OpenTelemetry, Middleware Metrics)
84. Rate Limiting (slowapi, Redis-Based, Per-User, Per-IP)
85. API Best Practices (Consistent Naming, Error Format, Pagination)

### Interview Scenarios
86. FastAPI vs Flask vs Django — When to Use Which
87. How Does Dependency Injection Work in FastAPI
88. Async vs Sync Endpoints — When to Use Which
89. How to Structure a Large FastAPI Project
90. Pydantic Validation — How It Works Internally

---

## 🎯 Solution Architect Perspective

FastAPI is crucial for:
- **Performance**: Async support, high throughput
- **Modern Python**: Type hints, async/await
- **Auto Documentation**: OpenAPI/Swagger out of the box
- **Data Validation**: Pydantic for robust validation
- **Developer Experience**: Fast development, easy testing
- **Production Ready**: Battle-tested, used by major companies

---

← Previous: Django | Back to Main Index | Next: Frontend Technologies →
