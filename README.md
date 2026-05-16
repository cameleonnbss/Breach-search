# BrixHub OSINT CLI Tool

A **command-line tool** for querying the **BrixHub API** to perform OSINT searches (identity, contact, address, vehicles, etc.).
Lightweight, written in Python, with no unnecessary dependencies.

---

---

## ✨ Features

- **Multi-criteria search**:
  Identity (name, first name, birth date...),
  Contact (email, phone, IP...),
  Address (city, postal code, country...),
  Unique IDs (NIR, IBAN, SIRET, SIREN...),
  Vehicles (license plate, VIN, brand...),
  Professional (company, job, position...).

- **Reverse Lookup**:
  Search by email, phone, or IBAN.

- **Account Info**:
  Displays your daily quota, BrixHub plan, and remaining requests.

- **Simple CLI Interface**:
  Interactive menus, guided input, clear results.

- **Secure**:
  Your API key is **never displayed** on screen.

---

---

## 💻 Installation

### **Windows**
1. Open **PowerShell** or **CMD**.
2. Install Python (if not already installed):
   Download from [python.org](https://www.python.org/downloads/windows/) (check **"Add Python to PATH"** during installation).
3. Clone the repo and install dependencies:
   ```cmd
   git clone https://github.com/cameleonnbss/Breach-search.git
   cd Breach-search
   pip install -r requirements.txt
   ```

### **Linux (Debian/Ubuntu)**
1. Open a terminal.
2. Install Python and pip (if not already installed):
   ```bash
   sudo apt update && sudo apt install python3 python3-pip git
   ```
3. Clone the repo and install dependencies:
   ```bash
   git clone https://github.com/cameleonnbss/Breach-search.git
   cd Breach-search
   pip3 install -r requirements.txt
   ```

### **macOS**
1. Open **Terminal**.
2. Install Python (if not already installed):
   ```bash
   brew install python
   ```
3. Clone the repo and install dependencies:
   ```bash
   git clone https://github.com/cameleonnbss/Breach-search.git
   cd Breach-search
   pip3 install -r requirements.txt
   ```

### **Termux (Android)**
1. Open **Termux** and update packages:
   ```bash
   pkg update && pkg upgrade
   ```
2. Install Python and Git:
   ```bash
   pkg install python git
   ```
3. Clone the repo and install dependencies:
   ```bash
   git clone https://github.com/cameleonnbss/Breach-search.git
   cd Breach-search
   pip install -r requirements.txt
   ```

---

---

## 🚀 Usage

1. **Run the script**:
   ```bash
   python main.py
   ```
   *(On some systems, use `python3 main.py` instead.)*

2. **Enter your BrixHub API key** when prompted.
   *(It will **not** be displayed on screen.)*

3. **Choose an option from the menu**:
   - `1` to `6`: Search by category (identity, contact, etc.).
   - `7`: Reverse Lookup (email, phone, IBAN).
   - `8`: View your BrixHub account info (quota, plan, etc.).
   - `0`: Exit.

4. **Fill in the requested fields** and confirm.
   Results will display directly in the terminal.

---

---

## 📋 Examples

### Search by Identity
```
Choice: 1

👤 Search by Identity

Last name: Dupont
First name: Jean
Birth date (YYYY-MM-DD): 1990-01-01
Fuzzy search? (y/n): y
Results per page (max 10): 10
Page: 1

✅ 2 result(s) found:

=== Result #1 ===
prenom: Jean
nom_famille: Dupont
email: jean.dupont@example.com
telephone: 0612345678
ville: Paris
_confidence: 85
_sources: Free (2024), SFR (2025)
```

### Reverse Lookup by Email
```
Choice: 7

🔍 Reverse Lookup

1. Search by Email
2. Search by Phone
3. Search by IBAN
0. Back

Choice: 1
Enter email: jean.dupont@example.com
```

---

---

## ⚠️ Important Notes

- **API Key Required**: You need a valid key from [BrixHub](https://brixhub.net/dashboard).
- **Respect Terms of Service**: Comply with BrixHub's usage policies.
- **No Data Storage**: Your API key is only used for the current session.

---
---
## 👤 Author

**camzzz**
- GitHub: [@cameleonnbss](https://github.com/cameleonnbss)
- Discord: `cameleonmortis_new`

---
*Made with ❤️ for the OSINT community.*
