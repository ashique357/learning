# Linux/OS Fundamentals

Master the foundation of operating systems, Linux administration, and system-level concepts essential for Solution Architects.

## 📑 Topics

### Core Concepts
1. Operating System Basics
2. Linux Architecture (Kernel, Shell, User Space)
3. Kernel and System Calls
4. Boot Process (BIOS/UEFI → Bootloader → Kernel → Init/Systemd)
5. Linux Distributions (Ubuntu, CentOS, RHEL, Amazon Linux)

### File System
6. File System Hierarchy (/, /etc, /var, /home, /proc, /dev)
7. File Permissions and Ownership (chmod, chown, chgrp)
    - Numeric vs Symbolic Permissions
    - SUID, SGID, Sticky Bit
8. File System Types (ext4, XFS, Btrfs, NFS)
9. Inodes and Links (Hard Links vs Soft Links)

### Command Line & Shell
10. Shell Basics and Types (bash, zsh, sh)
11. Essential Commands (ls, cp, mv, rm, find, grep, cat, head, tail, wc)
12. Text Processing Tools
    - grep (Regular Expressions, -i, -r, -v, -c)
    - awk (Field Processing, Patterns, Actions)
    - sed (Stream Editing, Substitution, Deletion)
    - cut, sort, uniq, tr, xargs
13. Shell Scripting
    - Variables, Conditionals, Loops
    - Functions, Exit Codes
    - Piping and Redirection (|, >, >>, 2>&1)
    - Command Substitution ($(), ``)
14. Environment Variables (PATH, HOME, export, .bashrc, .profile)

### Process Management
15. Processes and Threads (PID, PPID, Process Tree)
16. Process States and Lifecycle (Running, Sleeping, Zombie, Orphan)
17. Process Management Commands (ps, top, htop, kill, nice, renice)
    - Reading top/htop Output (CPU%, MEM%, Load Average)
18. Signals and Inter-Process Communication (SIGTERM, SIGKILL, SIGHUP, SIGINT)
19. Job Control and Background Processes (bg, fg, nohup, &, disown)

### Memory Management
20. Memory Architecture (Physical, Virtual, Kernel Space vs User Space)
21. Virtual Memory and Paging
22. Swap Space (Configuration, When to Use, Swappiness)
23. Memory Monitoring (free, vmstat, /proc/meminfo)

### Storage and I/O
24. Disk Partitioning (fdisk, parted, GPT vs MBR)
25. Logical Volume Manager (LVM) (PV, VG, LV, Extending, Snapshots)
26. RAID Configurations (RAID 0, 1, 5, 6, 10)
27. I/O Scheduling (CFQ, Deadline, NOOP)
28. Mounting and Unmounting (mount, umount, /etc/fstab)
29. Disk Usage Analysis (df, du, lsblk, iostat)

### User and Group Management
30. Users and Groups (/etc/passwd, /etc/group, /etc/shadow)
31. User Authentication (useradd, usermod, userdel, passwd)
32. Sudo and Privileges (/etc/sudoers, visudo)
33. PAM (Pluggable Authentication Modules)

### Networking Basics
34. Network Configuration (ifconfig, ip, nmcli)
35. Network Interfaces (eth0, lo, bonding)
36. Routing and IP Tables (route, iptables, nftables)
37. DNS Configuration (/etc/resolv.conf, /etc/hosts, dig, nslookup)
38. Network Troubleshooting (ping, traceroute, netstat, ss, curl, wget, telnet, nc)

### System Services
39. Systemd (Units, Targets, Dependencies)
40. Service Management (systemctl start/stop/restart/enable/disable/status)
    - systemctl vs service Comparison
41. Cron and Scheduled Tasks (crontab, cron expressions, at)
42. Logging with Syslog and Journald (journalctl, /var/log/, rsyslog)

### Performance and Monitoring
43. System Monitoring Tools (top, htop, vmstat, iostat, sar, dstat)
    - Reading Load Average (1min, 5min, 15min)
    - CPU Utilization (user, system, iowait, idle)
44. Performance Tuning (sysctl, ulimit, kernel parameters)
45. Resource Limits (ulimit, /etc/security/limits.conf)
46. Troubleshooting Techniques
    - High CPU Troubleshooting
    - High Memory / OOM Killer
    - Disk Full Scenarios
    - Network Connectivity Issues

### Security
47. Linux Security Model (DAC, MAC)
48. SELinux and AppArmor (Modes, Policies, Troubleshooting)
49. Firewall Configuration (iptables, firewalld, ufw)
50. SSH and Secure Access (Key-based Auth, ssh-keygen, ssh-agent, sshd_config)
51. Security Best Practices (Hardening, Audit, Fail2ban)

### Package Management
52. Package Managers (apt, yum, dnf, zypper)
53. Software Installation Methods (Source, Binary, Repository)
54. Dependency Management

### Advanced Topics
55. Containers and Namespaces (PID, Network, Mount, User)
56. Cgroups (Control Groups) (CPU, Memory, I/O Limits)
57. System Calls and strace (Debugging, Tracing)
58. Kernel Modules (lsmod, modprobe, insmod)

### Interview Scenarios
59. What Happens When You Type a Command in Terminal
60. How to Debug a Slow Linux Server
61. How to Find Which Process is Using a Port
62. How to Recover from a Full Disk

---

## 🎯 Solution Architect Perspective

Understanding Linux/OS fundamentals is crucial for:
- **Infrastructure Design**: Choosing right OS configurations for workloads
- **Performance Optimization**: Tuning systems for specific use cases
- **Security Architecture**: Implementing defense-in-depth strategies
- **Troubleshooting**: Diagnosing system-level issues in production
- **Automation**: Building reliable infrastructure automation
- **Cost Optimization**: Right-sizing resources based on OS metrics

---

← Back to Main Index | Next: Basic Networking →
