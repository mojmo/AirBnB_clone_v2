#!/usr/bin/python3
"""A Fabric script to create a compressed archive of the web_static folder.

This script defines a Fabric task `do_pack()` that creates a compressed archive
(.tgz) containing the contents of the web_static folder. The archive is stored
in the versions directory and follows the naming convention
`web_static_<year><month><day><hour><minute><second>.tgz`.
"""

import os
from fabric.api import env, put, run


env.hosts = ['3.83.253.65', '3.84.239.237']


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

    if os.path.exists(archive_path) is False:
        return False

    archive_file = archive_path.split("/")[-1].split(".")[0]
    archive_path_server = f"/data/web_static/releases/{archive_file}/"

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        run("mkdir -p {}".format(archive_path_server))

        # Uncompress the archive to the folder
        # /data/web_static/releases/<archive filename without extension>
        # on the web server
        run("tar -xzf /tmp/{}.tgz -C {}".format(archive_file, archive_path_server))

        # Delete the archive from the web server
        run("rm /tmp/{}.tgz".format(archive_file))

        run("rsync -a {}web_static/* {}".format(archive_path_server, archive_path_server))

        run("rm -rf {}web_static".format(archive_path_server))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create a new the symbolic link /data/web_static/current on the
        # web server, linked to the new version of the code
        # /data/web_static/releases/<archive filename without extension>
        run("ln -s {} /data/web_static/current".format(archive_path_server))
        return True
    except:
        return False
