# Task 3: Password Complexity Checker

## Overview

This project implements a **password complexity checker** to assess the strength of a password based on multiple criteria such as length, uppercase and lowercase letters, numbers, special characters, and avoidance of common passwords.

---

## 🔐 Features

- Evaluates password strength as **Strong**, **Moderate**, or **Weak**
- Provides detailed feedback on password criteria
- Offers suggestions to improve weak passwords
- Uses colored output for better visualization:
  - ✅ **Green** for Strong
  - ⚠️ **Yellow** for Moderate
  - ❌ **Red** for Weak

---

## 🛠️ How It Works

- **Password Length Check**: Ensures the password has at least 8 characters
- **Uppercase and Lowercase Check**: Verifies the presence of both letter cases
- **Digit Check**: Ensures the password contains at least one number
- **Special Character Check**: Validates the inclusion of at least one special symbol
- **Blacklist Check**: Compares the password against a list of common and insecure passwords

> 💡 Note: A combination of all criteria results in a stronger password.

---

## 📦 Requirements

- Python 3.x

Run the script using:
```
python password_checker.py
```

---

## 🚀 How to Run

1. Run the Python script using the command above.
2. Enter your password when prompted.
3. View the evaluation and suggestions (if any).

---

## 💡 Suggestions for Improvement

- Implement a GUI using Tkinter for better user interaction.
- Add a password generator to suggest strong passwords.

---

## 👨‍💻 Developed By

**Aswanth K P**  
_ProDigy Infotech Internship Project_

---

## ⚠️ Disclaimer

This tool is designed for educational purposes and basic password strength assessment. It is not intended for evaluating the security of sensitive passwords.
