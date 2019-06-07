from scripts.references import References

class TestReferences:
	def test_constructor(self):
		# Test that constructor properly formats self.url for API call
		ref = References('octocat/Hello-World')
		assert ref.url == 'https://api.github.com/repos/octocat/Hello-World/git/refs'
