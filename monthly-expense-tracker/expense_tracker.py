import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os
import math

# ---------------- COLORS ----------------
BG = "#F5F2EB"
BROWN = "#604735"
GOLD = "#D9A441"
WHITE = "#FFFFFF"
GREEN = "#367653"
RED = "#B84444"
TEXT = "#302820"

# ---------------- DATA STORAGE ----------------
DATA_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "expenses.json"
)

budget = 10000


def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Invalid expense data format.")

        valid_expenses = []

        for item in data:
            if not isinstance(item, dict):
                continue

            name = item.get("name")
            category = item.get("category")
            date = item.get("date")
            amount = item.get("amount")

            if (
                isinstance(name, str)
                and isinstance(category, str)
                and isinstance(date, str)
                and isinstance(amount, (int, float))
                and not isinstance(amount, bool)
                and math.isfinite(amount)
                and amount > 0
            ):
                valid_expenses.append({
                    "date": date,
                    "name": name,
                    "category": category,
                    "amount": amount
                })

        return valid_expenses

    except (json.JSONDecodeError, OSError, ValueError):
        messagebox.showerror(
            "File Error",
            "Could not read expenses.json.\n"
            "Please check the file before continuing."
        )
        return []


def save_expenses():
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)
        return True

    except OSError as error:
        messagebox.showerror(
            "Save Error",
            f"Could not save expenses:\n{error}"
        )
        return False


expenses = load_expenses()

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("My Monthly Expense Tracker")
root.geometry("1050x700")
root.minsize(850, 600)
root.configure(bg=BG)

# ---------------- HEADER ----------------
header = tk.Frame(root, bg=BROWN, height=100)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header,
    text="MY EXPENSE TRACKER",
    font=("Arial", 24, "bold"),
    bg=BROWN,
    fg=WHITE
).pack(pady=(18, 5))

tk.Label(
    header,
    text="Track your spending. Manage your budget.",
    font=("Arial", 11),
    bg=BROWN,
    fg="#F4DFC0"
).pack()

# ---------------- SUMMARY CARDS ----------------
summary = tk.Frame(root, bg=BG, padx=20, pady=15)
summary.pack(fill="x")


def make_card(parent, title, color):
    card = tk.Frame(
        parent,
        bg=WHITE,
        padx=15,
        pady=12,
        highlightbackground="#E0D8CC",
        highlightthickness=1
    )

    tk.Label(
        card,
        text=title,
        font=("Arial", 10),
        bg=WHITE,
        fg="#76685B"
    ).pack(anchor="w")

    value = tk.Label(
        card,
        text="₹0.00",
        font=("Arial", 18, "bold"),
        bg=WHITE,
        fg=color
    )
    value.pack(anchor="w", pady=(7, 0))

    return card, value


card1, total_value = make_card(
    summary, "TOTAL SPENDING", BROWN
)
card2, budget_value = make_card(
    summary, "MONTHLY BUDGET", GREEN
)
card3, remaining_value = make_card(
    summary, "BALANCE LEFT", GOLD
)

for card in (card1, card2, card3):
    card.pack(side="left", fill="x", expand=True, padx=6)

budget_value.config(text=f"₹{budget:.2f}")

# ---------------- ADD EXPENSE FORM ----------------
form = tk.LabelFrame(
    root,
    text="  Add a New Expense  ",
    font=("Arial", 12, "bold"),
    bg=BG,
    fg=BROWN,
    padx=15,
    pady=12
)
form.pack(fill="x", padx=26, pady=5)

tk.Label(
    form, text="Expense Name", bg=BG, fg=TEXT
).grid(row=0, column=0, sticky="w", padx=6)

tk.Label(
    form, text="Amount (₹)", bg=BG, fg=TEXT
).grid(row=0, column=1, sticky="w", padx=6)

tk.Label(
    form, text="Category", bg=BG, fg=TEXT
).grid(row=0, column=2, sticky="w", padx=6)

name_entry = tk.Entry(
    form, font=("Arial", 11), width=24
)
name_entry.grid(
    row=1, column=0, padx=6, pady=8, ipady=5
)

amount_entry = tk.Entry(
    form, font=("Arial", 11), width=16
)
amount_entry.grid(
    row=1, column=1, padx=6, pady=8, ipady=5
)

category_box = ttk.Combobox(
    form,
    values=[
        "Food", "Transport", "Shopping",
        "Education", "Bills", "Health", "Other"
    ],
    state="readonly",
    width=17,
    font=("Arial", 11)
)
category_box.set("Food")
category_box.grid(
    row=1, column=2, padx=6, pady=8, ipady=4
)

# ---------------- EXPENSE TABLE ----------------
table_frame = tk.Frame(root, bg=BG, padx=26, pady=10)
table_frame.pack(fill="both", expand=True)

tk.Label(
    table_frame,
    text="Recent Transactions",
    font=("Arial", 14, "bold"),
    bg=BG,
    fg=BROWN
).pack(anchor="w", pady=(0, 8))

columns = ("date", "name", "category", "amount")

table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=8
)

table.heading("date", text="DATE")
table.heading("name", text="EXPENSE")
table.heading("category", text="CATEGORY")
table.heading("amount", text="AMOUNT (₹)")

table.column("date", width=130, anchor="center")
table.column("name", width=280)
table.column("category", width=180, anchor="center")
table.column("amount", width=150, anchor="e")

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview",
    font=("Arial", 10),
    rowheight=29,
    background=WHITE,
    fieldbackground=WHITE
)

style.configure(
    "Treeview.Heading",
    font=("Arial", 10, "bold"),
    background=BROWN,
    foreground=WHITE,
    padding=8
)

style.map(
    "Treeview",
    background=[("selected", GOLD)],
    foreground=[("selected", TEXT)]
)

scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=table.yview
)
table.configure(yscrollcommand=scrollbar.set)

table.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# ---------------- FUNCTIONS ----------------
def update_summary():
    total = sum(item["amount"] for item in expenses)
    remaining = budget - total

    total_value.config(text=f"₹{total:.2f}")

    remaining_value.config(
        text=f"₹{remaining:.2f}",
        fg=GREEN if remaining >= 0 else RED
    )


def add_expense():
    name = name_entry.get().strip()
    amount_text = amount_entry.get().strip()
    category = category_box.get()

    if not name or not amount_text:
        messagebox.showwarning(
            "Missing Details",
            "Please enter an expense name and amount.",
            parent=root
        )
        return

    try:
        amount = float(amount_text)

        if not math.isfinite(amount) or amount <= 0:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Invalid Amount",
            "Enter a valid amount greater than zero.",
            parent=root
        )
        return

    date = datetime.now().strftime("%d-%m-%Y")

    expense = {
        "date": date,
        "name": name,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    if not save_expenses():
        expenses.pop()
        return

    table.insert(
        "",
        "end",
        values=(date, name, category, f"{amount:.2f}")
    )

    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

    update_summary()
    name_entry.focus()


def delete_expense():
    selected = table.selection()

    if not selected:
        messagebox.showinfo(
            "Select Expense",
            "Select a transaction in the table first.",
            parent=root
        )
        return

    rows = [
        (table.index(row), expenses[table.index(row)])
        for row in selected
    ]

    for row in selected:
        table.delete(row)

    for index, _ in sorted(rows, reverse=True):
        expenses.pop(index)

    if not save_expenses():
        expenses.extend([])
        messagebox.showwarning(
            "Warning",
            "Please check expenses.json. The changes may not be saved.",
            parent=root
        )

    update_summary()


def clear_all():
    if not expenses:
        messagebox.showinfo(
            "Information",
            "No expenses to clear.",
            parent=root
        )
        return

    confirm = messagebox.askyesno(
        "Confirm",
        "Delete all recorded expenses?",
        parent=root
    )

    if confirm:
        old_expenses = expenses.copy()
        expenses.clear()

        if not save_expenses():
            expenses.extend(old_expenses)
            return

        for row in table.get_children():
            table.delete(row)

        update_summary()


def change_budget():
    global budget

    new_budget = budget_entry.get().strip()

    try:
        value = float(new_budget)

        if not math.isfinite(value) or value <= 0:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Invalid Budget",
            "Enter a valid budget greater than zero.",
            parent=root
        )
        return

    budget = value
    budget_value.config(text=f"₹{budget:.2f}")

    budget_entry.delete(0, tk.END)
    update_summary()


# ---------------- BUTTONS ----------------
actions = tk.Frame(root, bg=BG, padx=26, pady=12)
actions.pack(fill="x")

tk.Button(
    actions,
    text=" + ADD EXPENSE ",
    command=add_expense,
    bg=BROWN,
    fg=WHITE,
    font=("Arial", 10, "bold"),
    relief="flat",
    padx=12,
    pady=10,
    cursor="hand2"
).pack(side="left", padx=(0, 8))

tk.Button(
    actions,
    text="DELETE SELECTED",
    command=delete_expense,
    bg=RED,
    fg=WHITE,
    font=("Arial", 10, "bold"),
    relief="flat",
    padx=12,
    pady=10,
    cursor="hand2"
).pack(side="left", padx=8)

tk.Button(
    actions,
    text="CLEAR ALL",
    command=clear_all,
    bg="#77716A",
    fg=WHITE,
    font=("Arial", 10, "bold"),
    relief="flat",
    padx=12,
    pady=10,
    cursor="hand2"
).pack(side="left", padx=8)

# ---------------- BUDGET SETTINGS ----------------
budget_frame = tk.Frame(root, bg=BG, padx=26, pady=8)
budget_frame.pack(fill="x")

tk.Label(
    budget_frame,
    text="Set monthly budget (₹):",
    bg=BG,
    fg=TEXT,
    font=("Arial", 10)
).pack(side="left")

budget_entry = tk.Entry(
    budget_frame, width=14, font=("Arial", 10)
)
budget_entry.pack(side="left", padx=8, ipady=4)

tk.Button(
    budget_frame,
    text="Update Budget",
    command=change_budget,
    bg=GOLD,
    fg=TEXT,
    font=("Arial", 10, "bold"),
    relief="flat",
    padx=10,
    pady=6,
    cursor="hand2"
).pack(side="left")

tk.Label(
    root,
    text="Made with Python and Tkinter",
    bg=BG,
    fg=BROWN,
    font=("Arial", 9, "italic"),
    pady=8
).pack()

# ---------------- LOAD SAVED EXPENSES ----------------
for expense in expenses:
    table.insert(
        "",
        "end",
        values=(
            expense["date"],
            expense["name"],
            expense["category"],
            f"{expense['amount']:.2f}"
        )
    )

# Keyboard shortcut: Ctrl+Enter adds an expense
root.bind("<Control-Return>", lambda event: add_expense())

update_summary()
name_entry.focus()
root.mainloop()