Notes:
* Raw HTML files for direct running on web server are stored seperately in the *//html* folder
* HTML templates for use with *jinja2* in FLASK are stored in *//app//templates* folder


Steps to run browser-sync on CLI:

* Go to directory in which HTML files (that are to be tested) are present
* Run `browser-sync start --server --directory --files "*"`
* "\*" can be substituted with filenames of only select files that need to be tested

Installing Python from Ubuntu PPA for WSL-Ubuntu:
* `sudo add-apt-repository ppa:deadsnakes/ppa`
* `sudo apt update && sudo apt upgrade`

Install Python for local user:
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
* Check if python is nstalled and added to path `which python3` or `python3 --version`


Install Python as super user:
* `sudo apt install python3.10`


Compiling Python from source on local user directory:
* Needs to have all tools needed by compilation installed as super user using: `sudo apt-get install build-essential` to avoid errors like *No acceptable C compiler found in $PATH*
* If *fatal error: ffi.h No such file or directory* is encountered then:`apt install libffi-dev`



