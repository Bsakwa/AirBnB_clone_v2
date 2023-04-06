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
    if os.path.isfile(archive_path) is False:
        return False

    try:
        file_n = archive_path.split("/")[-1]
        no_xt = file_n.split(".")[0]
        s_path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(s_path, no_xt))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, s_path, no_xt))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(s_path, no_xt))
        run('rm -rf {}{}/web_static'.format(s_path, no_xt))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(s_path, no_xt))
        return True
    except Exception as e:
        return False


def deploy():
    """ Find the path and deploy"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
