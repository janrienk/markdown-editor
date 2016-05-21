import os, shutil

DEBUG = True


def main(dataDir):
    if DEBUG:
        if os.path.isdir(dataDir):
            # cleanup test data
            shutil.rmtree(dataDir)
            main(dataDir)
        else:
            # setup test data
            os.mkdir(dataDir)
            os.chdir(dataDir)
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
    dataDir = "../data"
    main(dataDir)
