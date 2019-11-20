import json
from datetime import datetime


GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []

def init():
    global entries
    global next_id
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
        m = -1
        for ii in entries:
            if int(ii['id']) > m:
                m = int(ii['id'])
        next_id = m + 1
    except:
        print('Couldn\'t open', GUESTBOOK_ENTRIES_FILE)
        print('Next_id is set to 0')
        entries = []
        next_id = 0

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    entry = {"author": name, "text": text, "timestamp": time_string, 'id': str(next_id)}
    entries.insert(0, entry) ## add to front of list
    next_id += 1
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def delete_entry(id_value):
    global entries, GUESTBOOK_ENTRIES_FILE
    temp = []
    for ii in entries:
        if ii["id"] != id_value:
            temp.append(ii)
    entries = temp
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

