# 📁 Storage Manager for Phone Management System v2.0

import json

# storage.py

# Save contacts permanently
def save_contacts(contacts):
    
    with open("data/contacts.json", "w") as file:
        
        json.dump(contacts, file, indent=4)


# Load contacts when program starts
def load_contacts():
    
    with open("data/contacts.json", "r") as file:
        
        contacts = json.load(file)
        
    return contacts
