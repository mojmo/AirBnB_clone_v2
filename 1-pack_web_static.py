#!/usr/bin/python3
"""A Fabric script to create a compressed archive of the web_static folder.

This script defines a Fabric task `do_pack()` that creates a compressed archive
(.tgz) containing the contents of the web_static folder. The archive is stored
in the versions directory and follows the naming convention
`web_static_<year><month><day><hour><minute><second>.tgz`.
"""

from fabric.operations import local
from datetime import datetime
import os


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
