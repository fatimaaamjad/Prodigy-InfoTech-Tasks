🔐 Caesar Cipher Encryption & Decryption Tool

A simple yet elegant Python GUI application that allows you to encrypt and decrypt text using the Caesar Cipher algorithm.
Built with Tkinter, this tool features a clean dark-themed interface with live text input and output display.

🧠 About the Project

The Caesar Cipher is one of the oldest and simplest encryption techniques.
It works by shifting each letter of a given text by a fixed number of positions in the alphabet.
This project provides both encryption and decryption functions through an intuitive graphical interface.

✨ Features

✅ User-friendly GUI using Tkinter
✅ Encrypt and decrypt messages instantly
✅ Handles both uppercase and lowercase letters
✅ Keeps numbers and special symbols unchanged
✅ Input validation for shift values
✅ Dark mode UI with colorful action buttons

🧩 How It Works

Enter the text you want to encrypt or decrypt.

Input a shift value (0–25).

Click Encrypt or Decrypt.

The output will be displayed instantly below the buttons.

Use Clear to reset all fields.

🧾 Code Explanation
🔸 Encryption Function
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


Shifts letters by a given shift value

Preserves the case (upper/lower)

Leaves spaces and symbols unchanged

🔸 Decryption Function
def decrypt(text, shift):
    return encrypt(text, -shift)


Simply calls the encryption function with a negative shift

📁 File Structure
Caesar-Cipher-GUI/
│
├── main.py          # The main Caesar Cipher GUI program
├── README.md        # Project documentation

💡 Example
Action	Input	Shift	Output
Encrypt	Hello World	3	Khoor Zruog
Decrypt	Khoor Zruog	3	Hello World
🧑‍💻 Technologies Used

Python 3

Tkinter (GUI Library)

❤️ Credits

Developed by Your Name

Feel free to fork, star ⭐, and improve this project!
