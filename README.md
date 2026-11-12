# 📱 PocketOS — Phone Management System

A Python-based **Phone Management System** that simulates the core functionality of a smartphone through a modular, menu-driven console application.

PocketOS demonstrates **Object-Oriented Programming, multiple inheritance, modular programming, JSON file handling, persistent data storage, battery management, input validation, and practical software design**.

---

# 🚀 Current Version

## PocketOS v2.0.0 — File Handling & Battery System Update

Version 2.0.0 introduces persistent JSON-based data storage, improved battery management, enhanced module functionality, and a more complete smartphone-like experience.

---

# ✨ Features

## 📱 Phone System

* 🔐 Password Authentication
* 📋 Main Menu Navigation
* 📄 Phone Information
* 🕐 Real-Time Clock Display
* 🔋 Centralized Battery Status

---

## 📇 Contact Manager

* ➕ Add Contact
* 👀 View Contacts
* 🔍 Search Contact
* ✏️ Edit Contact
* 🗑️ Delete Contact
* 🧹 Clear All Contacts
* 📞 Phone Number Validation
* 🔎 Duplicate Contact and Number Checking
* 🔤 Case-Insensitive Contact Handling

---

## 📞 Call Manager

* 📲 Make Calls
* 👤 Call Using Contact Name
* 📞 Call Using Phone Number
* ❓ Call Unknown Numbers
* 💾 Save Unknown Numbers as Contacts
* 📜 View Call History
* 🗑️ Delete Individual Call Records
* 🧹 Clear Call History
* 🔤 Case-Insensitive Contact Lookup

---

## 💬 Message Manager

* 📨 Send Messages
* 📜 View Message History
* 🔍 Search Messages
* 🗑️ Delete Individual Messages
* 🧹 Clear Message History
* 👤 Contact-Based Messaging
* 🔤 Case-Insensitive Contact Lookup

---

## 🎵 Music Manager

* ➕ Add Songs
* 👀 View Playlist
* ▶️ Play Songs
* ⏹️ Stop Music
* 🗑️ Delete Songs
* 🎵 Track Currently Playing Song
* 💾 Persistent Playlist Storage

---

## 🧮 Calculator Manager

### ➗ Arithmetic Operations

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* %️⃣ Modulus
* ⬜ Square
* 🧊 Cube

### 📜 Calculator History

* 👀 View Calculation History
* 🗑️ Delete Calculation Records
* 🧹 Clear Calculation History

---

## 🎮 Game Manager

Includes built-in console games for entertainment:

* ✊ Rock Paper Scissors
* 🍀 Lucky Fortune
* 🎯 Hangman

---

## 🔋 Battery Manager

* 🔋 Display Current Battery Percentage
* ⚡ Charge Battery
* 🔄 Battery Consumption Management
* ⚠️ Low Battery Warning
* 🛡️ Battery Protection
* 📴 Automatic Phone Shutdown at 0%
* ✅ Battery Status Checking
* 🕐 Battery Status Alongside Real-Time Clock

The battery system is centralized through the `BatteryManager` and is shared across the phone application.

---

## ⚙️ Settings

* 🔐 Change Password
* 🔄 Reset Application Data
* 📊 Show System Status
* 📱 View Phone Information
* 🔒 Password Protection

---

# 💾 File Handling & JSON Persistence

PocketOS uses **JSON files for persistent data storage**.

Important application data is saved to files so that information can be restored when the program is started again.

### Stored Data

* 📇 Contact information
* 📞 Call history
* 💬 Message history
* 🧮 Calculator history
* 🔋 Battery state
* 🎵 Music playlist and current song
* 🔐 Password data

The `password.json` file is used for persistent password storage. **Its contents are intentionally not shown in screenshots for security reasons.**

---

# 🔋 Battery System

PocketOS uses a centralized `BatteryManager` to control battery-related operations across the application.

Different phone activities can consume battery, while charging restores the battery level.

The system provides:

* 🔋 Battery monitoring
* ⚡ Charging
* 🔄 Battery consumption
* ⚠️ Low-battery warnings
* 🛡️ Protection against negative battery values
* 📴 Automatic shutdown when battery reaches 0%
* 🕐 Battery and time status information

---

# 🧱 Object-Oriented Design

PocketOS is designed using Object-Oriented Programming principles.

The main `Phone` class combines the different application managers using **multiple inheritance**, while individual managers are responsible for their own functionality.

### Major Manager Classes

* `Phone`
* `ContactManager`
* `CallManager`
* `MessageManager`
* `CalculatorManager`
* `GameManager`
* `MusicManager`
* `BatteryManager`
* `SettingsManager`

This modular structure keeps individual features separated and makes the system easier to maintain and extend.

---

# 🧠 Concepts Demonstrated

* 🏛️ Classes and Objects
* 🔧 Constructors
* 🧬 Multiple Inheritance
* 🧩 Composition
* 🔒 Encapsulation
* 📦 Modular Programming
* 📋 Lists
* 📖 Dictionaries
* 🔁 Loops
* 🌿 Conditional Statements
* ⚙️ Methods
* ✔️ Input Validation
* 💾 File Handling
* 🗂️ JSON Data Storage
* 🛡️ Exception Handling
* 🔄 Persistent Data Management

---

# 📂 Project Structure

```text
PocketOS/
│
├── main.py
│
├── modules/
│   ├── phone_class.py
│   ├── contacts.py
│   ├── calls.py
│   ├── messages.py
│   ├── calculator.py
│   ├── games.py
│   ├── battery.py
│   ├── music.py
│   ├── settings.py
│   └── storage.py
│
├── data/
│   ├── battery.json
│   ├── calculator.json
│   ├── calls.json
│   ├── contacts.json
│   ├── messages.json
│   ├── music.json
│   └── password.json
│
├── Screenshots/
│
├── .gitignore
│
└── README.md
```

### 📦 Module Organization

Each manager is maintained as a separate Python module.

The `storage.py` module handles JSON-based data loading and saving, while `phone_class.py` integrates the different managers into the main phone system.

---

# 📸 Screenshots

The `Screenshots/` folder contains visual demonstrations of PocketOS modules, functionality, and persistent data.

**The complete screenshot documentation will be added here with the final screenshot layout.**

---

# 🧪 Testing

PocketOS was tested after the implementation of the file-handling and battery-system updates.

Testing included:

* 📇 Contact operations
* 📞 Call operations
* 💬 Message operations
* 🎵 Music operations
* 🧮 Calculator operations
* 🎮 Game functionality
* 🔋 Battery consumption
* ⚡ Battery charging
* ⚠️ Low-battery behavior
* 📴 Automatic shutdown
* 💾 JSON data persistence
* 🔐 Password functionality
* ⚙️ Settings operations
* 📋 Module navigation
* 🔤 Case-insensitive contact handling
* 🧪 Full-system testing and bug fixing

---

# 🛠️ Technologies Used

* **Python**
* **Object-Oriented Programming**
* **Multiple Inheritance**
* **JSON**
* **File Handling**
* **Persistent Storage**
* **Modular Programming**
* **Exception Handling**
* **Command-Line Interface (CLI)**

---

# ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Anju-AI-2026/PocketOS.git
```

### 2. Open the project directory

```bash
cd PocketOS
```

### 3. Run PocketOS

```bash
python main.py
```

### 4. Authenticate

Enter the configured password to access the PocketOS main menu.

---

# 📌 Version History

## v1.0.0 — Initial Release

The first complete version of the Phone Management System.

Included:

* 📱 Phone Navigation
* 📇 Contacts
* 📞 Calls
* 💬 Messages
* 🎵 Music
* 🧮 Calculator
* 🎮 Games
* 🔋 Basic Battery Management
* 🔐 Password Authentication
* 🎨 Console Interface

---

## v2.0.0 — File Handling & Battery System Update

Major improvements introduced:

* 💾 JSON-based persistent data storage
* 📇 Persistent contacts
* 📞 Persistent call history
* 💬 Persistent message history
* 🧮 Persistent calculator history
* 🎵 Persistent music data
* 🔋 Improved battery management
* ⚠️ Low-battery warnings
* 📴 Automatic shutdown at 0%
* 🛡️ Battery protection
* 🕐 Real-time status information
* ✏️ Contact editing
* 🔐 Password management
* 🔄 Application data reset
* 📊 System status
* 🧪 Full-system testing and bug fixing

---

# 🎯 Project Purpose

PocketOS was developed as a practical Python project to strengthen programming and software engineering fundamentals through a progressively developed application.

The project demonstrates the progression:

```text
Python Fundamentals
        ↓
Object-Oriented Programming
        ↓
Modular Programming
        ↓
Application Development
        ↓
File Handling
        ↓
JSON Persistence
        ↓
System-Level Application Logic
```

The goal is to build a stronger foundation for developing larger and more advanced software systems in the future.

---

# 📦 Release

### PocketOS v2.0.0

**File Handling & Battery System Update**

This release represents the completion of the **File Handling phase of PocketOS v2**, bringing persistent data storage, improved battery management, enhanced functionality, and system-wide testing to the project.

---

# 👩‍💻 Author

**Anjali Sangannavar**

A Python-based portfolio project developed to strengthen practical **Computer Science and Software Engineering fundamentals**.

The `Screenshots/` folder contains 23 screenshots demonstrating the major modules, features, and JSON-based data persistence of PocketOS.

📸 **[View the Complete PocketOS Screenshot Gallery →](Screenshots/README.md)**

Copyright © 2026 Anjali Ramesh Sangannavar. All rights reserved.


