from importlib import import_module
import pip
import sys
from sys import stdout

#   Checks Python Version
version = sys.version_info;
if version[0] > 2:
    raise 'Python 3 is not backwards compatible with this software.';
elif version[1] > 7:
    print >> stdout, 'WARNING:  This code was written using Python 2.7.x, '+\
                        'you are using a later version.  We recommend '+\
                        'down grading to Python 2.7.x.';

warnings = [];

def gt(a, b):
    if type(a) == unicode:
        a = str(a);
    if type(b) == unicode:
        b = str(b);

    assert(type(a) == str and type(b) == str);
    ainfo = a.split('.');
    binfo = b.split('.');
    length = min(len(ainfo),len(binfo));
    trip = True;
    for i in range(length):
        if int(ainfo[i]) > int(binfo[i]):
            return True;
        elif int(ainfo[i]) < int(binfo[i]):
            trip=False;
    return trip;

def verifyWarning():
    return 'WARNING:  Could not verify the installed version matches the '+\
            'following required versions...';

def wrongVersion(dep, req, cur_vers):
    raise ImportError('Tried to install and update {0} to version {1}, but '.format(dep, req)+\
            'only updated to {0}'.format(cur_vers));

def check(mod, dep, req):
    try:
        vn = mod.__version__;
    except:
        vn = 5;
    if type(vn) == str:
        if not gt(vn, req):
            wrongVersion(dep, req, vn);
    else:
        warnings.append(tuple([dep, req]));

#   Some useful mappings to what packages should be imported as
import_names = {
    'PyYaml':'yaml',
    'PyYAML':'yaml',
    'Jinja2':'jinja2',
    'Django':'django',
    'mod-wsgi':'mod_wsgi',
    'Markdown':'markdown',
    'mkdocs-bootstrap':'mkdocs_bootstrap',
    'mkdocs-bootswatch':'mkdocs_bootswatch',
    'biopython':'Bio',
    'python-dateutil':'dateutil',
    'scikit-learn':'sklearn',
    'backports-abc':'backports_abc',
    'python-markdown-math':'mdx_math',
    'MarkupSafe':'markupsafe',
    'Pygments':'pygments',
    'pymdown-extensions':'pymdownx',
                };

def install_dependencies(dependencies):
    """
    Installs the [dependencies], where each dependency is mapped to the
    requested version number.
    """

    for depend in dependencies.keys():
        print depend;
        call = import_names[depend];
        try:
            mod = import_module(call);
            check(mod, depend, dependencies[depend]);
        except ImportError:
            pip.main(['install', depend, '--upgrade']);
            mod = import_module(call);
            check(mod, depend, dependencies[depend]);

    if len(warnings) > 0:
        print verifyWarning();
        for warning in warnings:
            print 'Package: {0} --- Version: {1}'.format(warning[0], warning[1]);

if __name__ == '__main__':
    filename = sys.argv[1];
    with open(filename, 'r') as f:
        data = f.readlines();

    dependencies = {};

    for line in data:
        package, version = line.split('==');
        dependencies[package] = version;
        if package not in import_names.keys():
            import_names[package] = package;

    install_dependencies(dependencies);
