## ELEC 240 Website

The old website for ELEC 240 was very out of date, and not very functional.  This repo has a the new website, as well as a script in Python that was used to convert *most* of the old website to a prettier and more useful version that [MkDocs](http://www.mkdocs.org/) could work with.

## Python Dependencies

Since the website needs to be built with mkdocs, I included a virtualenv that can be copied to your virtualenv folder if you'd like, in order to hold the Python Dependencies for building.  Otherwise, this is the output of ```pip freeze``` for me:  
```bash
backports-abc==0.5
certifi==2016.9.26
click==6.6
Jinja2==2.8
livereload==2.5.0
Markdown==2.6.7
MarkupSafe==0.23
mkdocs==0.16.0
Pygments==2.1.3
pymdown-extensions==1.2
python-markdown-math==0.2
PyYAML==3.12
singledispatch==3.4.0.3
six==1.10.0
tornado==4.4.2
```

## On Rice Network

The site isn't currently live publically on the Rice ECE pages, however if you are inside the Rice Network, you should be able to access it [here](http://10.100.26.7:8000).
