import log_helper as log
import database_helper as db
from threading import Thread
import time
import interface
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

import sys
import manage


def init_logs():
    log.init_log('main')
    log.init_log('database')
    log.init_log('logging')
    log.init_log('sql')


if __name__ == "__main__":
    log.purge_logs(False)
    init_logs()


    # gui.start()
    print('Main Terminating...')
