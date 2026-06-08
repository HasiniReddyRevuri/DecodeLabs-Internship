```markdown
# DecodeLabs Expense Tracker Engine (Project 2)

An industrial-grade, data-validated Command Line Interface (CLI) financial management application built with Python. This project serves as a foundational blueprint for transactional backend architecture, focusing on the principles of **Algorithmic Input Validation**, **In-Memory Ledger Mapping**, and **Accumulative Data Tracking**.

---

## 🛠️ Architectural Blueprint

This application is engineered with a strict focus on data sanitization, custom mathematical error checks, and isolated transactional updates:

### 1. The Model (In-Memory Micro Ledger)
* **Volatile Transaction Cache:** Utilizes an active list wrapper (`expenses_list`) storing deep schema-nested Python dictionaries to track transaction parameters (`date`, `category`, `description`, `amount`) dynamically inside system RAM.
* **Aggregated Real-Time Tracking:** Maintains a persistent tracking counter variable (`total_spent`) that uses real-time accumulative floating-point math to reflect accurate overall spending values.

### 2. Validation & Processing Logic (The Guardrails)
* **Deterministic Date Parsing:** Leverages manual array string slicing algorithms (`date[0:2]`, `date[3:5]`, `date[6:10]`) combined with leap-year formulas to validate strict timeline bounds without relying on external packages.
* **Type-Sanitization Layers:** Protects the internal system ledger with strict format blocks ensuring text-only fields (categories/descriptions) and standard fractional floats (amounts) match production database guidelines.

### 3. The Interactive Loop (The Interface)
* Driven by a continuous-state looping algorithm wrapped tightly in safe `try-except` conditional logic to capture input anomalies without crashing the engine core.

---

## 🚀 Features

* **Strict Temporal Checks:** Automatic day-range limit detection based on month types (including dynamic **Leap-Year Equations** for February up to year **2026**).
* **Smart Contextual Success Tags:** Smart validation checking that flags whether data belongs to the current operating cycle (2026) or historical data banks.
* **Dynamic Ledger Generation:** Generates real-time index-numbered summaries complete with formatted currency printing output blocks (`$.2f`).
* **Accumulative Ledger Math:** Direct math aggregation rules that update total balances immediately upon confirmed validation of data entries.

---

## ⚡ Performance Testing & Benchmarks

| Assessment Vector | Test Input | Expected Behavior | System Status |
| :--- | :--- | :--- | :--- |
| **Invalid Date Format** | `05-11-2026` or `5/11/2026` | Delimiter string checks fail; rejects input immediately. | **PASSED** |
| **Leap-Year Precision** | `29/02/2026` | Modulus math evaluates 2026 as non-leap; blocks input. | **PASSED** |
| **Negative Financials** | Entering `-45.50` or `0` for amount | Conditional threshold blocks values $\le 0$; arrays remain clean. | **PASSED** |
| **Numeric Type Rejection**| Passing pure numbers `12345` as Category | `.isdigit()` check intercepts code; requests text characters. | **PASSED** |

---

## 💻 How to Run the System

### Option A: Using Your Code Editor (Run Button)
1. Open `expense_tracker.py` inside **VS Code, PyCharm, Thonny, or IDLE**.
2. Click the green visual **Run / Play** icon on the workspace interface to start the program.

### Option B: Using the Terminal Command
Open your terminal window inside the project directory and execute:
```bash
python expense_tracker.py