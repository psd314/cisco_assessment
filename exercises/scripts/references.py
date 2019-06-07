import click
import requests
import yaml

class References():
	def __init__(self, path):
		self.path = path
		self.url = f'https://api.github.com/repos/{self.path}/git/refs'

	def get_refs(self):
		r = requests.get(self.url)
		self.references = r.json()

	def filter_refs(self):
		self.references = [ref for ref in self.references if 'pull' not in ref['ref']]
		return self.references

	def format_refs(self):
		yaml_objs = []
		for ref in self.references:
			del ref['node_id']
			del ref['object']['url']
			del ref['url']
			yaml_objs.append(ref)

		return yaml.dump(yaml_objs, default_flow_style=False)
