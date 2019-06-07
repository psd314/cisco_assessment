from setuptools import setup, find_packages

setup(
	name='Exercises',
	version='0.1',
	setup_requires=['pytest-runner'],
	tests_require=['pytest'],
	packages=find_packages(),
	include_package_data=True,	
	install_requires=[
		'Click',
	],
	entry_points='''
		[console_scripts]
		exercises=exercises:cli
	'''
)