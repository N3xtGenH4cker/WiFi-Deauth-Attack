# WiFi Signal Scanner & Deauth Attack Tools

## Overview
This repository contains two powerful tools for scanning nearby WiFi networks and performing deauthentication attacks. These tools are designed for ethical hacking and penetration testing purposes.

## Tools
### 1. **SignalHunter** (WiFi Scanner)
A tool to scan for nearby WiFi networks, displaying their BSSID and channel information.

### 2. **SignalSlayer** (WiFi Deauth & Handshake Capture)
A tool to perform deauthentication attacks on a target WiFi network, allowing for handshake capture.

## Installation & Requirements
These scripts require Python3 and some additional packages.

### Prerequisites
- Linux-based OS (Tested on Kali Linux)
- Python3
- Wireless interface capable of monitor mode
- `scapy` library for packet manipulation

Install required dependencies:
```sh
sudo apt update && sudo apt install aircrack-ng
pip3 install scapy
```

## Usage

### **SignalHunter** (WiFi Scanner)
Scan for available WiFi networks.

#### Command:
```sh
sudo python3 signalHunter.py -i wlan0
```
#### Output Example:
```
BSSID                Channel   
==============================
00:14:22:01:23:45    6       
A4:7E:39:8F:AA:BB    11      
```

### **SignalSlayer** (WiFi Deauth & Handshake Capture)
Perform a deauthentication attack and capture WPA2 handshakes.

#### Command:
```sh
sudo python3 signalSlayer.py -i wlan0mon -c 6 -a 00:14:22:01:23:45 -t A4:7E:39:8F:AA:BB -o capture
```

- `-i wlan0mon`: Wireless interface in monitor mode
- `-c 6`: WiFi channel
- `-a 00:14:22:01:23:45`: Target AP MAC address
- `-t A4:7E:39:8F:AA:BB`: Target client MAC address
- `-o capture`: Output file for captured handshake

## Features
✅ **WiFi Scanner** – Detects networks and displays BSSID & channel.

✅ **Deauthentication Attack** – Disconnects a client from an AP.

✅ **Handshake Capture** – Helps in WPA2 security assessments.

## Author
**N3xtGenH4cker**

GitHub: [https://github.com/N3xtGenH4cker](https://github.com/N3xtGenH4cker)

## Legal Disclaimer
This project is intended for educational purposes only. Any misuse or unauthorized use is strictly prohibited.
