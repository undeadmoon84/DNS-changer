# DNS Changer

A simple Windows DNS changer script written in Python.
It allows you to quickly switch between multiple DNS providers or reset to automatic DNS.

---

## Features

* Fully self-contained Python script (no external JSON required)
* Includes 25 popular DNS providers (Shecan, Cloudflare, Google, OpenDNS, Quad9, AdGuard, etc.)
* Auto-detects available network interfaces
* Works perfectly as a standalone `.exe` on Windows

---

## Requirements

* Python 3.x installed on Windows
* Administrator privileges to change DNS settings

---

## Usage

1. Clone or download this repository:

```bash
git clone https://github.com/undeadmoon84/DNS-changer.git
cd DNS-changer
```

2. Run the script:

---

## Build Windows Executable

You can convert the script to a standalone `.exe` using PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile dns_changer.py
```

* The `.exe` will be located in the `dist/` folder
* You can run the `.exe` directly on Windows without Python


---

3. Follow the prompts to:

* Select your network interface
* Choose a DNS provider from the menu, or reset DNS to automatic

> ⚠️ **Important:** Run the script as Administrator. If the script fails, the terminal will wait so you can read the error.


## DNS Providers Included

* Shecan(185)
* Shecan(178)
* Electro
* Cloudflare
* OpenDNS
* CleanBrowsing
* Alternate DNS
* Quad9
* AdGuard DNS
* OpenNIC
* DNS Watch
* Verisign
* Safe DNS
* Yandex DNS
* Google Public DNS
* Comodo Secure
* Neustar DNS
* Host Iran
* Gozar DNS
* DYN DNS
* Shatel DNS
* Radar Game DNS
* Pishgaman DNS
* 403 Online DNS
* Bogzar DNS

---

## License

This project is licensed under the MIT License.
