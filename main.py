import log_helper as log
import database_helper as db

def init_logs():
    log.init_log('main')
    log.init_log('database')
    log.init_log('logging')

if (__name__ == "__main__"):
    init_logs()
    db.create_db('users')

    #test
    '''logging.getLogger('main').info('info')
    logging.getLogger('main').warning("Warning!")
    logging.getLogger('main').error("Whats happening??")
    logging.getLogger('main').critical("I'm dying!")'''