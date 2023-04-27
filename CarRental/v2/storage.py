import configparser
import MySQLdb.cursors

def connect():

    config = configparser.ConfigParser()
    config.read('config.ini')

    db_variable = 'mysqlDB'

    return MySQLdb.connect(host = config[db_variable]['host'],
                           user = config[db_variable]['user'],
                           passwd = config[db_variable]['pass'],
                           db = config[db_variable]['db'])