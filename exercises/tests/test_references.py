from scripts.references import References

class TestReferences:
	def test_constructor(self):
		# Test that constructor properly formats self.url for API call
		ref = References('octocat/Hello-World')
		assert ref.url == 'https://api.github.com/repos/octocat/Hello-World/git/refs'

	def test_get_refs(self):
		# no unit test, functionality is all from third party library,
		# add integration tests or e2e tests
		pass

	def test_filter_refs(self):
		# set up context for test
		ref = References('octocat/Hello-World')
		ref.references = [
			{'ref': 'refs/pull/36/head'},
			{'ref': 'refs/push/36/head'},
		]

		# run function to be tested
		ref.filter_refs()	

		# assert for expected behavior, that objects with 'pull' in the value for the ref
		# key have been removed

		assert len(ref.references) == 1
		assert 'pull' not in ref.references[0]['ref']

	def test_format_refs(self):
		ref = References('octocat/Hello-World')
		ref.references = [
			{
				'ref': 'refs/pull/36/head',
				'node_id': 1234,
				'url': 'www.github.com',
				'object': {
					'url': 'www.hackerrank.com'
				}
			},
			{
				'ref': 'refs/push/36/head',
				'node_id': 1234,
				'url': 'www.github.com',
				'object': {
					'url': 'www.hackerrank.com'
				}
			}
		]

		yaml_string = ref.format_refs()

		assert isinstance(yaml_string, str) == True
