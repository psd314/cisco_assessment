# cisco_assessment
After cloning the repo
### Install
1. $ virtualenv <environment_name> (Optional step but recommended) *
2. $ source <environment_name>/bin/activate (activate virtual environment)
3. $ python setup sdist (from /exercises directory)
4. $ pip install cisco_assessment/exercises/dist/Exercises-0.1.tar.gz
5. $ exercises --help

### About
exercises is a command line tool for interfacing with the GitHub 
API as well as performing a limited set of database operations.

Commands:

listrefs - returns non-pull refs from a GitHub repository
ex. exercises listrefs octocat/Hello-World

dbtool - performs record insert and retrieval.
arguments: action - insert | orders
options: --file - absolute path to json file with appropriate schema, used with 'insert' arg
	 --date - date in YYYY-MM-DD format, used with 'orders' arg

Database Notes:
Database was instantiated by running create_db.py in the /data directory.  Script simply establishes
a connection to a sqlite database in the data folder. Tables are created the first time 'dbtool insert' 
is run after installation per instructions. Data files are not included in tar package.


*$ - prompt symbol
