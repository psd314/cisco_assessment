from sqlalchemy import *
import sys
import json
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

def insert(fp):
	engine = create_engine('sqlite:///./data/dbtool.db')
	meta = MetaData()
	
	customers = Table('customers', meta, 
		Column('customer_id', Integer, primary_key=True),
		Column('first_name', String(250)),
		Column('last_name', String(250)),
		Column('zipcode', Integer, nullable=True),
		Column('country', String(250))
	)

	
	orders = Table('orders', meta,
		Column('order_id', Integer, primary_key=True),
		Column('customer_id', Integer, ForeignKey('customers.customer_id')),
		Column('ordered_on', Date) 
	)

	customers.create(engine, checkfirst=True)
	orders.create(engine, checkfirst=True)
	#meta = create_customers_table(engine, meta)
	#create_orders_table(engine, meta)

	with open(fp, 'r') as json_file:
		records = json.load(json_file)
	
	customer_records = records['tables'][0]['records']
	order_records = records['tables'][1]['records']

	insert_customers(customers, engine, customer_records)
	insert_orders(orders, engine, order_records)

	return records['tables'][0]['records']

def insert_customers(customers, engine, records):
	conn = engine.connect()
	for r in records:
		_id = r['customer_id']
		s = select([customers.c.customer_id]).where(customers.c.customer_id == _id) 
		query = conn.execute(s)
		check_id = query.fetchone()
		if not check_id:
			conn.execute(customers.insert(), r)	


def insert_orders(orders, engine, records):
	conn = engine.connect()
	for r in records:
		_id = r['order_id']
		s = select([orders.c.order_id]).where(orders.c.order_id == _id) 
		query = conn.execute(s)
		check_id = query.fetchone()
		if not check_id:
			r['ordered_on'] = datetime.strptime(r['ordered_on'], '%Y-%m-%d')
			conn.execute(orders.insert(), r)	

#def create_customers_table(engine, meta):
#	customers = Table('customers', meta, 
#		Column('customer_id', Integer, primary_key=True),
#		Column('first_name', String(250)),
#		Column('last_name', String(250)),
#		Column('zipcode', Integer, nullable=True),
#		Column('country', String(250))
#	)
#	customers.create(engine, checkfirst=True)
#	return meta
#
#def create_orders_table(engine,  meta):
#	#meta = MetaData()
#
#	orders = Table('orders', meta,
#		Column('order_id', Integer, primary_key=True),
#		Column('customer_id', Integer, ForeignKey('customers.customer_id')),
#		Column('ordered_on', String(20)) 
#	)
#	orders.create(engine, checkfirst=True)
#	return meta
#
#def iiiinsert_customers(engine, records):
#	customers = Table('customers', meta, 
#		Column('customer_id', Integer, primary_key=True),
#		Column('first_name', String(250)),
#		Column('last_name', String(250)),
#		Column('zipcode', Integer, nullable=True),
#		Column('country', String(250))
#	)
#	for r in records:
#		print(r)
#	
	# conn.execute(customers.insert(), r)	
