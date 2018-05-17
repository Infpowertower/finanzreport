import sqlite3
from pathlib import Path
import os
import logging
import sys
import shutil


def execute_sql(db_name, sql):
    """
    Execute raw sql statements in a database.
    :param db_name: String - name of the database. Path and data type are added automatically. Example: settings
    :param sql: String(s) - list of sql statement to be executed.
    :return:
    """
    db_path = 'db/' + db_name + '.db'
    db_file = Path(db_path)
    if not db_file.is_file():
        logging.getLogger('database').warning("execute_sql: Calling %s, but doesn't exist", db_path)
        create_db(db_name)
    db_con = sqlite3.connect(db_path)
    c = db_con.cursor()
    c.execute(sql)
    output = c.fetchone()
    logging.getLogger('sql').info(output)
    db_con.commit()
    db_con.close()
    return output


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
        execute_sql(db_name, "CREATE TABLE {} ({})".format(table_name, db_values))
        logging.getLogger('database').info("create_table: New table {} in database {} created!".format(table_name, db_name))
    except sqlite3.OperationalError:
        logging.getLogger('database').error("create_table: Couldn't create table!")


def delete_table(db_name, table_name):
    try:
        execute_sql(db_name, "DROP TABLE {}".format(table_name))
        log("delete_table: Deleted {} out of {}".format(table_name, db_name))
    except sqlite3.OperationalError as err:
        log("delete_table: {}".format(err), 'error')
    # toDO catch Operational Error


def insert_data(db_name, table_name, *values):
    db_values = ''
    i = 1
    for element in values:
        if i == 1:
            db_values = convert_elem(element)
        else:
            db_values += ', ' + convert_elem(element)
        i += 1
    try:
        execute_sql(db_name, "INSERT INTO {} VALUES ({});".format(table_name, db_values))
        logging.getLogger('database').info("insert_data: Data inserted in database {} table {}".format(db_name, table_name))
    except sqlite3.OperationalError as err:
        logging.getLogger('database').error("insert_data: {}".format(err))
    pass


def convert_elem(elem):
    if type(elem) is str:
        elem = '"' + elem + '"'
    else:
        elem = str(elem)
    return elem

def select_all(db_name, table_name):
    try:
        output = execute_sql(db_name, "SELECT * FROM {}".format(table_name))
        logging.getLogger('database').info("select_all: Data selected")
        return output
    except sqlite3.OperationalError as err:
        logging.getLogger('database').error("select_all: {}".format(err))


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


def purge_dbs(ask=True):
    if not ask:
        if os.path.exists('db'):
            shutil.rmtree('db')
            logging.getLogger('database').warning("purge_dbs: All databases were deleted")
        else:
            logging.getLogger('database').info("purge_dbs: No databases to delete")
        return
    in1 = input("Are you sure to delete ALL databases? [y/N]")
    if not in1 == 'y' or not in1 == 'Y':
        if os.path.exists('db'):
            shutil.rmtree('db')
            logging.getLogger('database').warning("purge_dbs: All databases were deleted")
        else:
            logging.getLogger('database').info("purge_dbs: No databases to delete")


def log(message, type='info'):
    if type == 'warning' or type == 'warn':
        logging.getLogger('database').warning(message)
    elif type == 'critical' or type == 'crit':
        logging.getLogger('database').critical(message)
    elif type == 'error' or type == 'err':
        logging.getLogger('database').error(message)
    else:
        logging.getLogger('database').info(message)
