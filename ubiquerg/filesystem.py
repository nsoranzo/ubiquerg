""" Filesystem utility functions """

import os

__author__ = "Vince Reuter"
__email__ = "vreuter@virginia.edu"

__all__ = ["expandpath"]


def expandpath(path):
    """
    Expand a filesystem path that may or may not contain user/env vars.

    :param str path: path to expand
    :return str: expanded version of input path
    """
    return os.path.expandvars(os.path.expanduser(path)).replace("//", "/")
