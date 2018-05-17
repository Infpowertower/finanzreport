import log_helper as log
import database_helper as db
from threading import Thread
import time
import interface


def init_logs():
    log.init_log('main')
    log.init_log('database')
    log.init_log('logging')
    log.init_log('sql')


if __name__ == "__main__":
    log.purge_logs(False)
    init_logs()
    db.create_table('db_test', 'table_test', 'transid integer', 'value real', 'note text')
    db.insert_data('db_test', 'table_test', 1, 9384.38, 'initial commit')
    print(db.select_all('db_test', 'table_test')[1])
    gui = interface.Gui()
    # gui.start()
    print('Main Terminating...')
