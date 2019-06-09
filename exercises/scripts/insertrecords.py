from sqlalchemy import *
import os
import sys
import json
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy import create_engine

class InsertRecords:
	def __init__(self, engine='sqlite:///./data/dbtool.db'):
		self.engine = create_engine('sqlite:///./data/dbtool.db')
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
			Column('ordered_on', String(20)) 
		)
	def insert(self, fp):
		#self.customers.create(self.engine, check_first=True)
		#meta = MetaData()
		#meta = create_customers_table(engine, meta)
		#create_orders_table(engine, meta)

		with open(fp, 'r') as json_file:
			records = json.load(json_file)
		#insert_customers(engine, records, meta)

		return records['tables'][0]['records']



	def create_customers_table(engine, meta):
		customers = Table('customers', meta, 
			Column('customer_id', Integer, primary_key=True),
			Column('first_name', String(250)),
			Column('last_name', String(250)),
			Column('zipcode', Integer, nullable=True),
			Column('country', String(250))
		)
		customers.create(engine, checkfirst=True)
		return meta

	def create_orders_table():
		orders = Table('orders', meta,
			Column('order_id', Integer, primary_key=True),
			Column('customer_id', Integer, ForeignKey('customers.customer_id')),
			Column('ordered_on', String(20)) 
		)
		orders.create(engine, checkfirst=True)
		return meta

	def insert_customers(engine, records, meta):
		customers = Table('customers', meta, 
			Column('customer_id', Integer, primary_key=True),
			Column('first_name', String(250)),
			Column('last_name', String(250)),
			Column('zipcode', Integer, nullable=True),
			Column('country', String(250))
		)
		for r in records:
			s = select
			print(r)
		
		# conn.execute(customers.insert(), r)	
