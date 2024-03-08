#!/usr/bin/python3
"""Cleans up old archives and releases from the server."""

import os
from fabric.api import env, run, cd, lcd, local

env.hosts = ['3.83.253.65', '3.84.239.237']


def do_clean(number=0):
    """Cleans up old archives and releases from the server."""

    # Convert number to an integer, default to 1 if 0 or invalid
    if int(number) == 0:
        number = 1
    else:
        number = int(number)

    # Remove old archives
    archives_path = "versions"
    archives = sorted(os.listdir(archives_path))
    [archives.pop() for i in range(number)]
    with lcd(archives_path):
        for archive in archives:
            local("rm {}".format(archive))

    # Remove old releases
    releases_path = "/data/web_static/releases"
    with cd(releases_path):
        releases = run("ls -tr").split()
        releases = [r for r in releases if "web_static_" in r]
        [releases.pop() for i in range(number)]
        for release in releases:
            run(f"rm -rf {release}")
