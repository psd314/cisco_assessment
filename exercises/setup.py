from setuptools import setup, find_packages

setup(
	name='Exercises',
	version='0.1',
	setup_requires=['pytest-runner'],
	tests_require=['pytest'],
	packages=find_packages(),
	include_package_data=True,	
	install_requires=[
		'certifi==2019.3.9',
		'chardet==3.0.4',
		'Click==7.0',
		'Exercises==0.1',
		'idna==2.8',
		'PyYAML==5.4',
		'requests==2.22.0',
		'SQLAlchemy==1.3.4',
		'urllib3==1.25.3'
	],
	entry_points='''
		[console_scripts]
		exercises=main_script.exercises:cli
	'''
)
