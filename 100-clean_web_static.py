#!/usr/bin/python3
"""Cleans up old archives and releases from the server."""

import os
from fabric.api import env, run, cd, lcd, local

env.hosts = ['3.83.253.65', '3.84.239.237']


def do_clean(number=0):
    """Cleans up old archives and releases from the server."""

    # Convert number to an integer, default to 1 if 0 or invalid
    number = max(1, int(number))

    # Remove old archives
    archives_path = "versions"
    archives = sorted(os.listdir(archives_path))
    with lcd(archives_path):
        for archive in archives[:-number]:
            local("rm {}".format(archive))

    # Remove old releases
    releases_path = "/data/web_static/releases"
    with cd(releases_path):
        releases = run("ls -tr | grep 'web_static_'").split()
        for release in releases[:-number]:
            run(f"rm -rf {release}")
