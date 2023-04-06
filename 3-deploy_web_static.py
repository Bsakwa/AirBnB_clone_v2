#!/usr/bin/python3
"""
Creates and distributes an archive to my web servers
"""

from fabric.api import *
from os.path import exists, isdir
from datetime import datetime
import os.path

env.user = "ubuntu"
env.hosts = ['100.25.222.45', '100.25.197.72']
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """
    Generates .tgz archive and outputs its correct format
    """
    try:
        if isdir("versions") is False:
            local("mkdir versions")

        time_now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        # Defines the format in which the compressed file is saved
        saved_file = "versions/web_static_{}.tgz".format(time_now)
        # Defines the bash command to compress the contents
        comp_file = local("tar -cvzf {} web_static/".format(saved_file))
        print("web_static packed: {}".format(saved_file))
        return (saved_file)
    except Exception as e:
        return None


def do_deploy(archive_path):
    """
    Deploys an archive to the specified remote servers
    through ssh
    Attr:
        archive_path (str): The path of our compressed archive
    """
    try:
        if not (path.exists(archive_path)):
            return False

        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        # Upload the the archive to the /tmp directory of the server
        put(archive_path, '/tmp/')

        # Create the destination folder
        run('mkdir -p /data/web_static/releases/{}/'.format
            (no_ext))

        # Uncompress the archive to the web server
        run("tar -xzf /tmp/{}.tgz -C \
            /data/web_static/releases/{}/".format
            (file_n, no_ext))

        # Delete the archive from the web server
        run('rm /tmp/{}.'.format(file_n))

        # Delete the symbolic link from the web server
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format
            (no_ext, no_ext))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(no_ext))
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s /data/web_static/releases/{}/ \
            /data/web_static/current".format(no_ext))

        print("New Version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """ Find the path and deploy"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
