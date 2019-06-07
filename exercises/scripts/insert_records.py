from sqlalchemy import *
import os
import sys
import json
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

def insert(fp):
	with open(fp, 'r') as json_file:
		return json.dumps(json_file)
	
def create_customers_table():
	engine = create_engine('sqlite:///../data/customer.db')
	meta = MetaData()

	customers = Table('customers', meta, 
		Column('customer_id', Integer, primary_key=True),
		Column('first_name', String(250)),
		Column('last_name', String(250)),
		Column('zipcode', Integer, nullable=True),
		Column('country', String(250))
	)
	customers.create(engine, checkfirst=True)

def create_orders_table():
	engine = create_engine('sqlite:///../data/customer.db')
	meta = MetaData()

	orders = Table('orders', meta,
		Column('order_id', Integer, primary_key=True),
		Column('customer_id', Integer, ForeignKey('customers.customer_id'), 
		Column('ordered_on', Date)) 
	)
	orders.create(engine, checkfirst=True)


