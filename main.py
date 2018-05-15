import log_helper as log
import database_helper as db

def init_logs():
    log.init_log('main')
    log.init_log('database')
    log.init_log('logging')
    log.init_log('sql')

if (__name__ == "__main__"):
    init_logs()
    db.delete_db('login')
    db.create_table('login', 'credentials', 'userid real', 'username text', 'password text')
    db.execute_sql('login', "INSERT INTO test VALUES ('', 'tim', 2)")
    db.execute_sql('login', "SELECT * FROM test")