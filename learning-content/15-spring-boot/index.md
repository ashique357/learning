# Spring Boot

Master Spring Boot framework for building production-ready enterprise applications.

## 📑 Topics

### Spring Boot Fundamentals
1. Spring Boot Overview (Convention over Configuration, Opinionated Defaults)
2. Spring vs Spring Boot (What Spring Boot Adds, Starter POMs, Auto-Config)
3. Spring Boot Architecture (Application Context, Bean Factory, Auto-Configuration)
4. Spring Boot Starter Projects (spring-boot-starter-web, data-jpa, security, test)
5. Auto-Configuration (@EnableAutoConfiguration, Conditional Annotations, Customizing)
6. Application Properties (application.yml vs application.properties, Precedence)
7. Profiles (spring.profiles.active, Environment-Specific Config, @Profile)

### Dependency Injection & IoC
8. Inversion of Control (IoC) (Container Manages Object Lifecycle)
9. Dependency Injection
    - Constructor Injection (Preferred, Immutable)
    - Setter Injection (Optional Dependencies)
    - Field Injection (@Autowired, Why to Avoid)
10. Bean Lifecycle (Instantiation, Populate, Init, Destroy, @PostConstruct, @PreDestroy)
11. Bean Scopes (Singleton, Prototype, Request, Session, Application)
12. Component Scanning (@ComponentScan, Base Packages, Filters)
13. Annotations (@Component, @Service, @Repository, @Controller, @Configuration, @Bean)
    - @Component vs @Bean (When to Use Which)
    - @Qualifier, @Primary (Resolving Ambiguity)

### Spring Web MVC
14. Spring MVC Basics (DispatcherServlet, Handler Mapping, View Resolver)
15. Controllers (@Controller, @RestController, Difference)
16. Request Mapping (@RequestMapping, @GetMapping, @PostMapping, @PutMapping, @DeleteMapping)
17. Request Parameters (@RequestParam, Required, Default Value)
18. Path Variables (@PathVariable, Multiple Variables)
19. Request Body and Response Body (@RequestBody, @ResponseBody, JSON Serialization)
20. Exception Handling
    - @ExceptionHandler (Controller-Level)
    - @ControllerAdvice (Global Exception Handling)
    - @ResponseStatus (Custom Status Codes)
    - ProblemDetail (RFC 7807, Structured Error Response)
21. Validation (@Valid, @NotNull, @Size, @Email, Custom Validators, BindingResult)

### REST API Development
22. RESTful Services (Resource-Based, Stateless, HATEOAS)
23. REST Controllers (@RestController, ResponseEntity, Status Codes)
24. HTTP Methods (GET, POST, PUT, PATCH, DELETE Mapping)
25. Status Codes (Returning Appropriate Codes, ResponseEntity.created())
26. Content Negotiation (JSON, XML, Accept Header, Produces/Consumes)
27. HATEOAS (Spring HATEOAS, EntityModel, CollectionModel, Links)
28. API Versioning (URL, Header, Media Type Versioning in Spring)
29. Swagger/OpenAPI (springdoc-openapi, @Operation, @Schema, Swagger UI)

### Spring Data JPA
30. JPA Basics (Entity Manager, Persistence Context, JPA vs Hibernate)
31. Entity Mapping (@Entity, @Table, @Id, @GeneratedValue, @Column)
32. Relationships
    - @OneToOne (Unidirectional, Bidirectional, Shared Primary Key)
    - @OneToMany / @ManyToOne (Owning Side, mappedBy, Cascade)
    - @ManyToMany (Join Table, @JoinTable)
    - Fetch Types (LAZY vs EAGER, N+1 Problem, @EntityGraph)
33. Repository Pattern (JpaRepository, CrudRepository, PagingAndSortingRepository)
34. CRUD Operations (save, findById, findAll, delete, existsById)
35. Query Methods (findByName, findByStatusAndType, Derived Queries)
36. JPQL (Java Persistence Query Language, @Query, Named Parameters)
37. Native Queries (@Query nativeQuery=true, Result Mapping)
38. Pagination and Sorting (Pageable, Sort, Page, Slice)
39. Transactions (@Transactional, Propagation, Isolation, Rollback Rules)
    - Propagation Types (REQUIRED, REQUIRES_NEW, NESTED, SUPPORTS)

### Database Integration
40. Database Configuration (DataSource, H2, PostgreSQL, MySQL)
41. Connection Pooling (HikariCP) (Pool Size, Timeout, Leak Detection)
42. Multiple Data Sources (Configuration, @Primary, Routing DataSource)
43. Database Migration
    - Flyway (SQL-Based, Versioned Migrations, Repeatable)
    - Liquibase (XML/YAML/JSON, Changesets, Rollback)

### Spring Security
44. Security Basics (SecurityFilterChain, Authentication, Authorization)
45. Authentication (UserDetailsService, PasswordEncoder, AuthenticationManager)
46. Authorization (hasRole, hasAuthority, @PreAuthorize, @Secured)
47. JWT Authentication
    - JWT Generation, Validation, Refresh Token
    - JWT Filter Chain Integration
    - Stateless Session Management
48. OAuth2 (Resource Server, Client, Authorization Server, OIDC)
49. Method Security (@PreAuthorize, @PostAuthorize, SpEL Expressions)
50. CORS Configuration (CorsConfigurationSource, Allowed Origins, Methods, Headers)

### Microservices with Spring
51. Microservices Architecture (Decomposition, Bounded Context, Communication)
52. Spring Cloud (Overview, Dependencies, Version Compatibility)
53. Service Discovery (Eureka) (Server, Client, Registration, Heartbeat)
54. API Gateway (Spring Cloud Gateway) (Routes, Predicates, Filters, Rate Limiting)
55. Load Balancing (Spring Cloud LoadBalancer, Client-Side, Round Robin)
56. Circuit Breaker (Resilience4j)
    - Circuit Breaker (Closed, Open, Half-Open, Failure Rate)
    - Retry, Rate Limiter, Bulkhead, Time Limiter
    - @CircuitBreaker, @Retry Annotations
57. Distributed Tracing (Micrometer Tracing, Zipkin, Trace ID, Span ID)
58. Config Server (Centralized Config, Git Backend, Refresh, Encryption)

### Messaging with Spring
59. Spring JMS (JmsTemplate, @JmsListener, Connection Factory)
60. Spring AMQP (RabbitMQ Integration)
    - RabbitTemplate (Send, Convert and Send)
    - @RabbitListener (Message Consumption, Concurrency)
    - Error Handling (Retry, Dead Letter Exchange)
61. Spring Kafka Integration
    - KafkaTemplate (Send, ProducerFactory)
    - @KafkaListener (Consumer Group, Partition Assignment)
    - Error Handling (ErrorHandler, Dead Letter Topic, Retry Topic)
    - Kafka Streams with Spring (StreamsBuilder, KStream, KTable)
62. WebSockets with Spring (@MessageMapping, STOMP, SockJS)
63. Server-Sent Events (SSE) (SseEmitter, Flux<ServerSentEvent>)

### Caching & Redis with Spring
64. Spring Cache Abstraction (@Cacheable, @CacheEvict, @CachePut, @Caching)
65. Spring Data Redis (RedisTemplate, StringRedisTemplate, Repository)
66. RedisTemplate Operations (opsForValue, opsForHash, opsForList, opsForSet, opsForZSet)
67. Redis as Cache Backend (RedisCacheManager, TTL, Serialization)
68. Redis as Session Store (Spring Session, @EnableRedisHttpSession)
69. Cache Strategies (Cache-Aside, Write-Through, Write-Behind)
70. Cache Eviction Policies (TTL, LRU, LFU, Manual Eviction)

### Testing
71. Unit Testing with JUnit (@Test, @BeforeEach, Assertions, @ExtendWith)
72. Integration Testing (@SpringBootTest, @AutoConfigureMockMvc, TestRestTemplate)
73. MockMvc (perform, andExpect, Content Matching, Status Matching)
74. Test Containers (@Testcontainers, PostgreSQL, Redis, Kafka in Tests)
75. Mocking with Mockito (@Mock, @InjectMocks, when/thenReturn, verify, ArgumentCaptor)

### Monitoring & Actuator
76. Spring Boot Actuator (/actuator, Endpoints, Exposure)
77. Health Checks (/health, Custom Health Indicators, Liveness, Readiness)
78. Metrics (/metrics, Micrometer, Counter, Gauge, Timer, Distribution Summary)
79. Custom Endpoints (@Endpoint, @ReadOperation, @WriteOperation)
80. Prometheus Integration (micrometer-registry-prometheus, /actuator/prometheus)

### Performance & Optimization
81. Performance Tuning (Connection Pool, Thread Pool, JVM Flags)
82. Connection Pool Tuning (HikariCP Settings, Pool Size Formula)
83. Async Processing (@Async, CompletableFuture, TaskExecutor Configuration)
84. Batch Processing (Spring Batch, Job, Step, Reader, Processor, Writer)
85. Scheduling (@Scheduled, fixedRate, fixedDelay, cron, @EnableScheduling)

### Deployment
86. Packaging (JAR vs WAR, Embedded Server, Executable JAR)
87. Docker Deployment (Dockerfile, Multi-Stage Build, Jib, Buildpacks)
88. Kubernetes Deployment (Deployment YAML, ConfigMap, Secrets, Health Probes)
89. Cloud Deployment (AWS Elastic Beanstalk, ECS, EKS, Azure App Service)
90. Production Best Practices (Graceful Shutdown, Externalized Config, Logging)

### Reactive Programming
91. Spring WebFlux Basics (Non-Blocking, Event Loop, Netty)
92. Reactive Streams (Publisher, Subscriber, Subscription, Processor)
93. Mono and Flux (Mono<T> Single, Flux<T> Multiple, Operators)
94. Reactive Repositories (R2DBC, ReactiveCrudRepository)
95. Reactive REST APIs (@RestController with Mono/Flux, WebClient)
96. Reactive WebClient (Non-Blocking HTTP Client, Replacing RestTemplate)
97. Backpressure (Overflow Strategies, Buffer, Drop, Latest)
98. Reactive vs Imperative (When to Use Which, Trade-offs, Debugging)

### Interview Scenarios
99. Spring Bean Lifecycle — Explain Step by Step
100. @Transactional — How It Works Internally (Proxy, AOP)
101. N+1 Problem in JPA — How to Solve
102. How to Implement JWT Authentication in Spring Boot
103. Spring Boot Auto-Configuration — How It Works

---

## 🎯 Solution Architect Perspective

Spring Boot is crucial for:
- **Rapid Development**: Convention over configuration
- **Microservices**: Complete ecosystem for distributed systems
- **Enterprise Ready**: Production-grade features out of the box
- **Scalability**: Horizontal scaling, cloud-native
- **Integration**: Extensive third-party integrations
- **Community**: Large ecosystem, extensive documentation

---

← Previous: Java | Back to Main Index | Next: Python →
