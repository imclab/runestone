import paver
import paver.misctasks
from paver.path import path
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()
import os, sys

from sphinxcontrib import paverutils

sys.path.append(os.getcwd())

# You will want to change these for your own environment in .gitignored paverconfig.py
try:
    from paverconfig import master_url, master_app
except:
    print 'NOTICE:  You are using default values for master_* Make your own paverconfig.py file'
    master_url = 'http://127.0.0.1:8000'
    master_app = 'runestone'



options(
    sphinx = Bunch(
        docroot=".",
        ),

    everyday = Bunch(
        outdir="static/everyday",
        sourcedir="everyday",
        builddir="static/everyday",
        confidir="everyday",
        template_args={'course_id':'everyday',
                       'login_required':'false',
                       'appname':master_app,
                       'loglevel':10,
                       'course_url':master_url }
        ),

    thinkcspy = Bunch(
        builddir="static/thinkcspy",
        sourcedir="source",
        outdir="static/thinkcspy",
        confdir="thinkcspy",
        template_args={'course_id':'thinkcspy',
                       'login_required':'false',
                       'appname':master_app,
                       'loglevel':10,
                       'course_url':master_url }

    ),

    pythonds = Bunch(
        builddir="static/pythonds",
        sourcedir="source",
        outdir="static/pythonds",
        confdir="pythonds",
        template_args={'course_id':'pythonds',
                       'login_required':'false',
                       'appname':master_app,
                       'loglevel':10,
                       'course_url':master_url }

    ),

    overview = Bunch(
        builddir="static/overview",
        sourcedir="overview",
        outdir="static/overview",
        confdir="overview",
        template_args={'course_id':'overview',
                       'login_required':'false',
                       'appname':master_app,
                       'loglevel':10,
                       'course_url':master_url }

    ),

    devcourse = Bunch(
        builddir="static/devcourse",
        sourcedir="source",
        outdir="static/devcourse",
        confdir="devcourse",
        template_args={'course_id':'devcourse',
                       'login_required':'true',
                       'appname':master_app,
                       'loglevel':10,
                       'course_url':master_url }

    )


)

@task
@cmdopts([('all','a','rebuild everything')])
def everyday(options):

    if 'all' in options.everyday:
      options['force_all'] = True
      options['freshenv'] = True

    paverutils.run_sphinx(options,'everyday')

@task
@cmdopts([('all','a','rebuild everything')])
def thinkcspy(options):
    sh('cp %s/index.rst %s' % (options.thinkcspy.confdir,options.thinkcspy.sourcedir))

    if 'all' in options.thinkcspy:
      options['force_all'] = True
      options['freshenv'] = True
    paverutils.run_sphinx(options,'thinkcspy')

@task
@cmdopts([('all','a','rebuild everything')])
def pythonds(options):
    sh('cp %s/index.rst %s' % (options.pythonds.confdir,options.pythonds.sourcedir))

    if 'all' in options.pythonds:
      options['force_all'] = True
      options['freshenv'] = True
    paverutils.run_sphinx(options,'pythonds')

@task
@cmdopts([('all','a','rebuild everything')])
def overview(options):
    if 'all' in options.overview:
      options['force_all'] = True
      options['freshenv'] = True

    paverutils.run_sphinx(options,'overview')

@task
@cmdopts([('all','a','rebuild everything')])
def devcourse(options):
    sh('cp %s/index.rst %s' % (options.devcourse.confdir,options.devcourse.sourcedir))

    if 'all' in options.devcourse:
      options['force_all'] = True
      options['freshenv'] = True

    paverutils.run_sphinx(options,'devcourse')

@task
@cmdopts([('all','a','rebuild everything')])
def allbooks(options):
    if 'all' in options.allbooks:
      options.thinkcspy['all'] = True
      options.pythonds['all'] = True
      options.overview['all'] = True
      options.devcourse['all'] = True
    thinkcspy(options)
    pythonds(options)
    devcourse(options)
    overview(options)
