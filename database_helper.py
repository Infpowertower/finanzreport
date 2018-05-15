import sqlite3
from pathlib import Path
import os
import logging


def create_db(db_name):
    if not os.path.exists('db'):
        os.makedirs('db')
    db_name = db_name+".db"
    db_path = 'db/' + db_name
    db_file = Path(db_path)
    if db_file.is_file():
        logging.getLogger('database').warning('create_db: Database exists!')
    else:
        with sqlite3.connect(db_path) as db:
            pass
        logging.getLogger('database').info('create_db: Database %s created', db_name)


def delete_db(db_name):
    db_name = db_name+".db"
    db_path = 'db/' + db_name
    db_file = Path(db_path)
    if db_file.is_file():
        os.remove(db_path)
        logging.getLogger('database').info('delete_db: Database %s deleted', db_name)
    else:
        logging.getLogger('database').warning("delete_db: Database %s doesn't exist!", db_path)