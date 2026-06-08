# DecodeLabs Python Programming Portfolio (Projects 1-3)

Welcome to the main directory for the DecodeLabs Python Core Infrastructure training suite. This portfolio contains three foundational backend applications engineered to demonstrate programming logic, secure input validation, and algorithm execution.

---

## 🛠️ Global Architectural Paradigms

Across all three programs, development strictly follows industry-standard coding patterns:

* **The Input-Process-Output Framework:** Code routines are systematically divided into three clear phases—gathering data inputs, executing the backend transformation logic, and delivering the final output to the user interface.
* **In-Memory Management:** Programs utilize efficient active data collections (like structured lists and dictionaries) to process and store records instantly inside system RAM.
* **Fault-Tolerant Loops:** Continuous interactive menus run safely enclosed within error-catching blocks (`try-except`) to handle invalid typing entries seamlessly without crashing.
* **The Gatekeeper Entry:** Standard structural control blocks (`if __name__ == "__main__":`) are implemented to safeguard and guide clean program execution.

---

## 📁 Project Portfolio Matrix

### 🚀 Project 1: To-Do List
An elegant, modular Command Line Interface (CLI) application built to track daily tasks. This program focuses on dynamic list management, where tasks are appended as structured dictionary objects and selectively modified or removed using precise array index positioning.

### 📊 Project 2: Expense Tracker
A transactional financial tracker engineered to process data ingestion pipelines and track variable spending aggregates. It features robust input validation, manual string clipping for date formatting, and a dynamic leap-year algorithm to protect the ledger from incorrect timeline data entries.

### 🛡️ Project 3: Random Password Generator
A security-focused console program built to bridge the gap between requirement gathering and library integrations. It uses strict high-security boundaries to transform user length requests into non-predictable, highly random alphanumeric security strings utilizing Python's native modules.

---

## 💻 System Deployment & Interaction

### Prerequisites
* Ensure a stable installation of **Python 3.x** on your host computer.

### Method A: Using Code Editors (The Run Button)
1. Open any of your project source scripts (`todo_list.py`, `expense_tracker.py`, or `password_generator.py`) inside **VS Code, PyCharm, Thonny, or IDLE**.
2. Locate and press the green visual **Run / Play** icon on the software interface to instantly bring up the interactive terminal loop.

### Method B: Using the Command Line (Manual Terminal Commands)
Open your terminal window inside the root path where your source code files are saved, then execute the command for the specific program engine you want to launch:

```bash
# To launch Project 1: To-Do List
python todo_list.py

# To launch Project 2: Expense Tracker
python expense_tracker.py

# To launch Project 3: Random Password Generator
python password_generator.py
