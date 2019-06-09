from scripts.insertreferences import *
from tests.dbcontext import DBContext

def test_insert_customers():
	# set up temp db for testing
	db = DBContext('./test_db.db')

	engine = db.engine
	db.create_customers_table()
	
	# run function
	insert_customers(db.customers, engine, db.customer_data)

	# check that record is successfully entered in database
	conn = engine.connect()
	res = conn.execute('SELECT * FROM customers')
	assert res.fetchone().first_name == 'Bruce'


def test_insert_orders():
	# set up temp db for testing
	db = DBContext('./test_db.db')
	engine = db.engine
	db.create_orders_table()
	
	# run function
	insert_orders(db.orders, engine, db.order_data)

	# check that record is successfully entered in database
	conn = engine.connect()
	res = conn.execute('SELECT * FROM orders')
	assert res.fetchone().ordered_on == '2016-10-18'

def test_get_orders():
	# set up temp db for testing
	db = DBContext('./test_db.db')
	engine = db.engine
	db.create_customers_table()
	db.create_orders_table()

	# run function
	tables = get_orders('2016-10-18', engine)	

	# check that get_orders returns to arrays of results
	assert len(tables['pre_date']) == 1
	assert len(tables['post_date']) ==1
