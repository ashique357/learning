# Basic Networking

Master networking fundamentals, protocols, and network architecture essential for Solution Architects.

## 📑 Topics

### Networking Fundamentals
1. OSI Model (7 Layers, Data Flow, Encapsulation/Decapsulation)
2. TCP/IP Model (4 Layers, Mapping to OSI)
3. IP Addressing and Subnetting
    - IPv4 Address Classes (A, B, C, D, E)
    - Subnet Mask Calculation
    - CIDR Notation
4. IPv4 vs IPv6 (Address Format, Header Differences, Transition Mechanisms)
5. MAC Addresses (Format, ARP Resolution, MAC Table)

### Network Protocols
6. TCP Protocol
    - 3-Way Handshake (SYN, SYN-ACK, ACK)
    - 4-Way Teardown (FIN, ACK)
    - Flow Control (Sliding Window)
    - Congestion Control (Slow Start, AIMD)
    - TCP vs UDP Comparison
7. UDP Protocol (Connectionless, Use Cases: DNS, Video, Gaming)
8. HTTP/HTTPS
    - HTTP Request/Response Structure
    - HTTP Headers (Content-Type, Authorization, Cache-Control)
    - HTTP Keep-Alive, Pipelining
    - HTTPS (TLS Handshake, Certificate Chain)
9. HTTP/2 and HTTP/3
    - Multiplexing, Server Push, Header Compression
    - HTTP/3 QUIC Protocol
10. WebSocket Protocol (Full-Duplex, Handshake, Use Cases)
11. DNS (Domain Name System)
    - DNS Resolution Step-by-Step (Recursive, Iterative)
    - DNS Record Types (A, AAAA, CNAME, MX, NS, TXT, SOA, PTR)
    - DNS Caching (TTL, Browser, OS, Resolver)
    - DNS Propagation
12. DHCP (Discover, Offer, Request, Acknowledge)
13. FTP/SFTP (Active vs Passive Mode, SFTP over SSH)
14. SMTP (Email Delivery, MX Records)
15. ARP (Address Resolution Protocol) (ARP Table, ARP Request/Reply)
16. ICMP (Ping, Traceroute, TTL)

### Network Devices
17. Routers (Routing Table, Default Gateway, NAT)
18. Switches (MAC Table, VLAN, Layer 2 vs Layer 3)
19. Load Balancers (Layer 4 vs Layer 7, Health Checks)
20. Firewalls (Stateful vs Stateless, Rules, Zones)
21. Gateways (Protocol Translation, Default Gateway)
22. Proxy Servers (Forward Proxy vs Reverse Proxy)

### Network Architecture
23. LAN, WAN, MAN (Scope, Technologies, Use Cases)
24. VLANs (Tagging, Trunk Ports, Inter-VLAN Routing)
25. VPN (Virtual Private Network)
    - Site-to-Site VPN vs Client VPN
    - IPSec, OpenVPN, WireGuard
26. NAT (Network Address Translation)
    - SNAT, DNAT, PAT
    - NAT Traversal
27. Port Forwarding
28. Subnets and CIDR (Subnet Design, Public vs Private Subnets)

### Routing and Switching
29. Routing Basics (Routing Table, Longest Prefix Match)
30. Static vs Dynamic Routing
31. Routing Protocols (BGP, OSPF, RIP)
    - BGP (Border Gateway Protocol, AS, eBGP vs iBGP)
    - OSPF (Link-State, Areas, Cost)
32. Switching Concepts (MAC Learning, Flooding, Forwarding)
33. Spanning Tree Protocol (STP, Loop Prevention, Root Bridge)

### Network Services
34. Load Balancing Algorithms (Round Robin, Least Connections, IP Hash, Weighted)
35. CDN (Content Delivery Network) (Edge Locations, Cache Hit/Miss, Origin)
36. Reverse Proxy (SSL Termination, Caching, Compression)

### Network Security
37. Firewall Rules (Inbound, Outbound, Stateful Inspection)
38. Network Segmentation (DMZ, Microsegmentation)
39. DDoS Protection (Types: Volumetric, Protocol, Application Layer)
40. SSL/TLS
    - TLS Handshake Step-by-Step
    - Certificate Types (DV, OV, EV)
    - mTLS (Mutual TLS)
41. Network ACLs (Stateless, Rule Evaluation Order)
42. Security Groups (Stateful, Allow Rules Only)

### Performance and Monitoring
43. Bandwidth and Throughput (Difference, Measurement)
44. Latency and Jitter (Causes, Impact, Measurement)
45. Network Monitoring Tools (Nagios, PRTG, SNMP)
46. Packet Analysis (Wireshark, tcpdump)
    - Capturing and Filtering Packets
    - Reading Packet Headers
47. Network Troubleshooting (ping, traceroute, mtr, dig, nslookup, netstat, ss)

### Advanced Topics
48. Software Defined Networking (SDN) (Control Plane, Data Plane Separation)
49. Network Function Virtualization (NFV)
50. Zero Trust Networking (Never Trust, Always Verify, Microsegmentation)

### Interview Scenarios
51. What Happens When You Type a URL in Browser (Full Flow)
52. How DNS Resolution Works End-to-End
53. TCP vs UDP — When to Use Which
54. How Does HTTPS Work (TLS Handshake Explained)
55. How Load Balancers Work (Layer 4 vs Layer 7)

---

## 🎯 Solution Architect Perspective

Understanding networking is crucial for:
- **Architecture Design**: Designing scalable, secure network topologies
- **Performance Optimization**: Minimizing latency, maximizing throughput
- **Security**: Implementing defense-in-depth network security
- **Troubleshooting**: Diagnosing network issues in production
- **Cost Optimization**: Efficient use of bandwidth and network resources
- **Cloud Architecture**: VPC design, hybrid connectivity, multi-region setups

---

← Back to Main Index | Next: Database →
