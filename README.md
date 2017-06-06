## ELEC 240 Website

The old website for ELEC 240 was a bit out of date, and needed some help.
This repo has an updated website, as well as a script in Python that was used to
convert *most* of the old website to a prettier and more useful version that
[MkDocs](http://www.mkdocs.org/) could work with.

## Building the Site

If you'd like, you can build the site from the (admittedly) mixed Markdown and HTML source files,
which are stored in [./docs](./docs).  The site was built with [MkDocs](http://mkdocs.org), and
is very simple to build.  It's suggested you create a blank python virtual environment, either
with Anaconda or ```virtualenv```.  Assuming you have ```pip``` installed, it's as easy as:

```bash
path/to/repo/dir$ pip install -r requirements.txt
path/to/repo/dir$ mkdocs build
```  

where [requirements.txt](./requirements.txt) is found in the repository, and you're working
from the project directory.

## Deploying the Site

After (optionally) building the site, simply either copy (worse), or symlink (better) the [static
site files](./site) to the root directory you host your site from.

