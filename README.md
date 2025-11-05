# 🌐 CTT+ Programming Language

**CTT+** is a custom mini programming language created by **Kenzo (CoDev Studios)**.  
It’s designed for fun and educational purposes — simulating a simple antivirus system that can detect threats, show notifications, and speak alerts.

---

## ⚙️ Features
- 🧠 Custom syntax (`.ctt+` files)
- 🔔 System notifications
- 🗣️ Voice alerts using system TTS
- 🧩 Script compiler (`compile_ctt.py`)
- 💾 Example programs in `/examples`

---

## 📁 Folder Structure

CTTPlus/ ├─ cttplus.py              # Core functions of CTT+ ├─ compile_ctt.py          # Script compiler/runner ├─ README.md               # Documentation └─ examples/ ├─ fun_scan.ctt+        # Basic virus scan simulation └─ voice_alert.ctt+     # Voice alert demonstration

---

## 🧰 Functions
| Function | Description |
|-----------|--------------|
| `printy(text)` | Prints a message to the console |
| `waity(seconds)` | Waits for a specified time |
| `notify(title, message)` | Shows a notification on screen |
| `sayy(voice, message)` | Speaks the message using system voice |
| `scan_system()` | Simulates virus scanning process |

---

## 🚀 Usage
Run a `.ctt+` file using the compiler:
```bash
python compile_ctt.py examples/fun_scan.ctt+

Example output:

🔧 Running CTT+ Script: examples/fun_scan.ctt+
Scanning system for potential threats...
✅ No threats found.
✨ Scan complete. System is secure.


---

🧩 Example Scripts

🔍 fun_scan.ctt+

printy("Starting system scan...")
waity(1)
scan_system()
notify("CTT+ Scan", "No threats detected.")

🔊 voice_alert.ctt+

printy("CTT+ Voice Alert Demo")
sayy("CTT+", "Hello user! This is a voice alert test.")
notify("CTT+ Security", "System is secure.")


---

💡 About

CTT+ is made for fun & experimentation — not a real antivirus engine.
Created by Kenzo / CoDev Studios for learning, creativity, and entertainment.


---

🧠 License

This project is open-source and free to use for educational purposes.
Feel free to fork, improve, or experiment!


---

⭐ Created with ❤️ by Kenzo (CoDev Studios)
