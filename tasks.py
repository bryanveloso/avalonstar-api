 # -*- coding: utf-8 -*-
import time
import functools
import os
import requests

from invoke import task, run


def _out(name, message):
    print('[\033[1;37m{}\033[0m] {}'.format(name, message))


@task
def dbsync(verbose=False, database='avalonstar-tv', **kwargs):
    out = functools.partial(_out, 'heroku.pull')
    hide = 'out' if not verbose else None

    # Take a snapshot.
    out('Snapshotting the production database.')
    run('heroku pg:backups capture DATABASE', hide=hide)

    # Fetch the latest database dump.
    run('curl -o latest.dump `heroku pg:backups public-url -q`', hide=hide)
    out('Latest database dump (latest.dump) grabbed via curl.')

    # Restore it.
    run('pg_restore --verbose --clean --no-acl --no-owner -h localhost -d %s latest.dump' % database, hide=True)
    run('rm latest.dump', hide=hide)
    out('Restored latest production dump to local database.')


@task
def deploy(verbose=False, migrate=False, **kwargs):
    out = functools.partial(_out, 'project.deploy')
    hide = 'out' if not verbose else None

    # Ready? Let's go.
    out('Pushing project to GitHub.')
    run('git push origin', hide=hide)
    out('Deploying to Heroku.')
    run('git push heroku')

    # Done!
    out('All done~!')


@task
def server(**kwargs):
    # Use `python manage.py runserver` wrapped around Grunt to start all
    # the development processes.
    run('python manage.py gruntserver', pty=True)


@task
def migrate(verbose=False, app='', **kwargs):
    out = functools.partial(_out, 'project.deploy')
    hide = 'out' if not verbose else None

    run('heroku run python manage.py migrate %s' % app, hide=hide)


@task
def resetmessages(verbose=False, **kwargs):
    out = functools.partial(_out, 'project.deploy')
    hide = 'out' if not verbose else None

    # Use requests to save out, then clear out Firebase chat.
    timestamp = time.strftime('%Y%m%d')
    url = 'https://avalonstar.firebaseio.com/messages/.json?print=pretty'
    out('Saving snapshot of Firebase `messages` endpoint to "messages-%s.json."' % timestamp)
    run('curl -o ./backups/messages-%s.json %s' % (timestamp, url), hide=hide)

    out('Clearing Firebase `messages` endpoint.')
    requests.delete('https://avalonstar.firebaseio.com/messages.json')
