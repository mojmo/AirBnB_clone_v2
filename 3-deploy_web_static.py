#!/usr/bin/python3
"""
Creates a compressed archive of the web_static folder and deploys
it to multiple servers.
"""

import os
from fabric.api import env, put, run, local
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


def deploy():
    """Creates a compressed archive of the web_static folder and
    deploys it to multiple servers.

    This function creates a compressed archive of the web_static folder
    using the do_pack() function and then deploys it to multiple servers
    using the do_deploy() function. If the archive creation or deployment
    fails, it returns False.

    Returns:
        bool: True if the deployment is successful, False otherwise.
    """

    file_path = do_pack()
    if file_path is None:
        return False

    return do_deploy(file_path)
