# 📁 Storage Manager for Phone Management System v2.0

import json

# storage.py

# Save contacts permanently
def save_contacts(contacts):
    with open("data/contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

def load_contacts():
    # 1. Open contacts.json
    # 2. Read the JSON data
    # 3. Convert it back into a Python dictionary
    # 4. Return the dictionary
