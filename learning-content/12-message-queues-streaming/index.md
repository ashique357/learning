# Message Queues & Event Streaming

Master asynchronous communication, message queues, and event streaming for distributed systems.

## 📑 Topics

### Messaging Fundamentals
1. What is Message Queuing (Decoupling, Buffering, Async Communication)
2. Synchronous vs Asynchronous Communication (Trade-offs, When to Use)
3. Message Queue Benefits (Decoupling, Scalability, Reliability, Load Leveling)
4. Message Queue Patterns (Queue, Topic, Exchange)
5. Delivery Guarantees
    - At-Most-Once (Fire and Forget, May Lose Messages)
    - At-Least-Once (Retry, May Duplicate)
    - Exactly-Once (Idempotency + At-Least-Once)

### Message Queue Concepts
6. Producers and Consumers (Publisher, Subscriber, Consumer Groups)
7. Topics and Queues (Point-to-Point vs Pub/Sub)
8. Message Routing (Direct, Topic-Based, Content-Based)
9. Dead Letter Queues (Failed Messages, Retry Exhaustion, Monitoring)
10. Message Ordering (FIFO, Partition-Level, Global vs Partial)
11. Message Persistence (Disk, Replication, Durability)
12. Message TTL (Time-to-Live, Expiry, Cleanup)

### Messaging Patterns
13. Point-to-Point (Single Consumer, Work Queue)
14. Publish-Subscribe (Multiple Consumers, Fan-Out)
15. Request-Reply (Correlation ID, Reply Queue, Timeout)
16. Fan-Out (One Message to Many Consumers)
17. Fan-In (Many Producers to One Consumer)
18. Priority Queue (Message Priority, Ordering)
19. Competing Consumers (Parallel Processing, Load Distribution)

### RabbitMQ
20. RabbitMQ Basics (AMQP Protocol, Broker, Virtual Hosts)
21. RabbitMQ Architecture (Connection, Channel, Exchange, Queue, Binding)
22. Exchanges
    - Direct Exchange (Routing Key Match)
    - Topic Exchange (Pattern Matching, Wildcards)
    - Fanout Exchange (Broadcast to All Queues)
    - Headers Exchange (Header Matching)
23. Queues and Bindings (Durable, Exclusive, Auto-Delete, Arguments)
24. RabbitMQ Routing (Routing Key, Binding Key, Exchange-Queue Binding)
25. RabbitMQ Acknowledgments (Manual ACK, Auto ACK, NACK, Reject, Prefetch)
26. RabbitMQ Clustering (Mirrored Queues, Quorum Queues, Node Types)
27. RabbitMQ High Availability (Quorum Queues, Federation, Shovel)

### Apache Kafka
28. Kafka Basics (Distributed Log, Append-Only, Immutable)
29. Kafka Architecture (Broker, Cluster, ZooKeeper/KRaft, Controller)
30. Kafka Topics and Partitions
    - Partition Strategy (Key-Based, Round-Robin)
    - Partition Count Selection
    - Partition Rebalancing
31. Kafka Producers
    - Acknowledgments (acks=0, acks=1, acks=all)
    - Partitioner (Key Hash, Custom)
    - Batching, Compression, Retries
32. Kafka Consumers
    - Consumer Groups (Partition Assignment, Rebalancing)
    - Offset Management (Auto-Commit, Manual Commit)
    - Consumer Lag (Monitoring, Alerting)
33. Kafka Replication (Leader, Follower, ISR, Min ISR)
34. Kafka Streams (Stateless, Stateful, KTable, KStream, Windowing)
35. Kafka Connect (Source, Sink, Connectors, Transforms, Converters)
36. Kafka Exactly-Once Semantics (Idempotent Producer, Transactional API)
37. Kafka Performance Tuning (Batch Size, Linger, Compression, Partitions)

### AWS Messaging Services
38. Amazon SQS
    - Standard (Best-Effort Ordering, At-Least-Once)
    - FIFO (Exactly-Once, Message Group ID, Deduplication ID)
    - Visibility Timeout, Dead Letter Queue, Long Polling
    - Batch Operations, Message Retention (1min-14days)
39. Amazon SNS (Topics, Subscriptions, Fan-Out, Message Filtering, FIFO Topics)
40. SQS + SNS Fan-Out Pattern (SNS → Multiple SQS Queues)
41. Amazon EventBridge (Event Bus, Rules, Targets, Schema Registry, Scheduler)
42. Amazon Kinesis
    - Kinesis Data Streams (Shards, Producers, Consumers, Enhanced Fan-Out)
    - Kinesis Data Firehose (Near Real-Time, S3, Redshift, OpenSearch)
43. Amazon MSK (Managed Kafka, Serverless, Connect, IAM Auth)

### Azure Messaging Services
44. Azure Service Bus (Queues, Topics, Sessions, Dead Letter)
45. Azure Event Hubs (Kafka Compatible, Partitions, Consumer Groups)
46. Azure Event Grid (Event-Driven, Reactive, Push Model)

### Event Streaming
47. Event Streaming Basics (Continuous Flow, Replay, Time-Based)
48. Stream Processing (Stateless, Stateful, Windowing, Aggregation)
49. Change Data Capture (CDC) (Debezium, Database Log, Outbox Pattern)

### Stream Processing Frameworks
50. Apache Flink (Stateful, Exactly-Once, Event Time, Watermarks)
51. Apache Spark Streaming (Micro-Batch, Structured Streaming)
52. Kafka Streams (Lightweight, No Separate Cluster, KTable)
53. AWS Kinesis Analytics (SQL, Apache Flink, Real-Time)

### Event-Driven Architecture
54. Event-Driven Architecture Basics (Loose Coupling, Reactive)
55. Event Notification (Lightweight, Trigger Action)
56. Event-Carried State Transfer (Full State in Event, No Callback)
57. Event Collaboration (Multiple Services React to Same Event)

### Performance & Scalability
58. Message Queue Scaling (Partitions, Consumer Groups, Horizontal)
59. Partitioning Strategies (Key-Based, Round-Robin, Custom)
60. Throughput Optimization (Batching, Compression, Async Producers)
61. Latency Optimization (Prefetch, Consumer Tuning, Partition Count)
62. Backpressure Handling (Flow Control, Buffering, Rate Limiting)

### Reliability & Monitoring
63. Message Queue Reliability (Replication, Persistence, Acknowledgments)
64. Error Handling (Retry, Dead Letter, Circuit Breaker)
65. Retry Strategies (Fixed, Exponential Backoff, Max Retries)
66. Monitoring Message Queues (Consumer Lag, Queue Depth, Throughput)
67. Alerting (Lag Threshold, Queue Buildup, Error Rate)

### Advanced Topics
68. Schema Registry (Avro, Protobuf, JSON Schema, Compatibility Modes)
69. Message Serialization (Avro vs Protobuf vs JSON, Schema Evolution)
70. Idempotency (Idempotency Keys, Deduplication, Exactly-Once Processing)
71. Message Deduplication (Content-Based, ID-Based, Time Window)
72. Multi-Region Messaging (Cross-Region Replication, Active-Active)
73. Outbox Pattern (Transactional Outbox, Polling Publisher, CDC)

### Interview Scenarios
74. Kafka vs RabbitMQ — When to Use Which
75. Kafka vs SQS vs Kinesis — Comparison
76. How to Handle Message Ordering in Distributed Systems
77. How to Achieve Exactly-Once Processing
78. Design a Notification System Using Message Queues
79. How to Handle Poison Messages

---

## 🎯 Solution Architect Perspective

Message Queues & Streaming is crucial for:
- **Decoupling**: Independent service scaling and deployment
- **Reliability**: Asynchronous processing, retry mechanisms
- **Scalability**: Handle traffic spikes, load leveling
- **Real-Time Processing**: Stream analytics, event-driven workflows
- **Integration**: Connect heterogeneous systems
- **Resilience**: Buffer between services, fault tolerance

---

← Previous: Security & Compliance | Back to Main Index | Next: API Design & Management →
