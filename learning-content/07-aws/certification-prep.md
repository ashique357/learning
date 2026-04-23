# AWS Solutions Architect Associate (SAA-C03) — Certification Prep Guide

A structured preparation plan aligned with the [AWS Learning Path](./index.md).

---

## 📋 Exam Overview

- **Exam Code**: SAA-C03
- **Duration**: 130 minutes
- **Questions**: 65 (multiple choice & multiple response)
- **Passing Score**: 720 / 1000
- **Cost**: $150 USD

### Exam Domain Weights

| Domain | Weight |
|--------|--------|
| Designing Secure Architectures | 30% |
| Designing Resilient Architectures | 26% |
| Designing High-Performing Architectures | 24% |
| Designing Cost-Optimized Architectures | 20% |

---

## 🗓️ 12-Week Study Plan

### Phase 1: Build Foundation (Weeks 1–3)

Complete these prerequisite subjects from the learning path:
- [Linux/OS Fundamentals](../01-linux-os-fundamentals/index.md)
- [Basic Networking](../02-basic-networking/index.md) — VPC questions are heavily tested
- [Database](../03-database/index.md)
- [System Architecture](../04-system-architecture/index.md)

### Phase 2: AWS Deep Dive (Weeks 4–8)

Follow the [AWS index](./index.md) sequentially. For each service, focus on:
- What problem it solves
- When to use it vs alternatives
- Key limits and defaults
- Pricing model (on-demand, reserved, spot)

Use **AWS Free Tier** for hands-on practice with: EC2, S3, VPC, RDS, Lambda, DynamoDB, IAM.

### Phase 3: Comparisons & Whitepapers (Weeks 9–10)

- Master the **Service Comparison & Selection** section (topics 118–124)
- Read AWS Whitepapers (see resources below)
- Review the Well-Architected Framework (all 6 pillars)

### Phase 4: Practice Exams (Weeks 11–12)

- Take at least 3–4 full timed practice tests
- Review every wrong answer thoroughly
- Re-study weak areas identified from practice tests
- Re-read Shared Responsibility Model — it appears on every exam

### Timeline Summary

| Phase | Duration | Focus |
|-------|----------|-------|
| Foundation | Weeks 1–3 | Linux, Networking, DB, Architecture |
| AWS Deep Dive | Weeks 4–8 | All AWS services + hands-on |
| Comparisons & Whitepapers | Weeks 9–10 | Service selection, Well-Architected |
| Practice Exams | Weeks 11–12 | Timed tests + weak area review |

> 1–2 hours/day of consistent study is a realistic commitment.

---

## 🎯 Key Focus Areas

### Service Comparison (Exam Winners)

For every scenario question, you need to instantly know the right service:

| Scenario | Choose |
|----------|--------|
| Decoupling microservices | SQS |
| Ordered streaming + replay | Kinesis Data Streams |
| Managed Kafka | Amazon MSK |
| In-memory caching | ElastiCache (Redis / Memcached) |
| Fan-out notifications | SNS |
| Event routing with rules | EventBridge |
| Relational + managed | RDS |
| Relational + serverless + high availability | Aurora |
| Key-value / millisecond latency | DynamoDB |
| Short event-driven functions | Lambda |
| Long-running containers | ECS / EKS |
| Containers without managing servers | Fargate |
| Static content delivery | CloudFront |
| TCP/UDP global performance | Global Accelerator |
| Block storage for EC2 | EBS |
| Shared file system (Linux) | EFS |
| Shared file system (Windows) | FSx |
| Object storage | S3 |
| Large-scale data transfer (offline) | Snow Family |
| Database migration | DMS + SCT |

### Must-Know Concepts

- **Shared Responsibility Model** — always on the exam
- **IAM Policies** — identity-based vs resource-based
- **VPC Design** — public/private subnets, NAT Gateway, VPC Endpoints
- **S3** — storage classes, lifecycle policies, replication (CRR/SRR)
- **DR Strategies** — Backup & Restore → Pilot Light → Warm Standby → Active-Active (cost vs RTO)
- **Auto Scaling + ELB** — scaling policies, health checks, cross-zone
- **Encryption** — at rest (KMS, CloudHSM) vs in transit (TLS/SSL)
- **Well-Architected 6 Pillars** — Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability

---

## 📚 Recommended Resources

### Free Resources
- **AWS Skill Builder** — official AWS training courses
- **AWS Well-Architected Labs** — hands-on labs from AWS
- **AWS Documentation** — service FAQs are gold for exam prep

### Must-Read Whitepapers
- Well-Architected Framework
- Disaster Recovery of Workloads on AWS
- AWS Security Best Practices
- Architecting for the Cloud: Best Practices

### Practice Exams
- AWS official practice exam (Skill Builder)
- Tutorials Dojo practice exams (highly recommended by the community)

---

## 💡 Exam Day Tips

- **Time management**: ~2 minutes per question, don't get stuck
- **Eliminate first**: remove obviously wrong answers, then choose between remaining
- **Watch for keywords**:
  - "most cost-effective" → cheapest option that meets requirements
  - "least operational overhead" → managed/serverless services
  - "most secure" → encryption, least privilege, private subnets
  - "highest availability" → multi-AZ, multi-region
- **Flag and return**: mark difficult questions and revisit at the end
- **Read carefully**: the question often contains hints in the constraints

---

← Back to [AWS Index](./index.md) | Back to [Main Index](../../README.md)
