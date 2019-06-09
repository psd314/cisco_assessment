from sqlalchemy import *
import sqlite3
from sqlite3 import Error
 
 
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
#engine = create_engine('sqlite:///dbtool.db')

#metadata = MetaData()
#
#customers = Table('customers', metadata,
#    Column('customer_id', Integer, primary_key=True),
#    Column('first_name', String(50)),
#    Column('last_name', String(50)),
#    Column('zipcode', Integer, nullable=True),
#    Column('country', String(50))
#)
#
#orders = Table('orders', metadata,
#    Column('order_id', Integer, primary_key=True),
#    Column('customer_id', Integer, ForeignKey('customers.customer_id'), nullable=False),
#    Column('ordered_on', Date), 
#)
#
#metadata.create_all(engine)
