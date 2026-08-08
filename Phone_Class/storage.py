# 📁 Storage Manager for Phone Management System v2.0

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CONTACTS_FILE = os.path.join(BASE_DIR, "data", "contacts.json")
CALLS_FILE = os.path.join(BASE_DIR, "data", "calls.json")
MESSAGES_FILE = os.path.join(BASE_DIR, "data", "messages.json")

# storage.py

# Save contacts permanently
def save_contacts(contacts):

    with open(CONTACTS_FILE, "w") as file:

        json.dump(contacts, file, indent=4)

# Load contacts when program starts
def load_contacts():

    with open(CONTACTS_FILE, "r") as file:

        contacts = json.load(file)
        
    return contacts

# Save call history permanently
def save_calls(call_list):
    
    with open(CALLS_FILE, "w") as file:
        
        json.dump(call_list, file, indent=4)

# Load call history when program starts
def load_calls():
    
    with open(CALLS_FILE, "r") as file:
        
        calls = json.load(file)
        
    return calls

# Save message history permanently
def save_messages(message_list):

    with open(MESSAGES_FILE, "w") as file:

        json.dump(message_list , file, indent=4)

# Load message history when program starts   
def load_messages():

    with open(MESSAGES_FILE, "r") as file:

        messages = json.load(file)

    return messages    
