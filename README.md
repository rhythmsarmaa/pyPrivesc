  pyPrivesc

pyPrivesc is a Linux privilege escalation enumeration tool written in Python.
It automates manual enumeration techniques commonly used in HTB, TryHackMe, and real-world pentesting engagements.

 Features

✔ Sudo privilege checks

✔ Writable file detection

✔ Cron job misconfiguration detection

✔ SUID binary scanning

✔ PATH hijack detection

✔ Linux capabilities check

✔ SSH key exposure detection

✔ Kernel information analysis

✔ Running services inspection

  Usage
git clone https://github.com/rhythmsarmaa/pyPrivesc.git
cd pyPrivesc
python3 main.py

## 📷 Example Output

### 🔹 System Info Check
![system info](systeminfocheck.png) 

### 🔹 Sudo Check
![sudo](sudo.png)

### 🔹 Cron Check
![cron](cron.png)

### 🔹 Kernel Check
![kernel](kernel.png)

### 🔹 Weak File Permissions Check
![weak file permissions](weakfilepermission.png)

  Purpose

This tool was built to practice automation of Linux privilege escalation techniques and simulate real-world red-team enumeration workflows.

⚠️ Disclaimer

This tool is for educational and authorized testing purposes only.
