import click
from scripts.references import References
import os
import scripts.insert_copy as ic

@click.group()
def cli1():
	"""Welcome to exercises"""
	pass

@cli1.command()
@click.argument('url')
def listrefs(url):
	"""Queries GitHub's API and returns references for a give user or repo
		\n\n\targs: path - url segment consisting of github name and repo <github_name>/<repo_name>
		\n\n\tex. octocat/Hello-World
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
@click.option('--file', '-f', 'file_', help='absolute path to file to be read in to db')
@click.option('--date', help='Date for query, format: YYYY-MM-DD')
def dbtool(action, file_, date):
	"""Extra help for db"""
	if action=='insert':
		click.echo(file_)
		click.echo(ic.insert(file_))
	elif action=='orders':
		orders = ic.get_orders(date)
		for o in orders['pre_date']:
			click.echo(o)
		click.echo()
		for o in orders['post_date']:
			click.echo(o)
	else:
		click.echo('handle error')
	click.echo('dbtool called')

	
#@cli2.command()
#@click.option('--file', help='absolute path to file to be read in to db')
#def insert(file):
#	"""Insert records into db"""
#	click.echo(ir.insert(file))
#
#@cli2.command()
#def orders():
#	"""Retrieve record based on date"""
#	click.echo('query results')
cli = click.CommandCollection(sources=[cli1, cli2])

