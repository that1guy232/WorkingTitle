# get all .py files in current directory recursively

import os
import sys


def count_lines(file):
    with open(file, "r") as f:
        return len(f.readlines())


def get_py_files(path):
    py_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))
    return py_files


if __name__ == "__main__":
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        path = os.getcwd()
    py_files = get_py_files(path)
    total_lines = 0
    for file in py_files:
        if file == os.path.join(path, "count.py"):
            continue
        total_lines += count_lines(file)
        # print just the file name without the path and the amount of lines
        print(
            file.split("\\")[-1], count_lines(file)
        )  # [1] for windows, [-1] for linux
        # print(file.split('\\/')[-1], count_lines(file))
    print("Total lines: ", total_lines)
