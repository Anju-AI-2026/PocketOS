# 📱 Phone Management System (Python OOP)

# 📖 Overview

The **Phone Management System** is a console-based Python project developed using Object-Oriented Programming (OOP) principles. It simulates the basic functionalities of a smartphone by organizing each application into separate manager classes.

The project focuses on writing clean, modular, reusable, and maintainable code while strengthening core Python OOP concepts.

---

# ✨ Features

## 📱 Phone

* 🔐 Password Authentication
* 📄 Display Phone Details
* 📋 Main Menu Navigation

---

## 📇 Contact Manager

* ➕ Add Contact
* 👀 View All Contacts
* 🔍 Search Contact
* 🗑️ Delete Contact
* 🧹 Clear All Contacts
* 📋 Contact Menu

---

## 📞 Call Manager

* 📲 Make a Call
* 📜 View Call History
* 🗑️ Delete Call History
* 🧹 Clear Call History
* 📋 Call Menu

---

## 💬 Message Manager

* 📨 Send Message
* 📜 View Message History
* 🗑️ Delete Message History
* 🧹 Clear Message History
* 📋 Message Menu

---

## 🎵 Music Manager

* ▶️ Play Music
* 🎶 Show Playlist
* ⏹️ Stop Music
* ➕ Add Song
* 🗑️ Delete Song
* 📋 Music Menu

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

* 👀 View Calculator History
* 🧹 Clear Calculator History

### 📋 Calculator Menu

---

## 🎮 Game Manager

* 🎲 Game Menu
* *(Games will be added in future versions.)*

---

## 🔋 Battery Manager

* 🔋 Show Current Battery Percentage
* ⚡ Charge Battery
* 🛡️ Battery Protection (prevents battery level from going below 0%)
* ⚠️ Low Battery Warning
* 🔄 Battery Consumption Management
* ✅ Battery Status Checking
* 📋 Battery Manager Menu

---

# 🏗️ Project Structure

```text
Phone
│
├── ContactManager
├── CallManager
├── MessageManager
├── MusicManager
├── CalculatorManager
├── GameManager
└── BatteryManager
```

Each manager is responsible for a single module, making the project modular, maintainable, and easy to expand.

---

# 🧠 OOP Concepts Used

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

---

# 💾 Runtime Data Management

The application stores data during execution using Python collections.

### 📇 Contacts

* Contact Name
* Phone Number

### 📞 Call History

* Contact Name
* Phone Number
* Call Type

### 💬 Message History

* Contact Name
* Phone Number
* Message Content

### 🧮 Calculator History

* Operation
* Expression
* Answer

---

# 🔋 Battery Management

Battery functionality has been separated into a dedicated **BatteryManager** class.

It is responsible for:

* 🔋 Monitoring the current battery level.
* ⚡ Charging the battery.
* 🔄 Managing battery consumption after different phone activities.
* 🛡️ Preventing the battery level from becoming negative.
* ⚠️ Displaying low battery warnings.
* 📱 Providing a centralized battery system shared across the entire phone application.

---

# 🚀 Future Improvements

* 💾 File Handling
* 🗂️ Persistent Data Storage
* 🔑 Password Change Feature
* 🎵 Advanced Music Library Management
* 🎮 Games
* ❤️ Battery Health Monitoring
* 🌙 Power Saving Mode
* ⚠️ Exception Handling
* 🖥️ Graphical User Interface (GUI)

---

# 🎯 Purpose

This project was developed to practice real-world Python programming by applying Object-Oriented Programming concepts in a structured smartphone simulation.

The goal is to build the project incrementally while following clean coding practices and software design principles.

---

## 📌 Current Version

**✅ Version 1 — Core Console Application**

