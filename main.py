import log_helper as log
import database_helper as db


def init_logs():
    log.init_log('main')
    log.init_log('database')
    log.init_log('logging')
    log.init_log('sql')


if __name__ == "__main__":
    log.purge_logs(False)
    init_logs()
    db.purge_dbs(False)
    db.create_db('data')
    db.create_table('data', 'giro', 'entryid integer', 'day integer', 'month integer', 'year integer', 'value real', 'note text', 'Primary Key(entryid)')
    db.delete_table('data', 'giro')
    db.delete_table('data', 'giro')