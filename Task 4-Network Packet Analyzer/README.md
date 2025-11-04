🧠 Safe In-App Keystroke Logger (Python + Tkinter)
📘 Overview

This project is a safe and educational in-app keystroke logger built using Python and Tkinter.
It records only the keystrokes typed inside its own window, making it ideal for learning, testing, or GUI event handling demonstrations.

⚠️ Ethical Notice:
This program is designed strictly for educational and self-testing purposes.
It does not capture any system-wide input or background keystrokes — only those entered in the app’s text area.
Using this for recording other people’s keystrokes without consent is unethical and illegal.

🧩 Features

✅ Logs only in-app keystrokes — never outside the window

✅ Displays real-time typed text in a Tkinter Text widget

✅ Option to choose your own log file for saving keystroke data

✅ Start and Stop logging anytime

✅ Adds timestamp to every key event

✅ Includes a clear button and status bar

✅ Displays a built-in consent message at launch

⚙️ How It Works

When launched, the app shows a text box and control buttons.

The user chooses a file to save the keystroke logs.

After pressing Start Logging, the program begins recording all key events that occur inside the text area.

Each log entry includes:

YYYY-MM-DD HH:MM:SS UTC | keysym=<KeyName> | char='<TypedCharacter>'


Press Stop Logging to pause, or Clear Text to reset the input area.

🧠 Example Log Output
IN-APP KEYLOG (ONLY KEYS PRESSED INSIDE THIS APP)
User consent: You are using this program to record your own keystrokes.
Do NOT use this for other people's keystrokes without consent.

2025-11-03 18:24:12 UTC | keysym=H | char='H'
2025-11-03 18:24:13 UTC | keysym=e | char='e'
2025-11-03 18:24:14 UTC | keysym=l | char='l'
2025-11-03 18:24:15 UTC | keysym=l | char='l'
2025-11-03 18:24:16 UTC | keysym=o | char='o'
2025-11-03 18:24:17 UTC | keysym=space | char=' '
2025-11-03 18:24:18 UTC | keysym=W | char='W'
2025-11-03 18:24:19 UTC | keysym=o | char='o'
2025-11-03 18:24:20 UTC | keysym=r | char='r'
2025-11-03 18:24:21 UTC | keysym=l | char='l'
2025-11-03 18:24:22 UTC | keysym=d | char='d'

🧩 Technologies Used

Python 3.x

Tkinter — for GUI design

datetime — for timestamp generation

filedialog / messagebox — for user interactions and file selection

🚀 How to Run

Make sure Python 3 is installed on your system.

Save this script as in_app_logger.py.

Run it using:

python in_app_logger.py


Choose a file to store logs, start logging, and begin typing in the app window.

🛡️ Ethics & Safety

This project is meant only for educational and self-monitoring purposes.
Never use it for capturing other users’ input without explicit permission — doing so violates privacy laws and ethical guidelines.

👨‍💻 Author

Developed by: Fatima Amjad
