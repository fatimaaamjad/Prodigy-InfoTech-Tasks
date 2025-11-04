import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength():
    password = entry.get()
    strength = 0
    feedback = ""

    # Criteria checks
    if len(password) < 6:
        feedback = "Password too short! Minimum 6 characters required."
    else:
        if re.search(r"[a-z]", password):
            strength += 1
        if re.search(r"[A-Z]", password):
            strength += 1
        if re.search(r"[0-9]", password):
            strength += 1
        if re.search(r"[@$!%*?&#]", password):
            strength += 1

        # Strength evaluation
        if strength == 1:
            feedback = "Weak: Add uppercase, numbers, and symbols."
        elif strength == 2:
            feedback = "Moderate: Try adding numbers or symbols."
        elif strength == 3:
            feedback = "Strong: Add one more type (symbol/number) for maximum security."
        elif strength == 4:
            feedback = "Very Strong: Excellent password!"

    result_label.config(text=feedback, fg="green" if strength >= 3 else "red")

# GUI setup
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("400x250")
root.config(bg="#e6f2ff")

title_label = tk.Label(root, text="🔒 Password Strength Checker", font=("Arial", 14, "bold"), bg="#e6f2ff")
title_label.pack(pady=10)

entry_label = tk.Label(root, text="Enter your password:", bg="#e6f2ff", font=("Arial", 10))
entry_label.pack()

entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=check_password_strength, bg="#4da6ff", fg="white", font=("Arial", 10, "bold"))
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11, "bold"), bg="#e6f2ff")
result_label.pack(pady=10)

root.mainloop()
