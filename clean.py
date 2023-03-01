# remove any file that is __pycache__ or .pyc

import os
import sys


def clean_files(path):
    # all the file recursively
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".pyc"):
                os.remove(os.path.join(root, file))


# a function to remove empty directories
def clean_dirs(path):
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if dir == "__pycache__":
                os.rmdir(os.path.join(root, dir))


def clean(path):
    clean_files(path)
    clean_dirs(path)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        clean(sys.argv[1])
    else:
        clean(".")
