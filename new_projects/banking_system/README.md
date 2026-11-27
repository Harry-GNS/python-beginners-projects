# Python Banking Management System

This project is a modular command-line interface (CLI) application demonstrating core Object-Oriented Programming (OOP) concepts in Python.

# 🚀 Key Features

- Account Management: Create unique bank accounts with initial deposits.
- Transactions: Deposit and withdraw funds with validation checks.
- Data Persistence: Uses the built-in json library to save accounts permanently to a local file (accounts.json).
- Error Handling: Catches invalid inputs and insufficient funds using custom Python exceptions.
- Modular Design: Code is split across three files for improved structure and readability.

# 📁 Files Explained
- accounts.py: Contains the Account class and custom Exception definitions.
- bankmanager.py: Manages the overall system, including loading/saving data and creating accounts.
- main.py: The user interface and application entry point.

# ⚙️ How to Run
1. Make sure you have Python installed.
2. Navigate to this folder in your terminal.
3. Run the main file using the Python interpreter:

```bash
python main.py
```

The program will automatically create the accounts.json file when you create your first account.

# 🧪 How to Run the Tests
From this folder, run:

```bash
python -m unittest discover -s tests
```

The tests use a temporary data file, so they do not change your accounts.json.

Created by : Shanmukh