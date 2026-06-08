# Random Password Generator (Project 3)

A security-focused Command Line Interface (CLI) application built with Python. This project serves as an introductory blueprint for credential generation, demonstrating how to use Python's built-in libraries to solve real-world security challenges through module integration and string manipulation.

---

## 🛠️ Program Design

This application is built by breaking the cryptographic workflow down into three distinct, manageable backend lifecycle phases:

### Phase 1: Environmental Input Validation
* **The Failure Gatekeeper:** The input phase acts as the primary validation layer to keep the system stable and secure.
* **Length Bounds Compliance:** Enforces industry-standard guidelines by mandating an absolute minimum length of **15 characters** and a maximum constraint cap of **64 characters** to prevent weak or oversized credentials.

### Phase 2: Backend Core Transformation
* **Standard Library Integration:** Instead of building custom, error-prone random logic, the program utilizes verified standard libraries (`import random` and `import string`).
* **Alphanumeric Character Synthesis:** Pools available character sets (`string.ascii_letters + string.digits`) and executes a selection list comprehension loop to transform the user's length choice into a non-predictable string array.

### Phase 3: Output Delivery
* **Shield Deployment:** Coordinates the final token extraction and prints the secure generated password out to the terminal interface.

---

## 🚀 Features

* **Alphanumeric Generation:** Dynamically creates complex passwords using uppercase letters, lowercase letters, and numbers.
* **Continuous Input Traps:** Uses a localized `try-except` data loop to catch typing errors (like entering words instead of integers) safely without breaking the system program loop.
* **Clean Formatting Layout:** Utilizes distinct structural section indicators to show the exact lifecycle phases as the code processes data.

---

## ⚡ Performance Testing & Benchmarks

| Assessment Vector | Test Input | Expected Behavior / Console Output | System Status |
| :--- | :--- | :--- | :--- |
| **Below-Minimum Check** | Length value `12` | Intercepts input and prints:<br>`[Validation Error] Below 15 character minimum requirement for high-security contexts.` | **PASSED** |
| **Above-Maximum Check** | Length value `75` | Intercepts input and prints:<br>`[Validation Error] Exceeds maximum allowed passphrase limit of 64 characters.` | **PASSED** |
| **String Ingestion Trap** | Entering `"sixteen"` | Catches `ValueError` and prints:<br>`[System Alert] Input phase failure. Value must be a valid target numerical integer.` | **PASSED** |

---

## 💻 How to Run the System

### Option A: Using Your Code Editor (Run Button)
1. Open `password_generator.py` inside **VS Code, PyCharm, Thonny, or IDLE**.
2. Click the green visual **Run / Play** icon on your development interface to start the program loop.

### Option B: Using the Terminal Command
Open your terminal window inside the Project 3 directory and execute the following instruction:
```bash
python password_generator.py
