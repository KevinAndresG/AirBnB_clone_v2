#!/usr/bin/python3
"""
    Write a Fabric script
    that distributes an archive to your web servers,
    using the function do_deploy:
"""
from fabric.api import *
from fabric.operations import run, put
import os
env.user = 'ubuntu'
env.hosts = ['35.243.183.11', '34.201.98.44']


def do_pack():
    """
        make the .tgz file
    """
    from fabric.api import local
    import datetime

    try:
        local("mkdir -p versions")
        timenow = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        local("tar -cvzf versions/web_static_{}.tgz web_static"
              .format(timenow))
        return ("versions/web_static_{}.tgz".format(timenow))
    except Exception as Right:
        return (None)


def do_deploy(archive_path):
    """
        making some modifications
    """
    if not os.path.isfile(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        split1 = archive_path.split('/')
        split2 = split1[1].split('.')
        split3 = split2[0]
        dwr = "/data/web_static/releases/{}/".format(split3)
        run("mkdir -p {}".format(dwr))
        run("tar -xzf /tmp/{} -C {}".format(split1[1], dwr))
        run("rm /tmp/{}".format(split1[1]))
        run("mv {}web_static/* {}".format(dwr, dwr))
        run("rm -rf {}web_static".format(dwr))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(dwr))
        return (True)
    except Exception as Right:
        return (False)


def deploy():
    """
        use all the functions
    """
    path = do_pack()
    if not path:
        return False
    return do_deploy(path)
