import os, shutil, getopt, sys

DEBUG = True
DATA_DIR = "../data"


def parseArgs():
    global DATA_DIR
    opts, args = getopt.getopt(sys.argv[1:], '', ["data-dir="])
    for opt, arg in opts:
        if opt == "--data-dir":
            DATA_DIR = arg
            
            
def main():
    if DEBUG:
        if os.path.isdir(DATA_DIR):
            # cleanup test data
            shutil.rmtree(DATA_DIR)
            return main(DATA_DIR)
        else:
            # setup test data
            os.mkdir(DATA_DIR)
            os.chdir(DATA_DIR)
            open("testfile", mode='w')

if __name__ == '__main__':
    print("""
     __    __     _____        ______     _____     __     ______   ______     ______
    /\ "-./  \   /\  __-.     /\  ___\   /\  __-.  /\ \   /\__  _\ /\  __ \   /\  == \\
    \ \ \-./\ \  \ \ \/\ \    \ \  __\   \ \ \/\ \ \ \ \  \/_/\ \/ \ \ \/\ \  \ \  __<
     \ \_\ \ \_\  \ \____-     \ \_____\  \ \____-  \ \_\    \ \_\  \ \_____\  \ \_\ \_\\
      \/_/  \/_/   \/____/      \/_____/   \/____/   \/_/     \/_/   \/_____/   \/_/ /_/
    License: LGPL v2.1
    """)
    parseArgs()
    main()
