import click
from scripts.references import References
import os
import scripts.insertreferences as ir

@click.group()
def cli1():
	"""Python Exercises"""
	pass

@cli1.command()
@click.argument('url')
def listrefs(url):
	"""Queries GitHub's API and returns references for a give user or repo
		\n\n\targs: path - url segment consisting of github name and repo <github_name>/<repo_name>
		\n\n\tex. exercises listrefs octocat/Hello-World
	"""
	ref = References(url)
	ref.get_refs()
	ref.filter_refs()
	click.echo(ref.format_refs())

@click.group()
def cli2():
	pass

@cli2.command()
@click.argument('action', required=False, default=True)
@click.option('--file', '-f', 'file_', help='Absolute path to file to be read in to db. Use with \'insert\' argument. ex. /home/Documents/data.json')
@click.option('--date', help='Date for query, format: YYYY-MM-DD. Use with \'order\' argument. ex. 2016-09-18')
def dbtool(action, file_, date):
	# doc string for dbtool --help
	"""Database operations
		\n\n\targs: insert - use --file option with absolute path to load json file into database. ex. exercises dbtools insert --file=/home/Documents/data.json
		\n\n\torders - use --date option with YYYY-MM-DD format to return order information. ex. exercises dbtools orders --date=2016-10-18
	"""
	# handle dbtool arguments 
	if action=='insert':
		click.echo(ir.insert(file_))
	elif action=='orders':
		# loop through query results for a given date and print out
		# lists for on/before and after
		orders = ir.get_orders(date)
		for o in orders['pre_date']:
			click.echo(o)
		click.echo()
		for o in orders['post_date']:
			click.echo(o)
	else:
		click.echo('Invalid or missing argument. Valid arguments: insert | orders. See \'exercises dbtools --help\'\
option for more information on correct usage.')

# combine groups into one cli object
cli = click.CommandCollection(sources=[cli1, cli2])

