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
yourapp/
    __init__.py
    admin/
        __init__.py
        views.py
        static/
        templates/
    home/
        __init__.py
        views.py
        static/
        templates/
    control_panel/
        __init__.py
        views.py
        static/
        templates/
    models.py


