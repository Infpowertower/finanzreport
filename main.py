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
    init_logs()

    # gui = startGui()
    # gui.setName('GUI')
    # Start running the threads!
    # gui.start()
    # Wait for the threads to finish...
    # gui.join()
    gui = interface.Gui()
    gui.start()
    print('Main Terminating...')
