#!D:\UPB\Matkul\Senin\Bahasa Pemrograman\UAS\program1\venv\Scripts\python.exe
# ********************************
# * author: Ilya Shalyapin       *
# * website: ishalyapin.ru       *
# * email: ishalyapin@gmail.com  *
# ********************************

import getopt
import os
import re
import subprocess
import sys
import tempfile



def run(cmd):
    return subprocess.call(cmd, shell=True)

def out(cmd):
    return subprocess.check_output(cmd, shell=True)

def github_download(url, dirname):
    user, repo = re.search("github.com/(?P<user>[\w\-]+)/(?P<repo>[\w\-]+)/", url).groups()
    if not os.path.exists(dirname):
        error("Destination folder ('%s') does not exist." % dirname)
        sys.exit(1)
    tmpdir = tempfile.mkdtemp()

    run("wget %s -O %s/master.tar.gz" % (url, tmpdir))
    run("(cd %s; tar -xzf master.tar.gz)" % tmpdir)
    run("cp -R %(tmpdir)s/`ls %(tmpdir)s|grep %(repo)s`/* %(dirname)s" % dict(tmpdir=tmpdir, repo=repo, dirname=dirname))
    run("rm -rf %s" % tmpdir)

def help():
    tasks = load_tasks()

    print """
Usage: da [command] [options] [args]

Options:
  -h, --help            show this help message and exit

Available commands:"""

    maxlen = 0
    for name in tasks.keys():
        maxlen = max(len(name), maxlen)

    for name, obj in tasks.items():
        if callable(obj):
            doc =(obj.__doc__ or '').strip()
            spaces = (maxlen + 15 - len(name))
            print u"%s%s%s" % (name, ' '*spaces, doc)

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.GetoptError as err:
        # print help information and exit:
        error(str(err)) # will print something like "option -a not recognized"
        help()
        sys.exit(2)

    for o, a in opts:
        if o in ("-h", "--help"):
            help()
            sys.exit()
        else:
            assert False, "unhandled option"

    if len(sys.argv) < 2:
        help()
        sys.exit()
    task_name = sys.argv[1]
    tasks = load_tasks()
    if not task_name in tasks:
        error("Task '%s' not found." % task_name)
        sys.exit(1)
    tasks[task_name]()

def load_tasks():
    path = os.path.join(os.getcwd(), 'da.tasks.py')
    if not os.path.exists(path):
        error(u"da.tasks.py not found in current directory")
        sys.exit(1)

    locals = {}
    execfile(path, globals(), locals)
    return locals

def error(text):
    print >> sys.stderr, u'Error: ' + text

if __name__ == '__main__':
    main()
