import sqlite3
from pathlib import Path
import os
import logging
import sys


def execute_sql(db_name, *sql):
    """
    Execute raw sql statements in a database.
    :param db_name: String - name of the database. Path and data type are added automatically. Example: settings
    :param sql: String(s) - list of sql statement to be executed.
    :return:
    """
    db_path = 'log/' + db_name + '.db'
    db_file = Path(db_path)
    if not db_file.is_file():
        logging.getLogger('database').warning("execute_sql: Calling %s, but doesn't exist", db_path)
        create_db(db_name)
    db_con = sqlite3.connect(db_path)
    c = db_con.cursor()
    for command in sql:
        c.execute(command)
        print(c.fetchone())
    db_con.commit()
    db_con.close()


def create_table(db_name, table_name, *values):
    """

    :param db_name: String- name of the database. Path and data type are added automatically. Example: settings
    :param table_name: String
    :param values: String - Have to be entered in Form "name data type". Example: "name text".
    Primary key entered with "Primary key (example)" - no data type needed as it already should be stated before.
    :return:
    """
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
        logging.getLogger('database').error("create_table: Table already exists!")
    except:
        logging.getLogger('database').critical("create_table: Unexpected error: {}".format(sys.exc_info()[0]))
        raise


def create_db(db_name):
    """

    :param db_name:
    :return:
    """
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
    """

    :param db_name:
    :return:
    """
    db_name = db_name+".db"
    db_path = 'db/' + db_name
    db_file = Path(db_path)
    if db_file.is_file():
        os.remove(db_path)
        logging.getLogger('database').info('delete_db: Database %s deleted', db_name)
    else:
        logging.getLogger('database').warning("delete_db: Database %s doesn't exist!", db_path)