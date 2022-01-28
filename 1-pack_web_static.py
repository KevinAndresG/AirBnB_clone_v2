#!/usr/bin/python3
"""
    Write a Fabric script that generates a .tgz archive
    from the contents of the web_static folder
    of your AirBnB Clone
"""


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
    except:
        return (None)
