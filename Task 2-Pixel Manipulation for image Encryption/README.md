🔐 Pixel Image Encryption Tool

An interactive Python Tkinter application that encrypts and decrypts images at the pixel level using a simple XOR cipher.
Fast, lightweight, and visually intuitive — perfect for understanding the fundamentals of image cryptography.

🧠 Overview

This project demonstrates pixel manipulation encryption using the XOR operation.
Each pixel’s RGB values are modified with a user-defined key (0–255), producing a visually scrambled version of the image.
When decrypted with the same key, the image returns to its original state — perfectly reversible and lossless.

⚡ Features

🔒 Encrypt / Decrypt any image file (PNG, JPG, BMP, GIF, TIFF)

🧮 XOR-based algorithm (fast and reversible)

🧭 Dual image preview (original vs processed)

⚙️ Progress bar & threading for smooth UI

💾 Save & reset functions for quick workflow

🎨 Clean, minimal, and responsive GUI

🧩 How It Works

Select an image via 📂 Select Image.

Enter a numeric key (range 0–255).

Click 🔒 Encrypt to scramble pixels.

Use the same key and press 🔓 Decrypt to restore.

Save the output or reset the workspace anytime.

🧾 Core Logic
def xor_image(img, key):
    img = img.convert("RGBA")
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            r, g, b, a = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key, a)
    return img


Applies an XOR operation to every pixel.

The process is reversible — applying XOR twice with the same key restores the image.

🧰 Technologies Used
Tool	Purpose
Python 3	Core language
Tkinter	Graphical user interface
Pillow (PIL)	Image handling & processing
Threading	Background operations
⚙️ Installation

Install the required dependency before running:

pip install pillow


Run the tool:

python main.py

📁 Project Structure
Pixel-Image-Encryption-Tool/
│
├── PixelManipulationForImageEncrypttion.py          # Main source code
└── README.md        # Documentation

⚠️ Important Notes

The same XOR key must be used for both encryption and decryption.

This method is for educational purposes only — not suitable for real-world security.

Large images may take longer to process.
💡 Example
Operation	Input	Key	Output
Encrypt	photo.jpg	100	Scrambled image
Decrypt	Scrambled image	100	Original restored
💖 Credits

Developed by Fatima Amjad

If you found this project helpful, please ⭐ it and share it!
