# DecodeLabs Backend Task Engine (Project 1)

An elegant, modular Command Line Interface (CLI) To-Do List application built with Python. This project serves as a foundational blueprint for backend architecture, focusing on the principles of **Data Ingestion**, **Dynamic In-Memory Management**, and **Structured Array Indexing**.

---

## 🛠️ Architectural Blueprint

This application is built with a focus on logical isolation and structured state mutation, mirroring fundamental data pipeline workflows:

### 1. The Model (In-Memory Active State)
* **Volatile Storage:** Utilizes an active list wrapper (`my_tasks`) containing structured dictionary schemas to serve as a high-speed, volatile runtime database.
* **Deterministic Structures:** Implements strict data models tracking task parameters (`task` text string and `done` boolean flag) directly inside active system RAM.

### 2. The View & Controller (User Interface Logic)
* **State Mutation Isolation:** Functional modules isolate operations like appending, updating, and popping data objects from the main execution loop.
* **Pythonic Conventions:** Integrates native `enumerate()` iteration structures rather than manual index counters to guarantee optimal, safe indexing loops.

### 3. The Gatekeeper
* Controlled system entry is safely managed using the industry-standard structural block: `if __name__ == "__main__":`.

---

## 🚀 Features

* **Create Tasks:** Real-time generation of structural dictionary rows appended instantly to active runtime memory.
* **Read Tasks:** Dynamic layout rendering complete with visual status badges (`✓ Done` vs `Pending`).
* **Update States:** Target selection checking that dynamically shifts task states to completed.
* **Delete Tasks:** Secure, targeted removal of individual entries using index positioning.
* **Input Fail-Safes:** Full `try-except` error handling blocks to catch and neutralize invalid non-integer inputs gracefully.

---

## ⚡ Performance Testing & Benchmarks

| Assessment Vector | Test Input | Expected Behavior | System Status |
| :--- | :--- | :--- | :--- |
| **Null Data Guard** | Passing an empty string `""` as a task | Intercepted by `.strip()` check; rejects entry with an error message. | **PASSED** |
| **Invalid Selection** | Entering string characters like `"abc"` in menu | Caught by terminal input evaluation rules; prompts menu re-entry. | **PASSED** |
| **Out-of-Bounds Index** | Selecting task number `99` on a 2-task list | Conditional bound check flags index as invalid; prevents runtime crash. | **PASSED** |

---

## 💻 How to Run the System

### Option A: Using Your Code Editor (Run Button)
1. Open `todo_list.py` inside **VS Code, PyCharm, Thonny, or IDLE**.
2. Click the green visual **Run / Play** icon on the workspace interface to start the program.

### Option B: Using the Terminal Command
Open your terminal window inside the project directory and execute:
```bash
python todo_list.py