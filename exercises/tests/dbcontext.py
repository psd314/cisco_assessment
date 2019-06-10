from sqlalchemy import *
import json
import sqlite3
from datetime import datetime
import os
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy import create_engine

db_path = 'sqlite:///' + os.path.abspath('dbtool.db')

class DBContext:
	def __init__(self, db_file):
		# instantiate db if it doesn't exist
		sqlite3.connect(db_file)

		self.engine = create_engine(db_path)
		self.meta = MetaData()
		self.customers = Table('customers', self.meta, 
			Column('customer_id', Integer, primary_key=True),
			Column('first_name', String(250)),
			Column('last_name', String(250)),
			Column('zipcode', Integer, nullable=True),
			Column('country', String(250))
		)
		
		self.orders = Table('orders', self.meta,
			Column('order_id', Integer, primary_key=True),
			Column('customer_id', Integer, ForeignKey('customers.customer_id')),
			Column('ordered_on', Date) 
		)
		self.customer_data = [
			{
		          "customer_id": 27,
        		  "first_name": "Bruce",
        		  "last_name": "Wayne",
        		  "zipcode": 25490,
        		  "country": "USA"
        		}
		]
		self.order_data = [
			{
        		  "order_id": 4593,
        		  "customer_id": 27,
        		  "ordered_on": "2016-10-18"
        		}
		]

	def create_customers_table(self):
		conn = self.engine.connect()
		self.customers.create(self.engine, checkfirst=True) 
		
	def create_orders_table(self):
		conn = self.engine.connect()
		self.orders.create(self.engine, checkfirst=True)
