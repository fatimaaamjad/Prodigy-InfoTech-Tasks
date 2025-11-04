import tkinter as tk
from tkinter import messagebox

# --- Encryption & Decryption Functions ---
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # only shift letters
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # keep non-letters unchanged
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# --- GUI Functions ---
def handle_encrypt():
    text = entry_text.get("1.0", tk.END).strip()
    shift = entry_shift.get()
    if not shift.isdigit():
        messagebox.showerror("Invalid Input", "Shift value must be a number!")
        return
    shift = int(shift)
    encrypted_text = encrypt(text, shift)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, encrypted_text)

def handle_decrypt():
    text = entry_text.get("1.0", tk.END).strip()
    shift = entry_shift.get()
    if not shift.isdigit():
        messagebox.showerror("Invalid Input", "Shift value must be a number!")
        return
    shift = int(shift)
    decrypted_text = decrypt(text, shift)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, decrypted_text)

def clear_all():
    entry_text.delete("1.0", tk.END)
    entry_shift.delete(0, tk.END)
    output_box.delete("1.0", tk.END)

# --- MAIN WINDOW ---
root = tk.Tk()
root.title("Caesar Cipher Tool 🔐")
root.geometry("500x400")
root.config(bg="#1e1e2f")

# --- HEADING ---
tk.Label(root, text="Caesar Cipher Encryption / Decryption", 
         font=("Helvetica", 16, "bold"), bg="#1e1e2f", fg="#f4c430").pack(pady=10)

# --- INPUT TEXT ---
tk.Label(root, text="Enter your text:", bg="#1e1e2f", fg="white", font=("Arial", 12, "bold")).pack()
entry_text = tk.Text(root, height=5, width=50, font=("Consolas", 11))
entry_text.pack(pady=5)

# --- SHIFT VALUE ---
tk.Label(root, text="Shift Value (0–25):", bg="#1e1e2f", fg="white", font=("Arial", 12, "bold")).pack()
entry_shift = tk.Entry(root, width=10, font=("Consolas", 11), justify="center")
entry_shift.pack(pady=5)

# --- BUTTONS ---
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=10)
btn_encrypt = tk.Button(frame, text="Encrypt", command=handle_encrypt, bg="#4CAF50", fg="white", width=10, font=("Arial", 10, "bold"))
btn_encrypt.grid(row=0, column=0, padx=10)

btn_decrypt = tk.Button(frame, text="Decrypt", command=handle_decrypt, bg="#2196F3", fg="white", width=10, font=("Arial", 10, "bold"))
btn_decrypt.grid(row=0, column=1, padx=10)

btn_clear = tk.Button(frame, text="Clear", command=clear_all, bg="#f44336", fg="white", width=10, font=("Arial", 10, "bold"))
btn_clear.grid(row=0, column=2, padx=10)

# --- OUTPUT BOX ---
tk.Label(root, text="Result:", bg="#1e1e2f", fg="white", font=("Arial", 12, "bold")).pack()
output_box = tk.Text(root, height=5, width=50, font=("Consolas", 11))
output_box.pack(pady=5)

# --- RUN LOOP ---
root.mainloop()
