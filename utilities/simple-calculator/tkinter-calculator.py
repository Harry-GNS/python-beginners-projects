import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

def evaluate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Simple - Calculator")
root.geometry("400x500")
root.config(bg="#282c35")  

entry = tk.Entry(root, width=20, font=('Arial', 20), justify=tk.RIGHT, bd=10)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=20)  

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(
        root, text=button, padx=20, pady=20, font=('Arial', 16),
        command=lambda b=button: button_click(b) if b != '=' else evaluate(),
        bg="#61dafb", 
        fg="#282c35"   
    ).grid(row=row_val, column=col_val, sticky="nsew")  
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(
    root, text='C', padx=20, pady=20, font=('Arial', 16),
    command=clear_entry, bg="#ff6b6b", fg="#282c35"
).grid(row=row_val, column=col_val, sticky="nsew")
col_val += 1
tk.Button(
    root, text='⌫', padx=20, pady=20, font=('Arial', 16),
    command=backspace, bg="#ff6b6b", fg="#282c35"
).grid(row=row_val, column=col_val, sticky="nsew")

for i in range(1, 5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Main loop
root.mainloop()