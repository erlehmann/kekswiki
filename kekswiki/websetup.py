"""Setup the kekswiki application"""
import logging

import pylons.test

from os import mkdir
from time import time

from dulwich.repo import Repo
from dulwich.objects import Blob, Tree, Commit, parse_timezone

from kekswiki.config.environment import load_environment

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup kekswiki here"""
    # Don't reload the app if it was loaded under the testing environment
    if not pylons.test.pylonsapp:
        load_environment(conf.global_conf, conf.local_conf)

    # create repository directory
    try:
        mkdir("wiki")
    except OSError:
        pass

    # create repository
    try:
        repo = Repo.init("wiki")
    except OSError:
        repo = Repo("wiki")

    # create blob
    blob = Blob.from_string("Kekswiki is a collaborative hypertext editing system.\n")

    # add blob to tree
    tree = Tree()
    tree.add(0100644, "Kekswiki", blob.id)

    # commit
    commit = Commit()
    commit.tree = tree.id
    author = "Anonymous <anonymous@example.invalid>"
    commit.author = commit.committer = author
    commit.commit_time = commit.author_time = int(time())
    tz = parse_timezone('+0100')[0]  # FIXME: get proper timezone
    commit.commit_timezone = commit.author_timezone = tz
    commit.encoding = "UTF-8"
    commit.message = "Initial commit"

    # save everything
    object_store = repo.object_store
    object_store.add_object(blob)
    object_store.add_object(tree)
    object_store.add_object(commit)

    # create master branch, set it as current
    repo.refs.add_if_new('refs/heads/master', commit.id)
    repo.refs.set_symbolic_ref('HEAD', 'refs/heads/master')
