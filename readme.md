## Python version and virtual environment setup:
* Uses [Python 3.9](https://www.python.org/downloads/release/python-3913/)
* Use virtual environment installed with pip `py -m venv env` in application directory to create virtual environment named `env`
* Install project requirements by running `py -m pip install -r requirements.txt` in application directory after activating virtual environment by running `.\env\Scripts\activate` from application directory
### Run Flask application server from CLI inside virtual environment:
* Move to project folder: `cd /project_folder`
* Activate environment venv on Unix(assuming venv is in project_folder): `source venv/bin/activate` or Windows: `"venv/Scripts/activate"`
#### For Flask < 2.2.x:
* Set environment variables FLASK_APP and FLASK_ENV: `set FLASK_APP=application_name` and `set FLASK_ENV=development` for flask development server
* Set DATABASE_URL for using Flask-SQLAlchemy with `set DATABASE_URL="mysql+mysqldb://root:root@localhost/sqlalchemy"`
* Note: `DATABASE_URL` follows the same syntax as engine call syntax in native SQLAlchemy 
* Run command: `flask run`
#### For Flask >= 2.2.x:
* `flask --app app_name --debug run` can be used to indirectly set `FLASK_APP`, turn on debug mode and run the flask application server
### Run Flask application from PyCharm IDE (for debugging only):
* set environment variables `FLASK_APP`, `FLASK_DEBUG` (for Flask >= 2.2.x only) and `DATABASE_URL` in PyCharm run configuration dialog box
* run script for Flask application

## Database migration instructions:
1. If project folder does not have a migrations folder, then initiate use of Flask-Migrate using `flask db init` in the CLI (*Flask-Migrate needs to installed with pip*)
2. Initiate migration with `flask db migrate -m "migration message"`
3. Finalize changes to auto-generated migration script and update database to conform to new application model by running `flask db upgrade`
4. Commit all new and modified files to version control
5. Repeat steps 2 through 4 every time there are changes in database model files
6. To use and synchronize database in another system, pull migrations folder from version control and run `flask db upgrade`

## Notes:
* Raw HTML files for direct running on web server are stored seperately in the *//html* folder
* HTML templates for use with *jinja2* in FLASK are stored in *//app//templates* folder

## Syntax for using *mysqlclient* driver in SQLAlchemy 1.4:
`mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>`

## Steps to run [browser-sync](https://browsersync.io/) on CLI:

* Go to directory in which HTML files (that are to be tested) are present
* Run `browser-sync start --server --directory --files "*"`
* "\*" can be substituted with filenames of only select files that need to be tested

## Installing Python from Ubuntu PPA for WSL-Ubuntu as super user:
* Add Python package ([packaged for Ubuntu](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa)) repository `sudo add-apt-repository ppa:deadsnakes/ppa`
* `sudo apt update && sudo apt upgrade`
* `sudo apt install python3.10`

## Install Python for local user (compile from source):
* `mkdir temp`
* `cd tmp`
* `wget https://www.python.org/ftp/python/3-10.4/Python-3.10.4.tgz`
* `tar zxvf Python-3.10.4.tgz`
* `cd Python-3.10.4`
* `./configure --prefix=$HOME/<python-install-directory>`
* `make`
* `make install`
* add `<python-install-directory>` to `$PATH` by adding following line to .bash_profile file in ~ 
	`export PATH=$HOME/<python-install-directory>/bin:$PATH`
* run `. ~/.bash_profile`
* Check if python is installed and added to path `which python3` or `python3 --version`

## Requisites for compiling [Python](https://www.python.org/downloads/) from source on local user directory:
* Needs to have all tools needed by compilation installed as super user using: `sudo apt-get install build-essential` to avoid error: *No acceptable C compiler found in $PATH*
* Also install other pre-requisites using `libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev` for SSL, SQLite3 and other modules in Python 3
* If *fatal error: ffi.h No such file or directory* is encountered then:`apt install libffi-dev`

## Using [SQLAlchemy](https://www.sqlalchemy.org/) with MySQL using [mysqlclient](https://pypi.org/project/mysqlclient/) package as connector (build from source):
* Download and install [MariaDB C Connector](https://mariadb.com/downloads/connectors/) at the default location (C:\Program Files\MariaDB\MariaDB Connector for C)
* Install MySQL (if not available with distribution) in the WSL Ubuntu distribution using `sudo apt-get install mysql-server`
* Install mysql-config using `sudo apt-get install libmysqlclient-dev`
* `pip install mysqlclient`

## Directory (divisional) structure for using Flask Blueprints with App Factory functions:
flaskapp/
|
---`config.py`
---`app`
|
------`__init__.py`

&nbsp;`config.py`


&nbsp;`app/`


&nbsp;&nbsp;`__init__.py`


&nbsp;&nbsp;`admin/`


&nbsp;&nbsp;&nbsp;`__init__.py`


&nbsp;&nbsp;&nbsp;`views.py`


&nbsp;&nbsp;&nbsp;`static/`


&nbsp;&nbsp;&nbsp;`templates/`


&nbsp;&nbsp;`home/`


&nbsp;&nbsp;&nbsp;`__init__.py`


&nbsp;&nbsp;&nbsp;`views.py`


&nbsp;&nbsp;&nbsp;`static/`


&nbsp;&nbsp;&nbsp;`templates/`
	    

&nbsp;&nbsp;`control_panel/`


&nbsp;&nbsp;&nbsp;`__init__.py`


&nbsp;&nbsp;&nbsp;`views.py`


&nbsp;&nbsp;&nbsp;`static/`


&nbsp;&nbsp;&nbsp;`templates/`


&nbsp;&nbsp;`models.py`


&nbsp;&nbsp;`forms.py`
