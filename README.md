# Network Traffic Analysis and Manipulation  

## 📌 Description  
Two key ideas in network security are **packet sniffing** and **spoofing**, which pose serious risks to network communication. Understanding these threats is essential to comprehending **network security protocols**.  

Various tools exist for packet sniffing and spoofing, including:  
- **Wireshark**  
- **Tcpdump**  
- **Netwox**  
- **Scapy**  

Both **attackers** and **security specialists** frequently utilize these techniques. While knowing how to use these tools is vital, understanding their inner workings—how software implements packet sniffing and spoofing—is even more crucial.  

---

## 🛠️ Languages and Utilities Used  
- **Python**  
- **Ubuntu 20.04 VM**  

## 💻 Environments Used  
- **Windows 11 Home (21H2)**  

---

## 📚 Lab Topics Covered  
✔️ Basics of **packet sniffing** and **spoofing**  
✔️ Using the **pcap** library and **Scapy** for packet sniffing  
✔️ Using **raw sockets** and **Scapy** for packet spoofing  
✔️ Manipulating packets using **Scapy**  

---

## ⚙️ Shell Script Commands  
| Command | Description |
|---------|------------|
| `./dc-build.sh` | Builds the Docker images. Can take an additional parameter, e.g., `./dc-build.sh --no-cache` |
| `./dc-up.sh` | Starts the Docker containers in the foreground |
| `./dc-up-d.sh` | Starts the Docker containers in the background |
| `./dc-stop.sh` | Stops the Docker containers, with optional parameters |
| `./dc-down.sh` | Stops and removes the Docker containers, with optional parameters |
| `./dc-unittest.sh` | Utility script to aid in running a specific unit test class |

---

## 🔍 Program Walk-through  

### **Using Scapy for Sniffing and Spoofing**  
🔹 Sniffing packets with **Scapy**, including setting filters to capture specific types of packets (e.g., **ICMP** or **TCP**)  
🔹 Spoofing **ICMP** packets with arbitrary source IP addresses using **Scapy**  
🔹 Implementing a **traceroute-like tool** using **Scapy** by manipulating the **TTL (Time-To-Live)** field in IP packets  
🔹 Combining **sniffing and spoofing** techniques to create a program that **automatically sends spoofed ICMP replies**  

### **Writing C Programs for Sniffing and Spoofing**  
📌 Writing **C programs** to manually implement packet sniffing and spoofing, helping to understand the **low-level implementation details** of these techniques  

---

🚀 **This project provides hands-on experience with core networking security concepts, leveraging both Python and C for deep technical insights into packet analysis and manipulation.**  
