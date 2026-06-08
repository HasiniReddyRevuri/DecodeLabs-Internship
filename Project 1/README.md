# To-Do List Application (Project 1)

An elegant, modular Command Line Interface (CLI) To-Do List application built with Python. This project serves as a foundational blueprint for basic data management, focusing on the principles of gathering user inputs, dynamic in-memory task management, and list indexing.

---

## 🛠️ Program Design

This application is built with a focus on logical isolation and structured functions to manage your daily tasks cleanly:

### 1. In-Memory Task Storage
* **Active Storage:** Utilizes a simple Python list (`my_tasks`) populated by structured dictionary entries to hold your tasks dynamically inside the computer's temporary memory (RAM).
* **Data Fields:** Tracks two precise elements for every single task row: the `task` description string and a `done` completion status (True/False).

### 2. View & Function Logic
* **Separation of Functions:** Individual tasks like adding, viewing, marking tasks as done, and deleting tasks are divided into their own standalone code blocks.
* **Clean Index Loops:** Integrates Python's native `enumerate()` logic to easily number your tasks on the screen without needing to build complex index counters.

### 3. Execution Guard
* Controlled program startup is safely managed using the standard Python structure: `if __name__ == "__main__":`.

---

## 🚀 Features

* **Add Tasks:** Real-time generation of task rows appended instantly to your active list memory.
* **View Tasks:** Dynamic rendering of your list complete with visual status badges (`✓ Done` vs `Pending`).
* **Mark Task as Done:** Target selection checks that instantly update task completion states.
* **Delete Tasks:** Secure, targeted removal of individual entries using index positioning.
* **Input Fail-Safes:** Full `try-except` error handling blocks to catch and handle typing mistakes (like passing letters into number options) gracefully without crashing.

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
