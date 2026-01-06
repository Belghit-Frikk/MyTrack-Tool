# 🛰️ MyTrack-Tool 
**Professional IP Tracker & OS Fingerprinting Tool for Parrot OS**

![License](https://img.shields.io/badge/License-GPLv3-blue.svg)
![Python](https://img.shields.io/badge/Python-3.x-green.svg)

## 📖 Description
MyTrack-Tool is a custom-built OSINT script designed for security researchers. It combines geolocation API data with Nmap's powerful OS detection to provide a comprehensive report on any target IP.

## 🚀 Features
* **Real-time Geolocation:** Country, City, ISP, and Timezone.
* **OS Detection:** Uses Nmap to guess the target's Operating System.
* **Google Maps Integration:** Direct link to the target's location.
* **Cleanup Utility:** Built-in script to manage and delete scan reports.
* **Report Generation:** Saves all findings into a `.txt` file automatically.

## 🛠️ Installation & Usage
To install MyTrack on your system, run:
```bash
git clone [https://github.com/Belghit-Frikk/MyTrack-Tool.git](https://github.com/Belghit-Frikk/MyTrack-Tool.git)
cd MyTrack-Tool
chmod +x mytrack.py track-clean.sh
sudo cp mytrack.py /usr/local/bin/mytrack
sudo cp track-clean.sh /usr/local/bin/track-clean
