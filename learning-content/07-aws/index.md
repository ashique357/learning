# AWS (Amazon Web Services)

Master AWS cloud services, architecture, and best practices for building scalable cloud solutions.

## 📑 Topics

### AWS Fundamentals
1. AWS Overview (Cloud Computing Models: IaaS, PaaS, SaaS)
2. AWS Global Infrastructure (Regions, AZs, Edge Locations, Local Zones, Wavelength)
3. Regions and Availability Zones (Multi-AZ, Region Selection Criteria)
4. AWS Account Management (Root Account, IAM, Organizations)
5. AWS Free Tier (Always Free, 12-Month Free, Trials)

### Identity and Access Management
6. IAM Basics (Users, Groups, Roles, Policies)
7. IAM Users, Groups, Roles
    - When to Use Roles vs Users
    - Cross-Account Access with Roles
    - Instance Profiles for EC2
8. IAM Policies (JSON Structure, Effect, Action, Resource, Condition)
    - Identity-Based vs Resource-Based Policies
    - Permission Boundaries
    - Policy Evaluation Logic
9. IAM Best Practices (Least Privilege, MFA, Password Policy, Access Keys Rotation)
10. AWS Organizations (SCPs, OUs, Consolidated Billing)
11. AWS SSO / IAM Identity Center (SAML, OIDC, Permission Sets)

### Compute Services
12. EC2 (Elastic Compute Cloud)
    - Instance Lifecycle (Pending, Running, Stopping, Terminated)
    - AMI (Amazon Machine Image, Custom AMI, AMI Sharing)
    - User Data (Bootstrap Scripts)
    - Metadata (Instance Metadata Service, IMDSv2)
    - Placement Groups (Cluster, Spread, Partition)
13. EC2 Instance Types (General, Compute, Memory, Storage, Accelerated)
14. EC2 Pricing Models (On-Demand, Reserved, Savings Plans, Spot, Dedicated)
    - Spot Instances (Spot Fleet, Interruption Handling, Use Cases)
15. Auto Scaling Groups
    - Launch Templates vs Launch Configurations
    - Scaling Policies (Target Tracking, Step, Simple, Scheduled, Predictive)
    - Cooldown Period, Warm Pool
16. Elastic Load Balancing
    - ALB (Layer 7, Path/Host Routing, Target Groups, Sticky Sessions)
    - NLB (Layer 4, Static IP, Ultra-Low Latency, TLS Termination)
    - CLB (Legacy, Layer 4/7)
    - Cross-Zone Load Balancing
    - Connection Draining / Deregistration Delay
17. Lambda
    - Event Sources (API Gateway, S3, SQS, DynamoDB Streams, EventBridge)
    - Cold Start (Causes, Mitigation, Provisioned Concurrency)
    - Concurrency (Reserved, Provisioned, Burst)
    - Limits (Timeout 15min, Memory 10GB, Package Size)
    - Lambda@Edge and CloudFront Functions
18. Lambda Layers (Shared Libraries, Runtime Dependencies)
19. ECS (Elastic Container Service)
    - Task Definitions (Container Definitions, CPU, Memory, Port Mappings)
    - Services (Desired Count, Load Balancer Integration)
    - Service Discovery (Cloud Map, DNS)
    - ECS Exec (Debugging)
20. EKS (Elastic Kubernetes Service)
    - Managed Node Groups, Self-Managed, Fargate Profiles
    - IAM Roles for Service Accounts (IRSA)
    - ALB Ingress Controller
21. ECS vs EKS (Comparison, When to Use Which)
22. Fargate (Serverless Containers, Task Sizing, Use Cases)
23. AWS Batch (Job Definitions, Job Queues, Compute Environments)

### Storage Services
24. S3 (Simple Storage Service)
    - Buckets, Objects, Keys, Versioning
    - Consistency Model (Strong Read-After-Write)
    - Multipart Upload, Transfer Acceleration
    - S3 Event Notifications (Lambda, SQS, SNS, EventBridge)
    - Pre-Signed URLs
25. S3 Storage Classes (Standard, IA, One Zone-IA, Glacier Instant/Flexible/Deep, Intelligent-Tiering)
26. S3 Security (Bucket Policies, ACLs, Block Public Access, Encryption SSE-S3/SSE-KMS/SSE-C)
27. EBS (Elastic Block Store)
    - Volume Types (gp3, gp2, io2, io1, st1, sc1)
    - Snapshots, Encryption, Multi-Attach
28. EFS (Elastic File System) (NFS, Mount Targets, Performance Modes, Throughput Modes)
29. FSx (Windows File Server, Lustre, NetApp ONTAP, OpenZFS)
30. Storage Gateway (File, Volume, Tape Gateway)
31. Glacier (Archive Storage, Retrieval Options, Vault Lock)

### Database Services
32. RDS (Relational Database Service)
    - Supported Engines (MySQL, PostgreSQL, MariaDB, Oracle, SQL Server)
    - Multi-AZ (Synchronous Standby, Automatic Failover)
    - Read Replicas (Async Replication, Cross-Region)
    - RDS Proxy (Connection Pooling, IAM Auth)
33. Aurora
    - Architecture (6 Copies, 3 AZs, Shared Storage)
    - Aurora Replicas (Up to 15, Auto-Failover)
    - Aurora Serverless v2 (Auto-Scaling, ACU)
    - Aurora Global Database (Cross-Region, <1s Replication)
34. DynamoDB
    - Partition Key, Sort Key, Composite Key
    - GSI vs LSI (Differences, Limits, Projections)
    - Capacity Modes (On-Demand vs Provisioned, Auto-Scaling)
    - DynamoDB Streams (Change Data Capture, Lambda Triggers)
    - DAX (In-Memory Cache, Microsecond Reads)
    - Single Table Design (Access Patterns, Overloaded Keys)
    - TTL (Auto-Expiry)
35. ElastiCache
    - Redis (Cluster Mode, Replication, Persistence, Pub/Sub)
    - Memcached (Multi-Threaded, Simple Caching)
    - Redis vs Memcached (When to Use Which)
36. Redshift (Columnar, MPP, Spectrum, Serverless)
37. DocumentDB (MongoDB Compatible, Managed)
38. Neptune (Graph Database, Gremlin, SPARQL)

### Data & Analytics
39. AWS Glue (ETL, Crawlers, Data Catalog, Glue Studio)
40. AWS Athena (Serverless SQL on S3, Presto, Partitioning)
41. EMR (Elastic MapReduce) (Hadoop, Spark, Hive, Presto)
42. Kinesis Data Streams (Shards, Producers, Consumers, Retention)
43. Kinesis Data Firehose (Near Real-Time Delivery, S3, Redshift, OpenSearch)
44. Kinesis Data Analytics (SQL, Apache Flink)
45. Amazon OpenSearch Service (Search, Log Analytics, Dashboards)
46. Amazon MSK (Managed Kafka, Serverless, Connect)

### Networking
47. VPC (Virtual Private Cloud) (CIDR, Tenancy, Default vs Custom)
48. Subnets (Public, Private, Subnet Sizing, AZ Mapping)
49. Internet Gateway (Public Internet Access, One per VPC)
50. NAT Gateway (Private Subnet Internet Access, AZ-Specific, Cost)
51. Route Tables (Main, Custom, Route Priority, Longest Prefix Match)
52. Security Groups (Stateful, Inbound/Outbound, Allow Only, Chaining)
53. Network ACLs (Stateless, Allow/Deny, Rule Numbers, Ephemeral Ports)
54. VPC Peering (Non-Transitive, Cross-Region, Cross-Account)
55. Transit Gateway (Hub-and-Spoke, Transitive Routing, Multi-VPC)
56. Direct Connect (Dedicated Connection, 1Gbps/10Gbps, LAG)
57. Site-to-Site VPN (IPSec, Virtual Private Gateway, Customer Gateway)
58. Direct Connect + VPN Failover (Hybrid Connectivity)
59. VPC Endpoints
    - Gateway Endpoints (S3, DynamoDB, Free)
    - Interface Endpoints (PrivateLink, ENI, Cost)
60. Elastic IP & ENI (Static IP, Multiple IPs, Failover)
61. VPC Flow Logs (Capture Traffic, CloudWatch, S3, Troubleshooting)
62. Route 53
    - Routing Policies (Simple, Weighted, Latency, Failover, Geolocation, Geoproximity, Multi-Value)
    - Health Checks (Endpoint, Calculated, CloudWatch Alarm)
    - DNS Record Types (A, AAAA, CNAME, Alias)
63. CloudFront (CDN, Edge Locations, Origin, Behaviors, Cache Policy, OAC)
64. Global Accelerator (Anycast IP, TCP/UDP, Endpoint Groups)

### Application Services
65. API Gateway (REST, HTTP, WebSocket, Stages, Throttling, Caching, Usage Plans)
66. SQS (Simple Queue Service)
    - Standard vs FIFO (Ordering, Deduplication)
    - Visibility Timeout, Dead Letter Queue, Long Polling
    - Message Retention, Batch Operations
67. SNS (Simple Notification Service) (Topics, Subscriptions, Fan-Out, Filtering)
68. EventBridge (Event Bus, Rules, Targets, Schema Registry, Scheduler)
69. Step Functions (State Machine, ASL, Standard vs Express, Error Handling)
70. Step Functions Patterns (Sequential, Parallel, Map, Choice, Wait)
71. AppSync (Managed GraphQL, Resolvers, Real-Time Subscriptions)

### Monitoring and Management
72. CloudWatch (Metrics, Namespaces, Dimensions, Custom Metrics)
73. CloudWatch Logs (Log Groups, Log Streams, Metric Filters, Insights)
74. CloudWatch Alarms (Threshold, Anomaly Detection, Composite Alarms, Actions)
75. CloudTrail (API Logging, Management Events, Data Events, Insights)
76. AWS Config (Configuration Recording, Rules, Remediation, Compliance)
77. Systems Manager (Parameter Store, Session Manager, Patch Manager, Run Command)
78. X-Ray (Distributed Tracing, Service Map, Segments, Subsegments, Annotations)

### Security
79. AWS Shared Responsibility Model (AWS vs Customer Responsibilities)
80. AWS Security Best Practices (Defense in Depth, Least Privilege)
81. KMS (Key Management Service) (CMK, Envelope Encryption, Key Rotation, Key Policies)
82. CloudHSM (Dedicated HSM, FIPS 140-2 Level 3)
83. KMS vs CloudHSM (Comparison, When to Use Which)
84. Secrets Manager (Rotation, RDS Integration, Cross-Account)
85. WAF (Web Application Firewall) (Rules, Web ACL, Rate Limiting, Managed Rules)
86. Shield (DDoS Protection) (Standard vs Advanced, Response Team)
87. GuardDuty (Threat Detection, Findings, Data Sources)
88. Security Hub (Aggregated Findings, Standards, Integrations)
89. Inspector (Vulnerability Scanning, EC2, ECR, Lambda)
90. Macie (Data Classification, PII Detection, S3 Scanning)
91. STS (Security Token Service) & Federation (AssumeRole, SAML, Web Identity)
92. Cognito (User Pools, Identity Pools, Social Login, MFA)

### Migration & Transfer
93. AWS Migration Strategies (6 R's: Rehost, Replatform, Refactor, Repurchase, Retire, Retain)
94. AWS Migration Hub (Tracking, Assessment)
95. Database Migration Service (DMS) (Homogeneous, Heterogeneous, CDC)
96. Schema Conversion Tool (SCT) (Schema Translation, Assessment Report)
97. Application Discovery Service (Agent-Based, Agentless)
98. Snow Family (Snowcone 8TB, Snowball Edge 80TB, Snowmobile 100PB)
99. DataSync (On-Premise to AWS, Scheduled, Encryption)
100. AWS Transfer Family (SFTP, FTPS, FTP to S3/EFS)
101. AWS Backup (Centralized, Cross-Region, Cross-Account, Vault Lock)

### DevOps and CI/CD
102. CodeCommit (Git Repository, IAM Auth)
103. CodeBuild (Build Service, buildspec.yml, Docker Support)
104. CodeDeploy (EC2, ECS, Lambda, Deployment Configurations)
105. CodePipeline (Orchestration, Stages, Actions, Artifacts)
106. CloudFormation (IaC, Templates, Stacks, Change Sets, Drift Detection)
107. CDK (Cloud Development Kit) (TypeScript, Python, Constructs, Synth)
108. Elastic Beanstalk (PaaS, Environments, Deployment Policies)

### Cost Management
109. Cost Explorer (Visualization, Forecasting, Filtering)
110. Budgets (Cost, Usage, Reservation, Alerts)
111. Cost Allocation Tags (AWS-Generated, User-Defined)
112. Reserved Instances (Standard, Convertible, Scheduled)
113. Savings Plans (Compute, EC2, SageMaker)
114. Compute Optimizer (Right-Sizing Recommendations)

### S3 Deep Dive
115. S3 Lifecycle Policies (Transition, Expiration, Abort Incomplete Multipart)
116. S3 Replication (CRR Cross-Region, SRR Same-Region, Replication Rules)
117. S3 Event Notifications (Lambda, SQS, SNS, EventBridge)
118. S3 Select & Glacier Select (Server-Side Filtering, SQL Expressions)

### Service Comparison & Selection
119. SQS vs SNS vs Kinesis vs EventBridge vs MSK
120. RDS vs Aurora vs DynamoDB
121. ECS vs EKS vs Lambda
122. S3 vs EBS vs EFS
123. CloudFront vs Global Accelerator
124. Security Groups vs NACLs
125. NAT Gateway vs NAT Instance
126. Gateway Endpoint vs Interface Endpoint

### Advanced Topics
127. Well-Architected Framework
    - Operational Excellence
    - Security
    - Reliability
    - Performance Efficiency
    - Cost Optimization
    - Sustainability
128. Disaster Recovery Strategies (Backup & Restore, Pilot Light, Warm Standby, Active-Active)
129. Multi-Region Architecture (Data Replication, Failover, Latency)
130. Hybrid Cloud (Direct Connect, VPN, Outposts, Storage Gateway)
131. Serverless Architecture (Lambda, API Gateway, DynamoDB, S3, Step Functions)
132. AWS Control Tower & Landing Zones (Guardrails, Account Factory)

### Architecture Scenarios
133. 3-Tier Web Application on AWS
134. Serverless REST API (API Gateway + Lambda + DynamoDB)
135. Real-Time Data Pipeline (Kinesis + Lambda + S3 + Athena)
136. Microservices on ECS/EKS with Service Discovery
137. Static Website with CloudFront and S3
138. Hybrid Connectivity (On-Premise to AWS)

---

## 🎯 Solution Architect Perspective

AWS knowledge is crucial for:
- **Cloud Architecture**: Designing scalable, reliable cloud solutions
- **Cost Optimization**: Right-sizing, reserved capacity, spot instances
- **Security**: IAM, encryption, compliance, network security
- **High Availability**: Multi-AZ, multi-region, disaster recovery
- **Performance**: Service selection, caching, CDN
- **Migration**: On-premise to cloud, cloud-to-cloud
- **Service Selection**: Choosing the right service for the right scenario

---

← Previous: Kubernetes | Back to Main Index | Next: CI/CD →
