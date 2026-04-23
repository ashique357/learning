# Java

Master Java programming language, core concepts, and enterprise development.

## 📑 Topics

### Java Fundamentals
1. Java Basics and JVM Architecture
2. JDK vs JRE vs JVM
3. Java Compilation & Execution Flow
4. Java Installation and Setup
5. Java Syntax and Structure
6. Data Types and Variables (Primitive vs Reference)
7. Type Casting (Widening, Narrowing, Autoboxing, Unboxing)
8. Operators
9. Control Flow (if, switch, loops)
10. Arrays (Single, Multi-dimensional)
11. Strings
    - String Pool & Immutability
    - String vs StringBuilder vs StringBuffer
    - String Interning
    - Common String Methods
12. Methods (Pass by Value vs Reference)
13. Varargs
14. Input/Output

### Object-Oriented Programming
15. Classes and Objects
16. Constructors (Default, Parameterized, Copy, Constructor Chaining)
17. `this` and `super` Keywords
18. Inheritance (Single, Multilevel, Hierarchical)
19. Why No Multiple Inheritance in Java
20. Polymorphism (Compile-time vs Runtime)
    - Method Overloading Rules
    - Method Overriding Rules
    - Covariant Return Types
21. Abstraction
22. Encapsulation
23. Interfaces (Default, Static, Private Methods)
24. Abstract Classes vs Interfaces
25. Inner Classes (Static, Non-static, Local, Anonymous)
26. `static` Keyword (Variable, Method, Block, Class)
27. `final` Keyword (Variable, Method, Class)
28. Object Class Methods (equals, hashCode, toString, clone, finalize)
29. equals() and hashCode() Contract
30. Immutable Classes (How to Create, Why String is Immutable)
31. Cloning (Shallow vs Deep Copy)
32. Marker Interfaces (Serializable, Cloneable)
33. Enums (Methods, Constructor, Singleton with Enum)
34. Access Modifiers (private, default, protected, public)
35. Packages and Imports

### Collections Framework
36. Collections Hierarchy & Overview
37. List Interface
    - ArrayList (Internal Working, Resizing)
    - LinkedList (Doubly Linked List Internals)
    - ArrayList vs LinkedList (When to Use)
    - Vector & Stack (Legacy)
38. Set Interface
    - HashSet (Internal Working via HashMap)
    - LinkedHashSet
    - TreeSet (Red-Black Tree)
    - EnumSet
39. Map Interface
    - HashMap (Internal Working, Hashing, Buckets, Treeification)
    - HashMap vs Hashtable vs ConcurrentHashMap
    - LinkedHashMap (Access Order, LRU Cache)
    - TreeMap (Sorted Map, NavigableMap)
    - WeakHashMap
    - EnumMap
40. Queue and Deque
    - PriorityQueue
    - ArrayDeque
    - BlockingQueue (ArrayBlockingQueue, LinkedBlockingQueue)
41. Iterators (Iterator, ListIterator, Spliterator)
42. Fail-Fast vs Fail-Safe Iterators
43. Comparable vs Comparator
44. Collections Utility Class (sort, unmodifiableList, synchronizedList)
45. Concurrent Collections (CopyOnWriteArrayList, ConcurrentSkipListMap)

### Exception Handling
46. Exception Hierarchy (Throwable, Error, Exception)
47. Try-Catch-Finally
48. Try-with-Resources (AutoCloseable)
49. Checked vs Unchecked Exceptions
50. Custom Exceptions
51. Exception Chaining
52. Exception Best Practices
53. Common Exceptions (NullPointerException, ClassCastException, StackOverflow, OutOfMemory)

### Multithreading & Concurrency
54. Thread Basics (Thread vs Runnable vs Callable)
55. Creating Threads
56. Thread Lifecycle & States
57. Thread Priority & Daemon Threads
58. Synchronization (synchronized keyword, method vs block)
59. `volatile` Keyword
60. Thread Communication (wait, notify, notifyAll)
61. Deadlock, Livelock, Starvation
62. Locks (ReentrantLock, ReadWriteLock, StampedLock)
63. Atomic Classes (AtomicInteger, AtomicReference, CAS)
64. Executor Framework & Thread Pools
    - FixedThreadPool, CachedThreadPool, ScheduledThreadPool
    - ThreadPoolExecutor Configuration
65. Callable and Future
66. CompletableFuture (thenApply, thenCompose, allOf, anyOf)
67. Fork/Join Framework
68. CountDownLatch, CyclicBarrier, Semaphore, Phaser
69. ThreadLocal
70. Concurrent Collections (ConcurrentHashMap Internals, CopyOnWriteArrayList)

### Java 8 Features
71. Lambda Expressions
72. Functional Interfaces (Predicate, Function, Consumer, Supplier, BiFunction)
73. Stream API
    - Intermediate vs Terminal Operations
    - Lazy Evaluation
    - Parallel Streams & Pitfalls
    - Collectors (groupingBy, partitioningBy, toMap, joining)
    - flatMap vs map
74. Optional (orElse, orElseGet, orElseThrow, map, flatMap)
75. Method References (Static, Instance, Constructor)
76. Default & Static Methods in Interfaces
77. Date and Time API (LocalDate, LocalDateTime, ZonedDateTime, Duration, Period)

### Java 11+ Features
78. Local Variable Type Inference (var)
79. HTTP Client API
80. New String Methods (isBlank, strip, lines, repeat)
81. Files.readString / writeString

### Java 17+ Features
82. Records
83. Sealed Classes & Interfaces
84. Pattern Matching for instanceof
85. Text Blocks
86. Switch Expressions

### Java 21+ Features
87. Virtual Threads (Project Loom)
88. Structured Concurrency
89. Pattern Matching for Switch
90. Sequenced Collections
91. String Templates (Preview)

### Generics
92. Generic Classes, Methods, Interfaces
93. Bounded Type Parameters (extends, super)
94. Wildcards (?, extends, super) — PECS Rule
95. Type Erasure
96. Generic Best Practices

### Annotations & Reflection
97. Built-in Annotations (@Override, @Deprecated, @SuppressWarnings, @FunctionalInterface)
98. Custom Annotations
99. Reflection API (Class, Method, Field introspection)
100. Reflection Use Cases & Performance Impact

### Serialization
101. Serializable Interface
102. serialVersionUID
103. transient Keyword
104. Externalizable Interface
105. Serialization Pitfalls & Best Practices

### File I/O and NIO
106. File Handling (File, Path, Files)
107. Byte Streams (InputStream, OutputStream)
108. Character Streams (Reader, Writer)
109. Buffered Streams
110. NIO (Channels, Buffers, Selectors)
111. NIO.2 (Path, Files, WatchService)

### JVM Internals & Memory
112. JVM Architecture (ClassLoader, Runtime Data Areas, Execution Engine)
113. ClassLoader (Bootstrap, Extension, Application, Custom)
114. Class Loading Mechanism (Loading, Linking, Initialization)
115. Memory Areas (Stack, Heap, Method Area, PC Register, Native Stack)
116. Heap Structure (Young Gen, Old Gen, Metaspace)
117. Garbage Collection Algorithms (Mark-Sweep, Mark-Compact, Copying)
118. Garbage Collectors (Serial, Parallel, CMS, G1, ZGC, Shenandoah)
119. GC Tuning & JVM Flags (-Xms, -Xmx, -XX:+UseG1GC)
120. Memory Leaks (Causes, Detection, Prevention)
121. Java Profiling Tools (JVisualVM, JConsole, JFR, async-profiler)

### JDBC and Database
122. JDBC Architecture & Drivers
123. Connection Management
124. Statement vs PreparedStatement vs CallableStatement
125. ResultSet Types & Concurrency
126. Transaction Management (ACID, Isolation Levels)
127. Connection Pooling (HikariCP)
128. Batch Processing

### Testing
129. JUnit 5 (Annotations, Assertions, Lifecycle)
130. Mockito (Mock, Spy, ArgumentCaptor, verify)
131. Test-Driven Development
132. Integration Testing

### Build Tools
133. Maven (POM, Lifecycle, Plugins, Profiles)
134. Gradle (Build Scripts, Tasks, Dependencies)
135. Dependency Management & Conflict Resolution

### Java Interview Essentials
136. Java Coding Standards & Naming Conventions
137. Effective Java Key Takeaways (Joshua Bloch)
138. Common Interview Pitfalls
    - String Pool Questions
    - HashMap Internal Working
    - equals/hashCode Contract
    - Immutable Class Creation
    - Thread Safety Patterns
    - ConcurrentModificationException
139. Java Performance Best Practices

---

## 🎯 Solution Architect Perspective

Java knowledge is crucial for:
- **Enterprise Applications**: Robust, scalable backend systems
- **Microservices**: Spring Boot, Spring Cloud ecosystem
- **Performance**: JVM tuning, memory management, GC optimization
- **Concurrency**: Thread-safe, high-performance applications
- **Integration**: JDBC, JMS, REST APIs
- **Maintainability**: Strong typing, OOP principles

---

← Previous: API Design & Management | Back to Main Index | Next: Spring Boot →
