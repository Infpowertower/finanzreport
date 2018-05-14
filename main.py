import sqlite3
from pathlib import Path
import os

def create_db(db_name):
    db_name = db_name+".db"
    db_file = Path(db_name)
    print(db_file)
    if (db_file.is_file()):
        print("ERROR - Database exists!")
    else:
        with sqlite3.connect(db_name) as db:
            pass

def delete_db(db_name):
    db_name = db_name+".db"
    db_file = Path(db_name)
    print(db_file)
    if (db_file.is_file()):
        os.remove(db_name)
    else:
        print("ERROR - Database doesn't exist!")


if (__name__ == "__main__"):
    delete_db("settings")