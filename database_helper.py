import sqlite3
from pathlib import Path
import os
import logging
import sys
import shutil


def execute_sql(db_name, *sql):
    db_path = 'db/' + db_name + '.db'
    db_file = Path(db_path)
    if not db_file.is_file():
        logging.getLogger('database').warning("execute_sql: Calling %s, but doesn't exist", db_path)
        create_db(db_name)
    db_con = sqlite3.connect(db_path)
    c = db_con.cursor()
    for command in sql:
        c.execute(command)
        logging.getLogger('sql').info(c.fetchone())
    db_con.commit()
    db_con.close()


def create_table(db_name, table_name, *values):
    db_values = ''
    i = 1
    for element in values:
        if i == 1:
            db_values = element
        else:
            db_values += ', ' + element
        i += 1
    try:
        execute_sql(db_name,"CREATE TABLE {} ({})".format(table_name, db_values))
        logging.getLogger('database').info("create_table: New table {} in database {} created!".format(table_name, db_name))
    except sqlite3.OperationalError:
        logging.getLogger('database').error("create_table: Couldn't create table!")


def delete_table(db_name, table_name):
    execute_sql(db_name, "DROP TABLE {}".format(table_name))
    # toDO catch Operational Error


def insert_data(db_name, table_name, *values):
    pass


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


def purge_dbs(ask=True):
    if not ask:
        if os.path.exists('db'):
            shutil.rmtree('db')
            logging.getLogger('database').info("purge_dbs: All databases were deleted")
        else:
            logging.getLogger('database').info("purge_dbs: No databases to delete")
        return
    in1 = input("Are you sure to delete ALL databases? [y/N]")
    if not in1 == 'y' or not in1 == 'Y':
        if os.path.exists('db'):
            shutil.rmtree('db')
            logging.getLogger('database').info("purge_dbs: All databases were deleted")
        else:
            logging.getLogger('database').info("purge_dbs: No databases to delete")