from sqlalchemy import *
import sqlite3
from sqlite3 import Error
 
#instantiate sqlite3 database when script is run
 
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()
 
if __name__ == '__main__':
    create_connection("dbtool.db") 
