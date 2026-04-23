# Design Patterns

Master software design patterns and best practices for building maintainable systems.

## 📑 Topics

### Design Patterns Fundamentals
1. What are Design Patterns (Gang of Four, Problem-Solution-Consequence)
2. Why Use Design Patterns (Communication, Reusability, Proven Solutions)
3. Pattern Categories (Creational, Structural, Behavioral)
4. SOLID Principles
    - Single Responsibility Principle (One Reason to Change)
    - Open/Closed Principle (Open for Extension, Closed for Modification)
    - Liskov Substitution Principle (Subtypes Must Be Substitutable)
    - Interface Segregation Principle (Small, Focused Interfaces)
    - Dependency Inversion Principle (Depend on Abstractions)
5. DRY, KISS, YAGNI (Don't Repeat Yourself, Keep It Simple, You Aren't Gonna Need It)
6. Composition over Inheritance (When to Use Which, Trade-offs)
7. When to Use Which Pattern (Decision Matrix)

### Creational Patterns
8. Singleton (Eager, Lazy, Thread-Safe, Double-Checked Locking, Enum, Bill Pugh)
    - Breaking Singleton (Reflection, Serialization, Cloning)
    - Singleton vs Static Class
9. Factory Method (Creator, Product, Parameterized Factory)
10. Abstract Factory (Family of Related Objects, Platform Independence)
11. Builder (Step-by-Step Construction, Fluent API, Director)
    - Builder vs Constructor (When to Use)
12. Prototype (Shallow vs Deep Clone, Prototype Registry)
13. Object Pool (Resource Reuse, Connection Pool, Thread Pool)

### Structural Patterns
14. Adapter (Class vs Object Adapter, Legacy Integration)
15. Bridge (Abstraction-Implementation Separation, Platform Independence)
16. Composite (Tree Structure, Leaf vs Composite, File System Example)
17. Decorator (Dynamic Behavior Addition, Wrapper Chain, Java I/O Streams)
18. Facade (Simplified Interface, Subsystem Encapsulation)
19. Flyweight (Shared State, Intrinsic vs Extrinsic, String Pool Example)
20. Proxy (Virtual, Protection, Remote, Caching Proxy)

### Behavioral Patterns
21. Chain of Responsibility (Handler Chain, Middleware, Servlet Filters)
22. Command (Encapsulate Request, Undo/Redo, Queue Commands)
23. Iterator (Sequential Access, Internal vs External Iterator)
24. Mediator (Centralized Communication, Chat Room Example)
25. Memento (State Snapshot, Undo, Caretaker-Originator)
26. Observer (Event System, Publisher-Subscriber, Loose Coupling)
27. State (State Machine, Context, State Transitions)
28. Strategy (Interchangeable Algorithms, Runtime Selection, Comparator Example)
29. Template Method (Algorithm Skeleton, Hook Methods, Abstract Steps)
30. Visitor (Double Dispatch, Adding Operations Without Modifying Classes)
31. Null Object (Avoid Null Checks, Default Behavior)
32. Specification (Business Rules, Composable Criteria, AND/OR/NOT)

### Architectural Patterns
33. MVC (Model-View-Controller) (Web Frameworks, Separation of Concerns)
34. MVP (Model-View-Presenter) (Testable UI, Passive View)
35. MVVM (Model-View-ViewModel) (Data Binding, Angular, WPF)
36. Layered Architecture (Presentation, Business, Data, Infrastructure)
37. Hexagonal Architecture (Ports and Adapters, Dependency Inversion)
38. Clean Architecture (Entities, Use Cases, Interface Adapters, Frameworks)
39. Onion Architecture (Domain Core, Application, Infrastructure)

### Dependency Injection
40. Dependency Injection Pattern (Constructor, Setter, Interface Injection)
41. IoC Container (Spring, Guice, Dagger)
42. Service Locator vs Dependency Injection (Trade-offs)

### Data Patterns
43. Repository Pattern (Data Access Abstraction, Collection-Like Interface)
44. Unit of Work (Transaction Management, Change Tracking)
45. Data Mapper (Object-Relational Mapping, Separation)
46. Active Record (Object = Row, Rails, Django ORM)
47. DAO (Data Access Object) (CRUD Abstraction, Database Independence)

### Concurrency Patterns
48. Thread Pool (Fixed, Cached, Scheduled, Work Stealing)
49. Producer-Consumer (Bounded Buffer, BlockingQueue)
50. Read-Write Lock (Multiple Readers, Single Writer)
51. Double-Checked Locking (Lazy Initialization, volatile)

### Cloud & Resilience Patterns
52. Retry Pattern (Exponential Backoff, Jitter, Max Retries)
53. Bulkhead Pattern (Isolation, Resource Pools, Thread Pool Isolation)
54. Throttling Pattern (Rate Limiting, Token Bucket, Leaky Bucket)
55. Cache-Aside (Lazy Loading, Cache Miss, Cache Invalidation)
56. Valet Key (Temporary Access, Pre-Signed URLs, SAS Tokens)
57. Static Content Hosting (CDN, S3, Blob Storage)
58. Queue-Based Load Leveling (Buffer, Decouple, Smooth Traffic)

### Anti-Patterns
59. Common Anti-Patterns (Recognition, Refactoring)
60. God Object (Too Many Responsibilities, Refactoring Strategies)
61. Spaghetti Code (No Structure, Tangled Dependencies)
62. Golden Hammer (One Solution for Everything)
63. Premature Optimization (Profile First, Optimize Later)
64. Cargo Cult Programming (Copying Without Understanding)

### Interview Scenarios
65. When Would You Use Strategy vs State Pattern
66. Singleton — Thread Safety and Breaking Scenarios
67. How to Implement an LRU Cache (Decorator + LinkedHashMap)
68. Real-World Examples of Observer Pattern
69. Factory vs Abstract Factory — When to Use Which

---

## 🎯 Solution Architect Perspective

Design patterns knowledge is crucial for:
- **Code Quality**: Maintainable, readable, testable code
- **Communication**: Common vocabulary for design discussions
- **Problem Solving**: Proven solutions to common problems
- **Scalability**: Patterns that support growth
- **Flexibility**: Easy to modify and extend
- **Best Practices**: Industry-standard approaches

---

← Previous: CI/CD | Back to Main Index | Next: Monitoring & Observability →
