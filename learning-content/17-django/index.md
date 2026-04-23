# Django

Master Django framework for building robust, scalable web applications.

## 📑 Topics

### Django Fundamentals
1. Django Overview (Batteries-Included, MTV Architecture, ORM, Admin)
2. Django Architecture (MTV: Model-Template-View, Request Lifecycle)
3. Django Installation (pip install django, django-admin startproject)
4. Project Structure (manage.py, settings.py, urls.py, wsgi.py, asgi.py)
5. Django Settings (DEBUG, ALLOWED_HOSTS, DATABASES, INSTALLED_APPS, MIDDLEWARE)
6. Django Apps (startapp, App Config, App Registry, Reusable Apps)

### URL Routing
7. URL Configuration (urlpatterns, path, re_path, include)
8. URL Patterns (Static, Dynamic, Regex, Converters)
9. Path Converters (int, str, slug, uuid, Custom Converters)
10. URL Namespaces (app_name, namespace, reverse, {% url %})

### Views
11. Function-Based Views (Request, Response, HttpResponse, JsonResponse)
12. Class-Based Views (View, TemplateView, as_view(), Method Handlers)
13. Generic Views (ListView, DetailView, CreateView, UpdateView, DeleteView)
14. View Mixins (LoginRequiredMixin, PermissionRequiredMixin, Custom Mixins)
15. Request and Response (HttpRequest, HttpResponse, QueryDict, FileUpload)

### Templates
16. Template Basics (Template Engine, Rendering, Context)
17. Template Syntax ({{ variable }}, {% tag %}, {# comment #})
18. Template Inheritance ({% extends %}, {% block %}, Base Templates)
19. Template Tags and Filters ({% for %}, {% if %}, |date, |default, |truncatewords)
20. Custom Template Tags (simple_tag, inclusion_tag, Library Registration)
21. Static Files (STATIC_URL, STATICFILES_DIRS, {% static %}, collectstatic)

### Models and ORM
22. Models Basics (Model Class, Fields, Meta, __str__, save, delete)
23. Field Types (CharField, IntegerField, DateTimeField, ForeignKey, JSONField, FileField)
24. Model Relationships
    - ForeignKey (Many-to-One, on_delete, related_name)
    - OneToOneField (Profile Pattern)
    - ManyToManyField (Through Model, Intermediate Table)
25. QuerySets (Lazy Evaluation, Chaining, Caching, Evaluation Triggers)
26. Query Optimization
    - select_related (ForeignKey, OneToOne, SQL JOIN)
    - prefetch_related (ManyToMany, Reverse FK, Separate Query)
    - N+1 Problem (Detection, Prevention)
    - only(), defer() (Partial Loading)
27. Aggregation (aggregate, annotate, Count, Sum, Avg, Max, F Expressions)
28. Q Objects (Complex Queries, OR, AND, NOT, Combining Conditions)
29. Transactions (atomic, savepoint, on_commit, select_for_update)
30. Database Migrations (makemigrations, migrate, squashmigrations, Data Migrations)
31. Model Managers (Custom Manager, Custom QuerySet, Default Manager)

### Forms
32. Forms Basics (Form Class, Fields, Validation, Rendering)
33. ModelForms (Model Binding, fields, exclude, save)
34. Form Validation (clean, clean_<field>, ValidationError)
35. Form Widgets (TextInput, Select, DateInput, Custom Widgets)
36. Formsets (BaseFormSet, ModelFormSet, Inline Formsets)

### Django Admin
37. Admin Interface (ModelAdmin, register, list_display, list_filter)
38. Customizing Admin (fieldsets, readonly_fields, inlines, Custom Templates)
39. Admin Actions (Custom Actions, Bulk Operations)
40. Admin Filters (SimpleListFilter, Custom Filters)

### Authentication & Authorization
41. User Authentication (authenticate, login, logout, @login_required)
42. User Model (AbstractUser, AbstractBaseUser, AUTH_USER_MODEL)
43. Custom User Model (When and How, Email-Based Auth)
44. Permissions (add, change, delete, view, Custom Permissions)
45. Groups (Group Model, Group Permissions, Bulk Assignment)
46. Login/Logout (LoginView, LogoutView, Custom Templates, Redirect)
47. Password Management (PasswordChangeView, PasswordResetView, Hashers)

### Django REST Framework
48. DRF Basics (APIView, Response, Status Codes, Browsable API)
49. Serializers (Serializer, ModelSerializer, Nested, Validation)
50. API Views (APIView, @api_view, GenericAPIView)
51. ViewSets and Routers (ModelViewSet, DefaultRouter, URL Generation)
52. Authentication (TokenAuthentication, JWTAuthentication, SessionAuthentication)
53. Permissions (IsAuthenticated, IsAdminUser, Custom Permissions, Object-Level)
54. Pagination (PageNumberPagination, LimitOffsetPagination, CursorPagination)
55. Filtering and Searching (django-filter, SearchFilter, OrderingFilter)
56. Throttling (AnonRateThrottle, UserRateThrottle, Custom Throttle)
57. API Documentation (drf-spectacular, OpenAPI, Swagger UI)

### Django Signals
58. Signal Basics (pre_save, post_save, pre_delete, post_delete, m2m_changed)
59. Custom Signals (Signal, send, connect, receiver Decorator)
60. Signal Best Practices (When to Use, When to Avoid, Performance)

### Middleware
61. Middleware Basics (Request/Response Processing, Order Matters)
62. Custom Middleware (__init__, __call__, process_view, process_exception)
63. Built-in Middleware (SecurityMiddleware, SessionMiddleware, CsrfViewMiddleware)

### Sessions and Cookies
64. Session Management (Session Backend, Session Data, Expiry)
65. Cookie Handling (set_cookie, get, Secure, HttpOnly, SameSite)
66. Session Backends (Database, Cache, File, Cookie-Based)

### Caching with Django
67. Django Cache Framework (cache.set, cache.get, cache.delete)
68. Cache Backends Configuration (Memcached, Redis, Database, File, Local Memory)
69. Per-View Caching (@cache_page, Vary Headers)
70. Template Fragment Caching ({% cache %}, Timeout, Key)
71. Redis as Cache Backend (django-redis, Configuration, Serialization)

### Async Tasks with Django
72. Celery Integration with Django (celery.py, @shared_task, Auto-Discover)
73. Defining & Running Tasks (delay, apply_async, Task Options, Retry)
74. Celery Beat (Periodic Tasks, Crontab Schedule, Database Scheduler)
75. Broker Configuration (Redis as Broker, RabbitMQ as Broker, Result Backend)

### Real-time Features
76. Django Channels (ASGI, Channel Layers, Consumers, Routing)
77. WebSockets with Django (WebsocketConsumer, AsyncWebsocketConsumer, Groups)
78. Webhooks (Receiving, Sending, Signature Verification)

### Django Management Commands
79. Built-in Commands (runserver, migrate, createsuperuser, shell, dbshell)
80. Custom Management Commands (BaseCommand, add_arguments, handle)

### Security
81. CSRF Protection ({% csrf_token %}, CsrfViewMiddleware, AJAX CSRF)
82. XSS Prevention (Auto-Escaping, |safe, mark_safe, Content Security Policy)
83. SQL Injection Prevention (ORM Parameterization, raw() Caution)
84. Security Best Practices (SECRET_KEY, DEBUG=False, SECURE_SSL_REDIRECT)
85. HTTPS and SSL (SECURE_HSTS_SECONDS, SECURE_PROXY_SSL_HEADER)

### Testing
86. Unit Testing (TestCase, setUp, tearDown, Assertions, @override_settings)
87. Integration Testing (Client, RequestFactory, Live Server)
88. Test Client (client.get, client.post, Response Assertions, Login)
89. Fixtures (JSON, YAML, Factory Boy, Model Bakery)
90. Coverage (coverage.py, Branch Coverage, HTML Report)

### Deployment
91. Production Settings (Environment Variables, django-environ, Whitenoise)
92. WSGI and ASGI (Gunicorn, Uvicorn, Daphne, Workers)
93. Static Files in Production (collectstatic, Whitenoise, CDN, S3)
94. Database Configuration (PostgreSQL, Connection Pooling, pgbouncer)
95. Docker Deployment (Dockerfile, docker-compose, Multi-Stage)
96. Cloud Deployment (AWS, Azure, GCP, Heroku, Railway)

### Performance
97. Query Optimization (select_related, prefetch_related, Indexing, EXPLAIN)
98. Database Indexing (db_index, Index Together, Partial Index)
99. Caching Strategies (Page Cache, Fragment Cache, Query Cache, Invalidation)
100. Performance Monitoring (Django Debug Toolbar, django-silk, New Relic)

### Interview Scenarios
101. Django Request Lifecycle — Explain Step by Step
102. N+1 Problem — How to Detect and Fix in Django
103. select_related vs prefetch_related — When to Use Which
104. How to Implement Custom User Model
105. Django Signals — Use Cases and Pitfalls

---

## 🎯 Solution Architect Perspective

Django is crucial for:
- **Rapid Development**: Batteries-included framework
- **Admin Interface**: Built-in admin panel
- **ORM**: Powerful database abstraction
- **Security**: Built-in protection against common vulnerabilities
- **Scalability**: Proven at scale (Instagram, Pinterest)
- **REST APIs**: Django REST Framework for API development

---

← Previous: Python | Back to Main Index | Next: FastAPI →
