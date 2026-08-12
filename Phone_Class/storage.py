# 📁 Storage Manager for Phone Management System v2.0

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CONTACTS_FILE = os.path.join(BASE_DIR, "data", "contacts.json")
CALLS_FILE = os.path.join(BASE_DIR, "data", "calls.json")
MESSAGES_FILE = os.path.join(BASE_DIR, "data", "messages.json")
CALCULATOR_FILE = os.path.join(BASE_DIR, "data", "calculator.json")
BATTERY_FILE = os.path.join(BASE_DIR, "data", "battery.json")
MUSIC_FILE = os.path.join(BASE_DIR, "data", "music.json")

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

# Save calculation history permanently
def save_calculations(calculator_history):

    with open(CALCULATOR_FILE, "w") as file:

        json.dump(calculator_history, file, indent=4)

# Load calculation history when program starts
def load_calculations():

    with open(CALCULATOR_FILE, "r") as file:
        
        calculations = json.load(file)

    return calculations    

# Save battery level permanently
def save_battery(level):

    with open(BATTERY_FILE, "w") as file:

        json.dump({"level": level}, file, indent=4)  

# Load battery level when program starts
def load_battery():

    with open(BATTERY_FILE, "r") as file:
        
        battery_data = json.load(file)

    return battery_data["level"]

# Save music playlist and last played song permanently
def save_music(play_list, current_song):

    with open(MUSIC_FILE, "w") as file:

        json.dump({
            "playlist": play_list,
            "current_song": current_song
            
        }, file, indent=4)
