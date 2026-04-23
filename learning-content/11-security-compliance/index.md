# Security & Compliance

Master security principles, best practices, and compliance requirements for enterprise systems.

## 📑 Topics

### Security Fundamentals
1. Security Principles (Defense in Depth, Least Privilege, Separation of Duties)
2. CIA Triad (Confidentiality, Integrity, Availability)
3. Defense in Depth (Multiple Layers, Network, Application, Data)
4. Least Privilege (Minimal Access, Just-In-Time, Just-Enough)
5. Zero Trust Architecture (Never Trust, Always Verify, Microsegmentation)
6. Security by Design (Shift-Left, Secure SDLC, Threat Modeling Early)

### Authentication & Authorization
7. Authentication Basics (Something You Know, Have, Are)
8. Multi-Factor Authentication (MFA) (TOTP, SMS, Hardware Keys, Push)
9. Single Sign-On (SSO) (Centralized Auth, Federation, Identity Provider)
10. OAuth 2.0
    - Grant Types (Authorization Code, Client Credentials, PKCE, Implicit, Resource Owner)
    - Access Token, Refresh Token, Scopes
    - OAuth 2.0 Flow Step-by-Step
11. OpenID Connect (OIDC) (ID Token, UserInfo, OAuth 2.0 Extension)
12. SAML (Security Assertion Markup Language) (IdP, SP, Assertions, SSO Flow)
13. JWT (JSON Web Tokens)
    - Structure (Header, Payload, Signature)
    - Signing (HS256, RS256)
    - Validation, Expiry, Refresh Strategy
    - JWT vs Session-Based Auth
14. API Keys (Usage, Rotation, Rate Limiting, Limitations)
15. Authorization Models
    - RBAC (Role-Based Access Control, Roles, Permissions)
    - ABAC (Attribute-Based Access Control, Policies, Conditions)
    - RBAC vs ABAC (When to Use Which)

### Encryption
16. Encryption Basics (Plaintext, Ciphertext, Keys, Algorithms)
17. Symmetric vs Asymmetric Encryption
    - Symmetric (AES-256, Fast, Shared Key)
    - Asymmetric (RSA, ECC, Public/Private Key Pair)
    - Hybrid Encryption (TLS Uses Both)
18. Encryption at Rest (Database, Disk, S3, Transparent Data Encryption)
19. Encryption in Transit (TLS, mTLS, VPN)
20. TLS/SSL
    - TLS Handshake Step-by-Step
    - TLS 1.2 vs TLS 1.3
    - Certificate Chain (Root CA, Intermediate CA, Leaf)
21. Certificate Management (Let's Encrypt, ACM, Renewal, Revocation)
22. Key Management (Key Rotation, Key Hierarchy, Envelope Encryption)
23. HSM (Hardware Security Module) (FIPS 140-2, Dedicated Hardware)

### Network Security
24. Firewall Basics (Stateful vs Stateless, Rules, Zones)
25. Network Segmentation (DMZ, Microsegmentation, VLANs)
26. VPN (Site-to-Site, Client VPN, IPSec, WireGuard)
27. DDoS Protection (Volumetric, Protocol, Application Layer, Mitigation)
28. WAF (Web Application Firewall) (Rules, Rate Limiting, Bot Protection, OWASP Rules)
29. IDS/IPS (Intrusion Detection vs Prevention, Signature vs Anomaly)
30. Security Groups (Stateful, Cloud, Allow Rules)
31. Network ACLs (Stateless, Allow/Deny, Subnet Level)

### Application Security
32. OWASP Top 10
    - Injection (SQL, NoSQL, OS Command, LDAP)
    - Broken Authentication
    - Sensitive Data Exposure
    - XML External Entities (XXE)
    - Broken Access Control
    - Security Misconfiguration
    - Cross-Site Scripting (XSS)
    - Insecure Deserialization
    - Using Components with Known Vulnerabilities
    - Insufficient Logging & Monitoring
33. SQL Injection (Types, Prevention, Parameterized Queries, ORM)
34. Cross-Site Scripting (XSS) (Stored, Reflected, DOM-Based, Prevention)
35. Cross-Site Request Forgery (CSRF) (Token-Based Prevention, SameSite Cookie)
36. Input Validation (Whitelist, Sanitization, Encoding)
37. Secure Coding Practices (Error Handling, Logging, Session Management)
38. API Security (Authentication, Rate Limiting, Input Validation, CORS)
39. Rate Limiting (Token Bucket, Sliding Window, Per-User, Per-IP)

### Cloud Security
40. Cloud Security Basics (Shared Responsibility, Cloud-Native Security)
41. Shared Responsibility Model (AWS, Azure, GCP — Provider vs Customer)
42. IAM Best Practices (Least Privilege, MFA, Roles, Policy Conditions)
43. S3 Security (Bucket Policies, Block Public Access, Encryption, Access Logs)
44. VPC Security (Security Groups, NACLs, Flow Logs, Private Subnets)
45. Cloud Security Posture Management (CSPM) (Misconfigurations, Compliance)

### Secrets Management
46. Secrets Management Basics (Why, What to Protect, Rotation)
47. HashiCorp Vault (Secrets Engine, Auth Methods, Policies, Dynamic Secrets)
48. AWS Secrets Manager (Rotation, RDS Integration, Cross-Account)
49. Azure Key Vault (Keys, Secrets, Certificates)
50. Secrets in CI/CD (Environment Variables, Sealed Secrets, OIDC)

### Security Testing
51. Security Testing Overview (Shift-Left, Continuous Security)
52. SAST (Static Application Security Testing) (Source Code Analysis, SonarQube, Checkmarx)
53. DAST (Dynamic Application Security Testing) (Runtime Testing, OWASP ZAP, Burp Suite)
54. Penetration Testing (Black Box, White Box, Grey Box, Scope)
55. Vulnerability Scanning (CVE, NVD, Nessus, Qualys)
56. Dependency Scanning (SCA, Snyk, Dependabot, OWASP Dependency-Check)

### DevSecOps
57. DevSecOps Basics (Security as Code, Automation, Culture)
58. Shift-Left Security (Early Detection, Developer Tooling)
59. Security in CI/CD Pipelines (SAST, DAST, SCA, Image Scanning Gates)
60. Secrets Scanning (git-secrets, TruffleHog, Gitleaks)
61. Container Image Scanning (Trivy, Snyk, Docker Scout, Admission Control)
62. Compliance Automation (Policy as Code, OPA, Sentinel, AWS Config Rules)
63. Supply Chain Security (SBOM, Sigstore, Cosign, SLSA Framework)

### Compliance
64. Compliance Basics (Regulatory, Industry, Internal Standards)
65. GDPR (Data Protection, Right to Erasure, Consent, DPO)
66. HIPAA (PHI, Safeguards, BAA, Audit Controls)
67. PCI DSS (Cardholder Data, 12 Requirements, SAQ, QSA)
68. SOC 2 (Trust Service Criteria, Type I vs Type II, Audit)
69. ISO 27001 (ISMS, Risk Assessment, Controls, Certification)

### Incident Response
70. Incident Response Plan (Preparation, Detection, Containment, Eradication, Recovery, Lessons)
71. Security Monitoring (Real-Time, Log Analysis, Anomaly Detection)
72. SIEM (Security Information and Event Management) (Splunk, ELK, Sentinel, Correlation)
73. Threat Detection (IOC, IOA, Threat Intelligence, MITRE ATT&CK)
74. Forensics (Evidence Collection, Chain of Custody, Root Cause)

### Data Security
75. Data Classification (Public, Internal, Confidential, Restricted)
76. Data Loss Prevention (DLP) (Endpoint, Network, Cloud, Policies)
77. Data Masking (Static, Dynamic, Tokenization)
78. Backup Security (Encryption, Immutable Backups, Access Control)
79. Privacy by Design (Data Minimization, Purpose Limitation, Anonymization)

### Advanced Topics
80. Threat Modeling (STRIDE, DREAD, Attack Trees, Data Flow Diagrams)
81. Security Metrics (MTTD, MTTR, Vulnerability Age, Patch Compliance)
82. Security Governance (Policies, Standards, Procedures, Risk Management)

### Interview Scenarios
83. How Does OAuth 2.0 Work — Explain the Flow
84. JWT vs Session-Based Authentication — Trade-offs
85. How to Secure a REST API
86. OWASP Top 10 — Explain Top 5 with Prevention
87. How to Implement Zero Trust in a Microservices Architecture

---

## 🎯 Solution Architect Perspective

Security & Compliance is crucial for:
- **Risk Management**: Protect assets and data
- **Trust**: Build customer confidence
- **Compliance**: Meet regulatory requirements
- **Business Continuity**: Prevent and recover from incidents
- **Reputation**: Avoid security breaches
- **Cost Avoidance**: Prevent expensive security incidents

---

← Previous: Monitoring & Observability | Back to Main Index | Next: Message Queues & Streaming →
