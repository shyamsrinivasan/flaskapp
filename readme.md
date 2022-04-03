Notes:
* Raw HTML files for direct running on web server are stored seperately in the *//html* folder
* HTML templates for use with *jinja2* in FLASK are stored in *//app//templates* folder


Steps to run browser-sync on CLI:

* Go to directory in which HTML files (that are to be tested) are present
* Run `browser-sync start --server --directory --files "*"`
* "\*" can be substituted with filenames of only select files that need to be tested


