import click
from scripts.references import References
import os
import scripts.insert_records as ir

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

@click.group(chain=True)
def cli2():
	pass

@cli2.command()
def dbtool():
	"""Extra help for db"""
	
@cli2.command()
@click.option('--file', help='absolute path to file to be read in to db')
def insert(file):
	"""Insert records into db"""
	click.echo(ir.insert(file))

@cli2.command()
def orders():
	"""Retrieve record based on date"""
	click.echo('query results')
cli = click.CommandCollection(sources=[cli1, cli2])
