# Simple OSINT & Information Gathering Tool
A Python-based reconnaissance tool designed to automate the initial phase of security foot-printing. Developed as part of a Cybersecurity Course assignment.

## 🚀 Features
* **WHOIS Lookup**: Retrieves registration details, registrar information, and domain age.
* **DNS Records**: Automatically fetches A records (IP addresses) and MX records (Mail Servers).
* **IP Geolocation**: Uses the IP-API to find the physical city, country, and ISP of the target server.
* **Security Header Analysis**: Scans for the presence of security-critical HTTP headers like CSP and HSTS.
* **Subdomain Enumeration**: Checks for common subdomains (www, dev, admin, etc.) to map out infrastructure.

## 🛠️ Requirements
This tool requires Python 3 and the following libraries:
* `dnspython`
* `python-whois`
* `requests`

## 📖 How to Use
1. Clone the repository to your local machine.
2. Install dependencies: `pip install -r requirements.txt` (or install manually).
3. Run the script: `python3 gather.py`.
4. Enter the target domain when prompted (e.g., example.com).

## ⚠️ Disclaimer
This tool is for educational purposes only. I am not responsible for any misuse. Always ensure you have permission before performing any type of scanning or information gathering.
