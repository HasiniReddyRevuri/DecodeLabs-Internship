```markdown
# DecodeLabs Enterprise Random Entropy Engine (Project 3)

A security-focused, architectural deployment built with Python. This project serves as a foundational blueprint for backend credential subsystems, demonstrating **Standard Library Integration**, **Strict NIST Cryptographic Constraints**, and the **Input-Process-Output (IPO) Structural Framework**.

---

## 🛠️ Architectural Blueprint

This application is built by breaking complex cryptographic workflows down into three distinct, manageable backend lifecycle phases [cite: 75-76]:

### Phase 1: Input Environmental Validation
* **The Scaffold Entrance:** The input phase acts as the primary gatekeeper and point of failure insulation for the engine[cite: 86, 88].
* **NIST SP 800-63-4 Alignment:** Enforces high-security context standards by strictly mandating an absolute minimum length of **15 characters** and a maximum constraint cap of **64 characters** to suppress predictable pattern structures [cite: 92-94].

### Phase 2: Backend Core Transformation
* **High Entropy Pooling:** Shifts processing focus from custom logic toward verified, high-quality standard library integration (`import random`, `import string`)[cite: 72].
* **Selection Algorithm:** Compiles alphanumeric data streams (`string.ascii_letters + string.digits`) using memory-efficient list comprehensions to guarantee peak performance and algorithmic randomness [cite: 28, 99-100].

### Phase 3: Output Delivery
* **Provision Delivery:** Coordinates the safe extraction and generation of the final secure string token across verified digital shield terminal lines[cite: 10, 83].

---

## 🚀 Features

* **Alphanumeric Character Synthesis:** Combines uppercase letters, lowercase letters, and base-10 numerical indexes to form chaotic string arrays[cite: 28].
* **Continuous Ingestion Traps:** Uses localized `try-except` data loops to identify and neutralize type conversion anomalies (`ValueError`) without interrupting runtime system states[cite: 90].
* **Zero Legacy Dependency:** Completely ditches obsolete complexity mandates (like forced symbol placement patterns) in strict favor of pure length-driven protection mechanics [cite: 92-93].

---

## ⚡ Performance Testing & Benchmarks

| Assessment Vector | Test Input | Expected Behavior | System Status |
| :--- | :--- | :--- | :--- |
| **Below-Minimum Check** | Length value `12` | Intercepted by NIST boundary check; rejects input as insecure. | **PASSED** |
| **Above-Maximum Check** | Length value `75` | Intercepted by boundary cap check; limits allocation to 64. | **PASSED** |
| **String Ingestion Trap** | Entering `"sixteen"` as length | Caught by `ValueError` handler; keeps engine loop running safely. | **PASSED** |

---

## 💻 How to Run the System

### Option A: Using Your Code Editor (Run Button)
1. Open `password_generator.py` inside **VS Code, PyCharm, Thonny, or IDLE**.
2. Click the green visual **Run / Play** icon on the workspace interface to start the program.

### Option B: Using the Terminal Command
Open your terminal window inside the project directory and execute:
```bash
python password_generator.py