"""
Main hub of the application and playground for new features
currently used database: db_test
"""
import log_helper as log
import logging
import gui
import os
import database_helper as db


def init_logs():
    log.init_log('main')
    log.init_log('database')
    log.init_log('logging')
    log.init_log('sql')
    log.init_log('gui')


if __name__ == "__main__":
    # Initiate logs. Old logs are purged to avoid confusion.
    log.purge_logs(False)
    init_logs()
    logging.getLogger('main').info("Application started")

    # db-Tests
    # db.delete_table('db_test', 'user')
    # db.create_table('db_test', 'user', 'id INTEGER PRIMARY KEY AUTOINCREMENT', 'username TEXT', 'name TEXT', 'surname TEXT')
    # db.insert_data('db_test', 'user', 1, 'infpowertower', 'Robert', 'Richter')
    print(db.show_tables('db_test'))
    print(db.select_all('db_test', 'user'))
    print(db.select_all('db_test', 'account'))
    print(db.select_all('db_test', 'transfer'))

    # Start the GUI
    gui.start()
    logging.getLogger('main').info('Application terminated')
