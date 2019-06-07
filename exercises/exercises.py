import click
from scripts.references import References

@click.group()
def cli1():
	"""Welcome to exercises"""
	pass

@cli1.command()
@click.argument('url')
def listrefs(url):
	"""Extra help for listrefs"""
	ref = References(url)
	ref.get_refs()
	ref.filter_refs()
	click.echo(ref.format_refs())

@click.group()
def cli2():
	pass

@cli2.command()
def dbtool():
	"""Extra help for db"""
	pass

@cli2.command()
def insert():
	"""Insert records into db"""
	click.echo('insert into db')

@cli2.command()
def orders():
	"""Retrieve record based on date"""
	click.echo('query results')
cli = click.CommandCollection(sources=[cli1, cli2])
