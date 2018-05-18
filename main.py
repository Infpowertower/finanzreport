import log_helper as log
import database_helper as db
from threading import Thread
import time
import interface
from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class webserver(BaseHTTPRequestHandler):
    def do_GET(self):
        rootdir = '/var/www/html/'
        try:
            if self.path.endswith('.html'):
                f = open(rootdir + self.path)  # open requested file

                # send code 200 response
                self.send_response(200)

                # send header first
                self.send_header('Content-type', 'text-html')
                self.end_headers()

                # send file content to client
                self.wfile.write(f.read())
                f.close()
                return

        except IOError:
            self.send_error(404, 'file not found')


def run_web():
  print('http server is starting...')

  #ip and port of server
  #by default http server port is 80
  server_address = ('127.0.0.1', 8080)
  httpd = HTTPServer(server_address, webserver)
  print('http server is running...')
  httpd.serve_forever()


def init_logs():
    log.init_log('main')
    log.init_log('database')
    log.init_log('logging')
    log.init_log('sql')


if __name__ == "__main__":
    log.purge_logs(False)
    init_logs()
    #db.delete_table('db_test', 'table_test')
    #db.create_table('db_test', 'table_test', 'transid integer', 'value real', 'note text')
    #db.insert_data('db_test', 'table_test', 1, 9384.38, 'initial commit')
    print(db.select_all('db_test', 'table_test')[1])

    run_web()
    # gui = interface.Gui()
    # gui.start()
    print('Main Terminating...')
