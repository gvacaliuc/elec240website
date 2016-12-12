import os
import glob
import yaml
import shutil

def stripheader(filename, outputfilename):
    """
    Strips header off html file, and saves as markdown file.
    """

    with open(filename, 'r') as f:
        data = f.readlines();
    line_num = 0;
    for line in data:
        if '<body' in line:
            line_num = max( line_num, data.index(line) + 1 );
        if '</script>' in line:
            line_num = max( line_num, data.index(line) + 1 );
        if '<button' in line:
            line_num = max( line_num, data.index(line) + 1 );

    try:
        newdata = map(unicode, data[line_num:]);
    except:
        safe_unicode = lambda line: unicode(''.join([i if ord(i) < 128 else 'MISSINGDATA' for i in line]));
        newdata = map(safe_unicode, data[line_num:]);

    with open(outputfilename, 'w+') as f:
        f.writelines(newdata);

def createlabyaml(filename, labnum):
    """
    Gets lab title data and lab page links and returns a dictionary to be
    printed as YAML
    """

    with open(filename, 'r') as f:
        data = f.readlines();

    #   Get line numbers of each element of a list
    line_nums = [];
    for i in range(len(data)):
        if '<a ' in data[i]:
            line_nums.append(i);

    #   Get titles and page links
    gettitles = lambda x: x[x.index('name=')+5:x.index('href=')].strip();
    getlinks = lambda x: x[x.index('href=')+5:x.index('>')];

    lines = map(lambda x: data[x], line_nums);
    titles =map(gettitles, lines)
    links = map(getlinks, lines);

    titles.insert(0, 'Home');
    links.insert(0, 'index.html');

    #   Only make links to html files and change path name to markdown
    entrytuples = filter(lambda x: '.html' in x[1], zip(titles, links));
    entrytuples = map(lambda x: (x[0],os.path.join('lab{}'.format(labnum),x[1].rstrip('.html')+'.md')), entrytuples);

    yamldict = {'Lab {}'.format(labnum): [ {title:link} for (title,link) in entrytuples ]};
    
    return yamldict;

def fix_links( filepath, imagefolder, mdfolder, outputpath ):
    """
    Fixes images in the specified file, as well as hyperlinks.  Actual images
    should be stored in the [imagefolder] and any .html files should be stored
    in the [mdfolder] with their extensions changed to .md.  Outputpath is where
    this will save data.
    """

    if not os.path.isdir(os.path.join(outputpath,'figs')):
        os.makedirs(os.path.join(outputpath,'figs'));

    imgsrc_lines = [];
    link_lines = [];

    try:
        with open(filepath, 'r') as f:
            data = f.readlines();
    except IOError:
        print 'Could not locate: {}'.format(filepath);
        print 'Are you sure you have the file right?';
        return;

    for i in range(len(data)):
        if 'src=' in data[i] or 'SRC=' in data[i]:
            imgsrc_lines.append(i);
        if 'href=' in data[i]:
            link_lines.append(i);

    #   Get lines with img src in them
    imgsrc = map(lambda x: data[x], imgsrc_lines);

    #   Redo the image names to follow ../figs/[filename]
    imgsrc_names = map(lambda x: x[x.lower().index('src=')+4:].split(' ')[0].strip('\r\n>/"'), imgsrc);
    imgsrc = map(lambda line, split: line.split(split), imgsrc, imgsrc_names);
    imgsrc_names = map(lambda x: os.path.join('../figs', x.replace('\\','/').split('/')[-1]), imgsrc_names);
    newimgsrc = map(lambda lst, middle: ''.join([lst[0], middle, lst[1]]), imgsrc, imgsrc_names);

    #   Copy image files to [outputpath]/figs
    srcpaths = map(lambda x: os.path.join(imagefolder, x.split('/')[-1]), imgsrc_names);
    dstpaths = map(lambda x: os.path.join(outputpath, 'figs', x.split('/')[-1]), imgsrc_names);
    map(shutil.copy, srcpaths, dstpaths);
    
    #   Write new names to data array
    for linenum, line in zip(imgsrc_lines, newimgsrc):
        data[linenum] = line;


    actual_linklines = filter(lambda x: 'html' in data[x], link_lines);
    bad_linklines = filter(lambda x: x not in actual_linklines, link_lines);
    
    #   These will be links to images or similar...
    if len(bad_linklines):
        print 'Please pay special attention to:\n\tLines: {}\n\tin: {}'.format(bad_linklines, filepath);

    #   Get lines with links in them
    linktext = map(lambda x: data[x], actual_linklines);

    #   Redo links
    links = map(lambda x: x[x.index('href=')+5:], linktext);
    links = map(lambda x: x[:x.index('>')], links);
    splitlink = map(lambda line, split: line.split(split), linktext, links);
    linkedfiles = map(lambda x: x.split('/')[-1].split('#')[0].rstrip('.html"'), links);
    newlinktext = map(lambda lst, middle: ''.join([lst[0], middle, lst[1]]), splitlink, linkedfiles);

    #   Copy linked files to [outputpath]
    srcpaths = map(lambda x: os.path.join(mdfolder, x + '.md'), linkedfiles);
    dstpaths = map(lambda x: os.path.join(outputpath, x + '.md'), linkedfiles);
    validsrc = filter(lambda x: os.path.isfile(x[0]), zip(srcpaths, dstpaths));
    if len(validsrc):
        valid_srcpaths, valid_dstpaths = zip(*validsrc);
    else:
        valid_srcpaths = [];
        valid_dstpaths = [];

    if len(validsrc) != len(srcpaths):
        for tup in zip(srcpaths, dstpaths):
            if tup not in validsrc:
                print 'Could not locate: {}'.format(tup[0]);

    map(shutil.copy, valid_srcpaths, valid_dstpaths);
    
    #   Write new lines to data array
    for linenum, line in zip(actual_linklines, newlinktext):
        data[linenum] = line;

    outputfile = os.path.join(outputpath, filepath.split('/')[-1]);
    with open(outputfile, 'w+') as f:
        f.write(''.join(data));

def main(filedirectory, imagedirectory, outputpath):
    """
    Main program body
    """
#   Removing Headers and changing file extension -------------------------------

    #   Get relative pathnames of htmlfiles
    htmlfiles = glob.glob(os.path.join(filedirectory,'*.html'));

    #   Makes new markdown pathnames
    html2md = lambda x: os.path.join(outputpath, x.split('/')[-1].rstrip('.html')+'.md')
    
    #   Strip headers and save to directory of markdown files
    map(stripheader, htmlfiles, map(html2md, htmlfiles));
    

#   Creating Yaml file for all labs -------------------------------------------- 

    #   Get labfile names
    labfiles = glob.glob(os.path.join(filedirectory,'lab*.html'));
    labnames = map(lambda x: x.split('/')[-1], labfiles);
    labnums = map(lambda x: int(x[x.index('lab')+3:x.index('lab')+3+1]), labnames);
    
    #   Make and write Yaml
    labyamls = map(createlabyaml, labfiles, labnums);
    labyamls = sorted( labyamls, cmp = lambda x,y: cmp(x.keys()[0],y.keys()[0]) );
    yamloutput = {'pages':labyamls};
    with open(os.path.join(outputpath,'output.yml'), 'w+') as f:
        f.write(yaml.dump(yamloutput));

#   Using Yaml file to create file hierarchy and fix links in files ------------

    #   Recover file names in Yaml
    files = [];
    for dct in labyamls:
        mappings = dct.values()[0];
        files.extend( map(lambda x: x.values()[0], mappings) );

    #   Make filenames and existing filepaths
    filenames = map(lambda x: x.split('/')[0]+'.md' if 'index' in x else x.split('/')[-1], files);
    filepaths = map(lambda x: os.path.join(outputpath, x), filenames);

#    print filenames;
#    print filepaths;
    
    #   Either fix links or make a new directory
    mdfolder = outputpath;
    for (fil, filepath) in zip(files, filepaths):
        labfolder = os.path.join(outputpath, fil.split('/')[0]);
    
        #   Fix if not a lab file
        if 'index' not in fil:
            print 'Fixing: {}'.format(filepath);
            fix_links( filepath, imagedirectory, mdfolder, labfolder );

        #   Otherwise try to make the directory
        else:
            if not os.path.isdir(labfolder):
                os.makedirs(labfolder);

            index_filepath = os.path.join(labfolder, fil.split('/')[-1]);
            shutil.copy( filepath, index_filepath );
            fix_links( index_filepath, imagedirectory, mdfolder, labfolder );

if __name__ == '__main__':
    filedirectory = 'elec240_website/html';
    outputpath = 'tmp_md';
    imagedirectory = 'elec240_website/figs';

    if not os.path.isdir(outputpath):
        os.makedirs(outputpath);

    main(filedirectory, imagedirectory, outputpath);
    
    

