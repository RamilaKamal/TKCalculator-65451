import tkinter as tk
from tkinter import messagebox

# --- Constants ---
TITLE_FONT = ("Arial", 16, "bold")
ENTRY_FONT = ("Arial", 12)
BUTTON_FONT = ("Arial", 14, "bold")
RESULT_FONT = ("Arial", 12)

WINDOW_SIZE = "400x350"


# --- Functions ---
def calculate(operation):
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())

        operations = {
            "add": num1 + num2,
            "subtract": num1 - num2,
            "multiply": num1 * num2,
            "divide": None if num2 == 0 else num1 / num2
        }

        if operation == "divide" and num2 == 0:
            messagebox.showerror("Math Error", "Cannot divide by zero.")
            return

        result = operations[operation]
        result_label.config(text=f"Result: {result:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


def create_button(parent, text, operation):
    return tk.Button(
        parent, text=text, width=5, height=2, font=BUTTON_FONT,
        command=lambda: calculate(operation)
    )


# --- Main window ---
root = tk.Tk()
root.title("Simple Calculator")
root.geometry(WINDOW_SIZE)
root.resizable(False, False)

# Title label
tk.Label(root, text="Simple Calculator", font=TITLE_FONT).pack(pady=30)

# Frame for entries
entry_frame = tk.Frame(root)
entry_frame.pack(pady=15)

num1_entry = tk.Entry(entry_frame, width=15, font=ENTRY_FONT)
num1_entry.grid(row=0, column=0, padx=10)

num2_entry = tk.Entry(entry_frame, width=15, font=ENTRY_FONT)
num2_entry.grid(row=0, column=1, padx=10)

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

buttons = [
    ("+", "add"),
    ("-", "subtract"),
    ("×", "multiply"),
    ("÷", "divide")
]

for i, (symbol, op) in enumerate(buttons):
    btn = create_button(button_frame, symbol, op)
    btn.grid(row=0, column=i, padx=8, pady=8)

# Result Label
result_label = tk.Label(root, text="Result: ", font=RESULT_FONT)
result_label.pack(pady=10)

root.mainloop()
