# 🧮 Simple Calculator using Tkinter

A beautifully designed, minimal, and fully functional **GUI Calculator** built using Python's `tkinter` module. This app performs basic arithmetic operations like addition, subtraction, multiplication, and division with an intuitive and elegant interface.

---

## 🛠️ Features

- Responsive GUI layout
- Basic operations: `+`, `-`, `*`, `/`
- Decimal point support
- **Clear (`C`)** and **Backspace (`⌫`)** functionality
- Exception handling with error display
- Professional UI styling using colors and font choices

---

## 🚀 Getting Started

### Requirements

- Python 3.x  
- No external dependencies — uses only the built-in `tkinter` module

### How to Run

1. Navigate to the project folder:
   ```bash
   cd utilities/simple-calculator
   ```
2. Run the calculator:
   ```bash
   python tkinter-calculator.py
   ```
---

## 💻 Code Highlights

- Uses `tk.Entry` for input/output display
- Dynamically generates buttons from a list
- Each button uses a shared click handler for clean logic
- Responsive grid layout using `sticky="nsew"` and row/column weights

---

## 🎨 UI Design

- Background: `#282c35` (Dark mode)
- Buttons:  
  - Numbers/Operators: `#61dafb`  
  - Clear/Backspace: `#ff6b6b`
- Font: Arial, size 16–20 for readability
- Centered input field with padding and justified text

---

## 📂 File Structure

```
📁 simple-calculator/
│
├── tkinter-calculator.py   # Main application file
└── readme.md               # Project documentation
```

## By **Vijay Rajesh R**  - [vijayrajeshr](https://github.com/vijayrajeshr)
