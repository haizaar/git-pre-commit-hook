"""Check correctness of *.ini files."""
import os
import fnmatch
from six.moves import configparser
from six.moves import cStringIO

DEFAULTS = {
    'files': '*.ini',
}


def check(file_staged_for_commit, options):
    basename = os.path.basename(file_staged_for_commit.path)
    if not fnmatch.fnmatch(basename, options.ini_files):
        return True
    contents = cStringIO.StringIO(file_staged_for_commit.contents)
    parser = configparser.RawConfigParser()
    try:
        parser.readfp(contents, file_staged_for_commit.path)
    except configparser.Error as e:
        print(e)
        return False
    else:
        return True
