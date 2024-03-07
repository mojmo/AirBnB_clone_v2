#!/usr/bin/python3
"""A Fabric script to create a compressed archive of the web_static folder.

This script defines a Fabric task `do_pack()` that creates a compressed archive
(.tgz) containing the contents of the web_static folder. The archive is stored
in the versions directory and follows the naming convention
`web_static_<year><month><day><hour><minute><second>.tgz`.
"""

import os
from fabric.api import *
from fabric.operations import *
from datetime import datetime


env.hosts = ['3.83.253.65', '3.84.239.237']


def do_pack():
    """Creates a compressed archive of the web_static folder.

    This function creates a compressed archive (.tgz) containing the contents
    of the web_static folder. The archive is stored in the versions directory
    and follows the naming convention
    'web_static_<year><month><day><hour><minute><second>.tgz'.

    Returns:
        str or None: The file path of the generated archive if successful. None
        if the archive creation failed.
    """

    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = f"versions/web_static_{date}.tgz"

    local("mkdir -p versions")
    local(f"tar -cvzf {file_path} web_static")

    if os.path.exists(file_path):
        return file_path
    else:
        return None


def do_deploy(archive_path):
    """Deploys a compressed archive of the web_static
    folder to multiple servers.

    This function uploads the specified compressed archive to multiple servers,
    extracts its contents, and creates a symbolic link to the latest version of
    the web_static folder.

    Args:
        archive_path (str): The path to the compressed archive file to deploy.

    Returns:
        bool: True if all operations are completed successfully,
        False otherwise.
    """

    if not os.path.exists(archive_path):
        return False

    # env.hosts = ['3.83.253.65', '3.84.239.237']
    archive_file = archive_path.split("/")[-1].split(".")[0]
    archive_path_server = f"/data/web_static/releases/{archive_file}/"

    # Upload the archive to the /tmp/ directory of the web server
    if put(archive_path, "/tmp/").failed is True:
        return False

    if run(f"mkdir -p {archive_path_server}").failed is True:
        return False

    # Uncompress the archive to the folder
    # /data/web_static/releases/<archive filename without extension>
    # on the web server
    command = f"tar -xzf /tmp/{archive_file}.tgz -C {archive_path_server}"
    if run(command).failed is True:
        return False

    # Delete the archive from the web server
    if run(f"rm /tmp/{archive_file}.tgz").failed is True:
        return False

    command = f"mv {archive_path_server}web_static/* {archive_path_server}"
    if run(command).failed is True:
        return False

    # Delete the symbolic link /data/web_static/current from the web server
    if run("rm -rf /data/web_static/current").failed is True:
        return False

    # Create a new the symbolic link /data/web_static/current on the
    # web server, linked to the new version of the code
    # /data/web_static/releases/<archive filename without extension>
    command = f"ln -s {archive_path_server} /data/web_static/current"
    if run(command).failed is True:
        False

    return True
