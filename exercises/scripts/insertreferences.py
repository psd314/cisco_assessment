from sqlalchemy import *
import json
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy import create_engine

# create objects for db manipulation
engine = create_engine('sqlite:///./data/dbtool.db')
meta = MetaData()

# table schemas
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
def insert(fp):
	conn = engine.connect()

	# create tables from json file if they don't already exist
	customers.create(engine, checkfirst=True)
	orders.create(engine, checkfirst=True)
	
	# parse json from files
	with open(fp, 'r') as json_file:
		records = json.load(json_file)

	# separate records per table	
	customer_records = records['tables'][0]['records']
	order_records = records['tables'][1]['records']

	# insert records
	insert_customers(customers, engine, customer_records)
	insert_orders(orders, engine, order_records)

	conn.close()

def insert_customers(customers, engine, records):
	conn = engine.connect()

	# loop through records and insert into table
	for r in records:
		# verify primary key doesn't already exist in table
		_id = r['customer_id']
		s = select([customers.c.customer_id]).where(customers.c.customer_id == _id) 
		query = conn.execute(s)
		check_id = query.fetchone()

		if not check_id:
			# insert record if primary key is unique
			conn.execute(customers.insert(), r)	
	conn.close()

def insert_orders(orders, engine, records):
	conn = engine.connect()

	# loop through records and insert into table
	for r in records:
		# verify primary key doesn't already exist in table
		_id = r['order_id']
		s = select([orders.c.order_id]).where(orders.c.order_id == _id) 
		query = conn.execute(s)
		check_id = query.fetchone()

		if not check_id:
			# insert record if primary key is unique
			r['ordered_on'] = datetime.strptime(r['ordered_on'], '%Y-%m-%d')
			conn.execute(orders.insert(), r)	
	conn.close()

def get_orders(date):
	conn = engine.connect()
	# query and aggregate results on/before date
	query_pre = f'SELECT * FROM customers LEFT JOIN (SELECT ordered_on, customer_id, \
		 COUNT(*) as item_counts FROM orders WHERE ordered_on<="{date}" GROUP BY \
		 customer_id) b ON customers.customer_id=b.customer_id ORDER BY b.item_counts DESC'
	pre_results = conn.execute(query_pre)

	tables = {
		'pre_date':[],
		'post_date':[]
	}
	for p in pre_results:
		string = f'{p.first_name} {p.last_name} ordered {p.item_counts} on/before {date}'
		if p.item_counts == None:
			# replace None item_counts with 0 in output string
			string = f'{p.first_name} {p.last_name} ordered {0} on/before {date}'
		tables['pre_date'].append(string)
		
	# query and aggregate results after date
	query_post = f'SELECT * FROM customers LEFT JOIN (SELECT ordered_on, customer_id, \
		 COUNT(*) as item_counts FROM orders WHERE ordered_on>"{date}" GROUP BY \
		 customer_id) b ON customers.customer_id=b.customer_id ORDER BY b.item_counts DESC'
	post_results = conn.execute(query_post)

	for p in post_results:
		string = f'{p.first_name} {p.last_name} ordered {p.item_counts} after {date}'
		if p.item_counts == None:
			# replace None item_counts with 0
			string = f'{p.first_name} {p.last_name} ordered {0} after {date}'
		tables['post_date'].append(string)
	conn.close()
	return tables

