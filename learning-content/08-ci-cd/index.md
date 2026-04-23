# CI/CD (Continuous Integration / Continuous Delivery)

Master CI/CD pipelines, automation, and DevOps practices for efficient software delivery.

## 📑 Topics

### CI/CD Fundamentals
1. What is CI/CD (Continuous Integration, Delivery, Deployment)
2. Continuous Integration (Frequent Merges, Automated Builds, Fast Feedback)
3. Continuous Delivery vs Deployment (Manual vs Automatic Release)
4. DevOps Culture (Collaboration, Shared Responsibility, Blameless Postmortems)
5. CI/CD Benefits (Speed, Quality, Reliability, Developer Productivity)

### Version Control with Git
6. Git Basics (Distributed VCS, Snapshots vs Diffs)
7. Git Installation and Configuration (git config, SSH Keys)
8. Git Repository Initialization (git init, git clone)
9. Git Add, Commit, Push, Pull (Staging Area, Commit History)
10. Git Status and Log (git status, git log --oneline --graph)
11. Git Branching (Create, Switch, Delete, List)
12. Git Merging (Fast-Forward, 3-Way Merge, Merge Commit)
13. Git Rebase (Interactive Rebase, Squash, When to Rebase vs Merge)
14. Git Cherry-Pick (Selective Commit Application)
15. Git Stash (Save, Pop, List, Drop, Apply)
16. Git Tags (Lightweight, Annotated, Release Tagging)
17. Git Reset and Revert
    - Reset (--soft, --mixed, --hard)
    - Revert (Safe Undo, New Commit)
    - Reset vs Revert (When to Use Which)
18. Git Workflows
    - GitFlow (Feature, Develop, Release, Hotfix, Main)
    - GitHub Flow (Feature Branch + PR + Main)
    - Trunk-Based Development (Short-Lived Branches, Feature Flags)
19. Branching Strategies (Environment Branches, Release Branches)
20. Pull Requests and Code Review (Review Process, Approval, CI Checks)
21. Git Hooks (Pre-Commit, Pre-Push, Commit-Msg, Server-Side Hooks)
22. Git Submodules (Nested Repositories, Version Pinning)
23. Git Subtrees (Alternative to Submodules, Merge Strategy)
24. Resolving Merge Conflicts (Manual Resolution, Tools, Prevention)
25. Git Best Practices (Commit Messages, Atomic Commits, Branch Naming)
26. GitHub (Actions, Issues, Projects, Packages, Pages)
27. GitLab (CI/CD, Merge Requests, Container Registry, Auto DevOps)
28. Bitbucket (Pipelines, Pull Requests, Jira Integration)
29. Git LFS (Large File Storage) (Track, Fetch, Prune)
30. Monorepo vs Polyrepo (Trade-offs, Tooling, When to Use)

### Build Automation
31. Build Tools Overview (Maven, Gradle, npm, pip, Make)
32. Build Scripts (Reproducible Builds, Build Stages)
33. Dependency Management (Lock Files, Version Ranges, Vulnerability Scanning)
34. Artifact Management (Nexus, Artifactory, S3, ECR)
35. Build Optimization (Caching, Incremental Builds, Parallel Builds)

### Testing Automation
36. Testing Pyramid (Unit > Integration > E2E, Cost vs Confidence)
37. Unit Testing (Fast, Isolated, Mocking)
38. Integration Testing (Database, API, Service Integration)
39. End-to-End Testing (Selenium, Cypress, Playwright)
40. Test Coverage (Line, Branch, Mutation Testing, Coverage Thresholds)
41. Test Automation Best Practices (Deterministic, Fast, Independent)

### CI/CD Pipeline
42. Pipeline Basics (Trigger, Stages, Jobs, Steps, Artifacts)
43. Pipeline Stages (Build, Test, Scan, Deploy, Verify)
44. Pipeline as Code (Jenkinsfile, .gitlab-ci.yml, .github/workflows)
45. Parallel Execution (Matrix Builds, Fan-Out/Fan-In)
46. Pipeline Optimization (Caching, Conditional Stages, Skip Unchanged)
47. Pipeline Security (Secrets, Least Privilege, Signed Artifacts)

### CI/CD Tools
48. Jenkins
    - Declarative vs Scripted Pipeline
    - Jenkinsfile (Stages, Steps, Post Actions)
    - Jenkins Agents (Master-Agent, Docker Agent)
    - Jenkins Plugins (Blue Ocean, Credentials, Docker)
    - Jenkins Shared Libraries
49. GitLab CI/CD (.gitlab-ci.yml, Runners, Stages, Artifacts, Environments)
50. GitHub Actions
    - Workflows, Jobs, Steps, Actions
    - Triggers (push, pull_request, schedule, workflow_dispatch)
    - Secrets and Environment Variables
    - Matrix Builds
    - Reusable Workflows, Composite Actions
    - Self-Hosted Runners
51. CircleCI (Orbs, Workflows, Executors)
52. AWS CodePipeline (Stages, Actions, Artifacts, Cross-Account)

### Deployment Strategies
53. Blue-Green Deployment (Zero Downtime, Instant Rollback, Cost)
54. Canary Deployment (Gradual Rollout, Metrics-Based Promotion)
55. Rolling Deployment (Incremental, maxSurge, maxUnavailable)
56. Feature Flags (LaunchDarkly, Unleash, Gradual Rollout, Kill Switch)
57. A/B Testing (Traffic Splitting, Metrics Comparison)
58. Rollback Strategies (Automatic, Manual, Database Rollback)

### Infrastructure as Code
59. IaC Basics (Declarative vs Imperative, Idempotency, Drift)
60. Terraform
    - HCL Syntax (Resources, Variables, Outputs, Data Sources)
    - State Management (Local, Remote, S3 + DynamoDB Locking)
    - Modules (Reusable, Registry, Versioning)
    - Workspaces (Environment Isolation)
    - Plan, Apply, Destroy Workflow
    - Terraform Import, State Manipulation
61. CloudFormation (Templates, Stacks, Change Sets, Nested Stacks, Drift Detection)
62. Ansible
    - Playbooks (Tasks, Handlers, Roles)
    - Inventory (Static, Dynamic)
    - Modules (apt, yum, copy, template, service)
    - Ansible vs Terraform (Configuration vs Provisioning)
63. Pulumi (Programming Languages, State, Stacks)
64. IaC Best Practices (Version Control, Code Review, Testing, Modules)

### Configuration Management
65. Configuration Management Basics (Desired State, Idempotency)
66. Environment Variables (12-Factor App, .env Files)
67. Secrets Management (Vault, AWS Secrets Manager, Sealed Secrets)
68. Configuration as Code (ConfigMaps, Parameter Store, Consul)

### Monitoring and Observability
69. Pipeline Monitoring (Build Times, Success Rate, MTTR)
70. Deployment Monitoring (Error Rate, Latency, Rollback Triggers)
71. CI/CD Metrics (DORA Metrics: Deployment Frequency, Lead Time, MTTR, Change Failure Rate)

### Advanced Topics
72. GitOps (Git as Single Source of Truth, Pull-Based Deployment)
73. ArgoCD (Application CRD, Sync, Auto-Heal, App of Apps)
74. Flux (Source Controller, Kustomize Controller, Helm Controller)
75. Progressive Delivery (Flagger, Argo Rollouts, Canary Analysis)
76. Chaos Engineering (Chaos Monkey, Litmus, Gremlin, Steady State)
77. Pipeline Orchestration (Multi-Pipeline, Cross-Project Dependencies)
78. Multi-Cloud CI/CD (Cloud-Agnostic Pipelines, Terraform Multi-Provider)

### Interview Scenarios
79. Design a CI/CD Pipeline for a Microservices Application
80. How to Handle Database Migrations in CI/CD
81. GitFlow vs Trunk-Based — When to Use Which
82. How to Implement Zero-Downtime Deployment
83. How to Manage Secrets in CI/CD Pipelines

---

## 🎯 Solution Architect Perspective

CI/CD knowledge is crucial for:
- **Automation**: Reduce manual errors, increase velocity
- **Quality**: Automated testing, early bug detection
- **Speed**: Faster time to market, frequent releases
- **Reliability**: Consistent deployments, easy rollbacks
- **Security**: Shift-left security, automated scanning
- **Collaboration**: Better team coordination, visibility

---

← Previous: AWS | Back to Main Index | Next: Design Patterns →
