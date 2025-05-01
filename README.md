# 🛡️ Clickjack Vulnerability Tester

Easily test any website for Clickjacking vulnerabilities with this lightweight Python tool.  
It checks for proper HTTP security headers (`X-Frame-Options`, `Content-Security-Policy`) and provides a visual browser-based test with an iframe preview.  

---

## 🚀 Features

- ✅ Checks for **`X-Frame-Options`** header
- ✅ Checks for **`Content-Security-Policy`** (specifically `frame-ancestors`)
- 🌐 Launches a browser-based test with an embedded `<iframe>`
- 🎨 Colorful terminal output
- 💡 One-line command: `clickjack https://example.com`

---

## 📦 Requirements

- Python 3.x
- `requests` library
- `colorama` for colored terminal output

> Kali Linux users: Python is already installed — but see [Kali installation notes](#🐉-kali-linux-users-read-this) below.

---

## 🛠️ Installation

### ✅ Easy Automated Install (For Linux)

```bash
git clone https://github.com/senukdias/clickjack.git
cd clickjack
chmod +x install.sh
sudo ./install.sh
```

After installation, use the tool like this:

```bash
clickjack https://example.com
```

---

## 🌍 Example Output

```bash
clickjack https://example.com
```

### 💡 Terminal Output:
```
🔍 Checking Clickjacking protection for: https://example.com

✔ X-Frame-Options is set: DENY
✔ Content-Security-Policy with frame-ancestors is set:
  frame-ancestors 'none';

✅ Your site appears to be protected against Clickjacking.
🌐 Opening visual test in your browser...
```

### 🖼️ Browser Output:
An iframe test page automatically opens to show if the site can be embedded.

---

## 🧪 Manual Visual Test

Want to test manually? Create your own HTML file like:

```html
<iframe src="https://example.com" width="800" height="600"></iframe>
```

If the site **loads inside** the iframe, it may be vulnerable.

---

## 🐉 Kali Linux Users: Read This

Kali Linux restricts direct system-wide Python installations.

Instead of using `pip install`, do one of the following:

### 🅰️ Option 1: Use `pipx` (Recommended)
```bash
sudo apt install pipx
pipx ensurepath
pipx install .
```

### 🅱️ Option 2: Use Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python clickjack.py https://example.com
```

---

## 🔧 Uninstallation

To remove the tool:

```bash
sudo rm /usr/bin/clickjack
sudo rm /usr/local/bin/clickjack_tool
```

---

## 🙌 Credits

Created by [Senuk Dias](https://senukdias.tech) 🧑‍💻  
Inspired by real-world web security practices and the need for accessible vulnerability testing tools.

📬 **Connect with me:**

- 🌐 Website: [https://senukdias.tech](https://senukdias.tech)
- 💼 LinkedIn: [linkedin.com/in/senukdias](https://linkedin.com/in/senukdias)
- 🐦 Twitter/X: [@senukdias](https://twitter.com/senukdias)
- 💻 GitHub: [github.com/senukdias](https://github.com/senukdias)
- 📸 Instagram: [@senuk.dias](https://instagram.com/senuk.dias)

---

## ☕ Support

If this tool helped you or your project, consider giving it a ⭐ on GitHub!

---
