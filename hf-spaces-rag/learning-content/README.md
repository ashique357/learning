# Learning Content

This folder contains all the learning materials for the Solution Architect roadmap.

## 📚 Subjects

1. **01-linux-os-fundamentals** - Operating systems, Linux administration
2. **02-basic-networking** - Network protocols, TCP/IP, DNS
3. **03-database** - Relational and NoSQL databases
4. **04-system-architecture** - Architectural patterns, scalability
5. **05-docker** - Containerization and Docker
6. **06-kubernetes** - Container orchestration
7. **07-aws** - AWS cloud services
8. **08-ci-cd** - Continuous integration and delivery
9. **09-design-patterns** - Software design patterns
10. **10-monitoring-observability** - Metrics, logging, tracing
11. **11-security-compliance** - Security principles and compliance
12. **12-message-queues-streaming** - Kafka, RabbitMQ, event streaming
13. **13-api-design-management** - REST, GraphQL, gRPC
14. **14-java** - Java programming
15. **15-spring-boot** - Spring Boot framework
16. **16-python** - Python programming
17. **17-django** - Django framework
18. **18-fastapi** - FastAPI framework
19. **19-frontend** - Frontend technologies

## 📝 Structure

Each subject folder contains:
- `index.md` - Main index with all topics
- Individual topic files (to be added)
- Examples and exercises (to be added)

## 🔄 Usage with RAG System

The RAG system in `../learning-rag-system/` automatically processes all markdown files in this folder to create an intelligent learning assistant.

To update the RAG system after adding new content:
```bash
cd ../learning-rag-system
python learning-rag-ingestion.py
```
