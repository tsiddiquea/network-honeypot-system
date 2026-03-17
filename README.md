# Honeypot Intrusion Detection System

## Overview

The Honeypot Intrusion Detection System is a defensive cybersecurity simulation project designed to monitor, capture, and analyze malicious connection attempts targeting network services.

This project emulates a vulnerable SSH-like service to attract attackers, log their activities, and generate actionable security intelligence.
It demonstrates real-world blue-team concepts such as attack surface exposure, credential harvesting detection, brute-force identification, and incident reporting.

The system provides hands-on experience in threat monitoring, intrusion detection engineering, and secure defensive architecture design.


## Key Features

* Simulated SSH service honeypot
* Real-time attacker connection monitoring
* Credential capture and logging
* Brute-force attack detection using attempt thresholds
* Multi-threaded client handling
* Security event timestamp tracking
* Automated attack intelligence reporting
* IP-based attack statistics generation
* Lightweight and portable deployment


## System Architecture

The honeypot operates as a TCP server that listens for incoming connections on a designated port.
Upon connection, the system mimics a legitimate authentication interface to observe attacker behavior.

Captured attack data includes:

* Source IP address
* Login attempt timestamps
* Username and password attempts
* Connection frequency patterns
* Suspicious brute-force indicators

Collected data is then processed to generate a structured security analysis report.


## Project Structure
```
honeypot/
│
├── honeypot.py          → Main honeypot server logic
├── logger.py            → Attack logging and statistical analysis engine
├── report.py            → Security report generation module
├── attacker_test.py     → Attack simulation client  
└── README.MD
```

## Technologies Used

* Python Socket Programming
* Multi-threading (concurrent client handling)
* Network traffic interaction simulation
* Defensive logging and incident analysis
* Basic intrusion detection logic


## How the Honeypot Works

1. The server listens for incoming TCP connections.
2. When an attacker connects, the system displays a fake SSH login banner.
3. The attacker attempts to enter credentials.
4. The honeypot captures and stores:

	* IP address
	* username attempts
	* password attempts
	* connection frequency
5. The logger analyzes patterns to detect brute-force activity.
6. A structured incident report is generated summarizing attack intelligence.


## Example Terminal Output

### Running the Honeypot
```
$ python honeypot.py

Honeypot running on port 2222 (SSH simulation)
Connection attempt detected
IP: 192.168.1.50
Timestamp: 2026-03-05 20:15:32
Credential attempt captured
Username: admin
Password: password123
```

### Generated Security Report
```
===== HONEYPOT ATTACK REPORT =====

Total connections: 18
Unique IPs: 3
Top username tried: admin
Top password tried: password123

Possible brute-force attackers:
192.168.1.50 → 10 attempts
```


## Performance Characteristics

* Lightweight network monitoring architecture
* Efficient multi-threaded connection handling
* Minimal CPU and memory consumption
* Suitable for local lab environments and security training setups


## Security & Ethical Use

This project is developed strictly for:

* cybersecurity education
* defensive security experimentation
* intrusion detection learning
* threat intelligence practice

The honeypot must only be deployed in controlled environments and authorized lab networks.

Unauthorized deployment on public systems or production networks is strongly discouraged.


## Learning Objectives

This project demonstrates practical skills in:

* Intrusion detection system design
* Network attack monitoring strategies
* Threat intelligence collection
* Secure logging architecture
* Brute-force detection logic
* Defensive cybersecurity engineering


## Author

Developed as part of a hands-on cybersecurity learning initiative focused on real-world defensive security practices and attack simulation environments.


## License

This project is released for educational and research purposes.
Use responsibly and only in permitted environments.
