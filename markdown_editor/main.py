import os, shutil, getopt, sys, subprocess

DEBUG = False
DATA_DIR = "../data"


def parse_args():
    global DATA_DIR, DEBUG
    opts, args = getopt.getopt(sys.argv[1:], 'd:', ["--debug", "data-dir="])
    for opt, arg in opts:
        if opt == "--data-dir":
            DATA_DIR = arg
        elif opt in ["-d", "--debug"]:
            DEBUG = True


def ensure_storage():
    if os.path.isdir(DATA_DIR):
        if DEBUG:
            # cleanup test data
            shutil.rmtree(DATA_DIR)
            return ensure_storage()
        else:
            os.chdir(DATA_DIR)
    else:
        # setup test data
        os.mkdir(DATA_DIR)
        os.chdir(DATA_DIR)
        proc = subprocess.Popen(["git", "init"])
        proc.wait()


def main():
    parse_args()
    ensure_storage()


if __name__ == '__main__':
    print("""
     __    __     _____        ______     _____     __     ______   ______     ______
    /\ "-./  \   /\  __-.     /\  ___\   /\  __-.  /\ \   /\__  _\ /\  __ \   /\  == \\
    \ \ \-./\ \  \ \ \/\ \    \ \  __\   \ \ \/\ \ \ \ \  \/_/\ \/ \ \ \/\ \  \ \  __<
     \ \_\ \ \_\  \ \____-     \ \_____\  \ \____-  \ \_\    \ \_\  \ \_____\  \ \_\ \_\\
      \/_/  \/_/   \/____/      \/_____/   \/____/   \/_/     \/_/   \/_____/   \/_/ /_/
    License: LGPL v2.1
    """)
    main()
