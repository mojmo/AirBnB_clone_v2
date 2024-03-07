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

    arch_file = archive_path.split("/")[-1].split(".")[0]
    arch_path_s = f"/data/web_static/releases/{arch_file}/"

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        run("mkdir -p {}".format(arch_path_s))

        # Uncompress the archive to the folder
        # /data/web_static/releases/<archive filename without extension>
        # on the web server
        run("tar -xzf /tmp/{}.tgz -C {}".format(arch_file, arch_path_s))

        # Delete the archive from the web server
        run("rm /tmp/{}.tgz".format(arch_file))

        run("rsync -a {}web_static/* {}".format(arch_path_s, arch_path_s))

        run("rm -rf {}web_static".format(arch_path_s))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create a new the symbolic link /data/web_static/current on the
        # web server, linked to the new version of the code
        # /data/web_static/releases/<archive filename without extension>
        run("ln -s {} /data/web_static/current".format(arch_path_s))
        return True
    except Exception:
        return False
