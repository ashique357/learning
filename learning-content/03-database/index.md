# Database

Master database concepts, design, optimization, and management for production systems.

## 📑 Topics

### Database Fundamentals
1. Database Basics and Types (Relational, Document, Key-Value, Graph, Column-Family, Time-Series)
2. Relational vs NoSQL (When to Use Which, Trade-offs)
3. ACID Properties (Atomicity, Consistency, Isolation, Durability)
4. CAP Theorem (Consistency, Availability, Partition Tolerance)
5. BASE Properties (Basically Available, Soft State, Eventually Consistent)

### SQL Fundamentals
6. SQL Basics (DDL, DML, DCL, TCL)
7. Data Types (Numeric, String, Date, Boolean, JSON, Array)
8. Tables and Schemas (CREATE, ALTER, DROP, TRUNCATE)
9. Primary and Foreign Keys (Composite Keys, Referential Integrity, Cascading)
10. Joins
    - Inner Join, Left Join, Right Join, Full Outer Join
    - Cross Join, Self Join
    - Join Performance Considerations
11. Subqueries and CTEs (Common Table Expressions)
    - Correlated vs Non-Correlated Subqueries
    - Recursive CTEs
12. Window Functions (ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD, NTILE, SUM OVER)
13. Aggregation (GROUP BY, HAVING, COUNT, SUM, AVG, MIN, MAX)
14. Views and Materialized Views (Refresh Strategies, Performance)
15. Stored Procedures and Functions (Input/Output Parameters, Cursors)
16. Triggers (BEFORE, AFTER, INSTEAD OF, Use Cases)

### SQL Practice Patterns
17. Common Interview Queries
    - Find Nth Highest Salary
    - Find Duplicates in a Table
    - Top N per Group
    - Running Totals and Cumulative Sums
    - Pivot and Unpivot
    - Date Range Queries
    - Hierarchical Queries (Manager-Employee)

### Database Engines
18. PostgreSQL (Features, Extensions, JSONB, Full-Text Search, Partitioning)
19. MySQL (InnoDB vs MyISAM, Replication, Group Replication)
20. PostgreSQL vs MySQL (Comparison, When to Use Which)
21. Oracle Database (Architecture, RAC, Partitioning)
22. SQL Server (T-SQL, Always On, Columnstore)

### Database Design
23. Normalization (1NF, 2NF, 3NF, BCNF, 4NF)
24. Denormalization (When and Why, Trade-offs)
25. ER Diagrams (Entities, Relationships, Cardinality)
26. Schema Design Patterns (Star Schema, Snowflake Schema, Galaxy Schema)
27. Data Modeling (Conceptual, Logical, Physical)

### Indexing and Performance
28. Index Types
    - B-Tree Index (Default, Range Queries)
    - Hash Index (Equality Lookups)
    - Bitmap Index (Low Cardinality)
    - GIN Index (Full-Text, JSONB)
    - GiST Index (Geometric, Range)
    - Composite Index (Column Order Matters)
    - Covering Index
    - Partial Index
29. Index Strategies (When to Index, When Not to Index)
30. Indexing Best Practices (Selectivity, Index-Only Scans)
31. Query Optimization
    - Reading Execution Plans (EXPLAIN, EXPLAIN ANALYZE)
    - Sequential Scan vs Index Scan vs Bitmap Scan
    - Join Algorithms (Nested Loop, Hash Join, Merge Join)
32. Query Performance Tuning (Slow Query Log, Query Rewriting)
33. Database Statistics (ANALYZE, Histogram, Cardinality Estimation)

### Transactions and Concurrency
34. Transactions (BEGIN, COMMIT, ROLLBACK, SAVEPOINT)
35. Isolation Levels
    - Read Uncommitted (Dirty Read)
    - Read Committed (Non-Repeatable Read)
    - Repeatable Read (Phantom Read)
    - Serializable (Full Isolation)
36. Locking Mechanisms (Row Lock, Table Lock, Advisory Lock, Optimistic vs Pessimistic)
37. Deadlocks (Detection, Prevention, Resolution)
38. MVCC (Multi-Version Concurrency Control) (PostgreSQL, MySQL InnoDB)

### NoSQL Databases
39. Document Databases (MongoDB)
    - Document Model, Collections, BSON
    - MongoDB Aggregation Pipeline (match, group, project, lookup, unwind)
    - MongoDB Indexing (Single, Compound, Text, Geospatial)
    - MongoDB Replication (Replica Sets, Elections)
    - MongoDB Sharding (Shard Key Selection, Chunks)
40. Key-Value Stores
    - Redis Deep-Dive
        - Data Structures (Strings, Hashes, Lists, Sets, Sorted Sets, Streams, HyperLogLog)
        - Redis Use Cases (Caching, Session Store, Rate Limiting, Leaderboard, Pub/Sub, Distributed Lock)
        - Redis Persistence (RDB Snapshots, AOF)
        - Redis Replication (Master-Replica)
        - Redis Sentinel (High Availability, Failover)
        - Redis Cluster (Sharding, Hash Slots)
        - Redis Eviction Policies (noeviction, allkeys-lru, volatile-lru, allkeys-random)
        - Redis Transactions (MULTI, EXEC, WATCH) & Pipelining
    - DynamoDB Deep-Dive
        - Partition Key, Sort Key, Composite Key
        - Global Secondary Index (GSI) vs Local Secondary Index (LSI)
        - Capacity Modes (On-Demand vs Provisioned)
        - DynamoDB Streams
        - DAX (DynamoDB Accelerator)
        - Single Table Design
41. Column-Family Stores (Cassandra, HBase)
    - Cassandra Architecture (Ring, Gossip, Consistent Hashing)
    - Cassandra Data Modeling (Partition Key, Clustering Key)
42. Graph Databases (Neo4j) (Nodes, Relationships, Cypher Query Language)
43. Time-Series Databases (InfluxDB, TimescaleDB, Use Cases)

### Replication and Scaling
44. Master-Slave Replication (Async, Semi-Sync, Sync)
45. Master-Master Replication (Conflict Resolution)
46. Read Replicas (Read Scaling, Replication Lag)
47. Sharding
    - Hash-Based Sharding
    - Range-Based Sharding
    - Directory-Based Sharding
    - Consistent Hashing
48. Partitioning Strategies (Range, List, Hash, Composite)
49. Horizontal vs Vertical Scaling (When to Use Which)

### Backup and Recovery
50. Backup Strategies (Full, Incremental, Differential, Logical vs Physical)
51. Point-in-Time Recovery (WAL, Binary Log)
52. Disaster Recovery (RPO, RTO, Failover)
53. High Availability (Active-Passive, Active-Active, Clustering)

### Database Administration
54. User Management and Permissions (GRANT, REVOKE, Roles)
55. Connection Pooling (PgBouncer, HikariCP, ProxySQL)
    - Pool Sizing Formula
    - Connection Pool vs Thread Pool
56. Connection Limits and Timeout Configuration
57. Database Monitoring (pg_stat_statements, slow_query_log, Performance Schema)
58. Performance Metrics (QPS, TPS, Cache Hit Ratio, Replication Lag)
59. Maintenance Tasks (VACUUM, REINDEX, Table Bloat)

### Advanced Topics
60. Database Caching Strategies (Query Cache, Application Cache, Read-Through, Write-Through)
61. Database Migration (Schema Versioning, Zero-Downtime Migration, Blue-Green)
62. Data Warehousing (ETL, ELT, Star Schema, Fact & Dimension Tables)
63. OLTP vs OLAP (Characteristics, Use Cases, Hybrid HTAP)
64. Database Security (Encryption at Rest, In Transit, Row-Level Security, Audit Logging)

### Interview Scenarios
65. How to Optimize a Slow Query
66. When to Use SQL vs NoSQL
67. How to Design a Schema for E-Commerce
68. Redis vs Memcached — When to Use Which
69. How to Handle Database Connection Pool Exhaustion

---

## 🎯 Solution Architect Perspective

Database knowledge is crucial for:
- **Data Architecture**: Choosing right database for use case
- **Performance**: Query optimization, indexing strategies
- **Scalability**: Sharding, replication, read replicas
- **Reliability**: Backup, recovery, high availability
- **Cost Optimization**: Right-sizing, reserved capacity
- **Security**: Encryption, access control, compliance

---

← Previous: Basic Networking | Back to Main Index | Next: System Architecture →
