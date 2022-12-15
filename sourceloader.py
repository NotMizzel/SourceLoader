import sys
import os
from time import sleep
import platform
import subprocess
from threading import Thread
import time
try:
    import patoolib
except ModuleNotFoundError:
    subprocess.run(["pip", "install", "patool"])


def InstallingForLinux():
    if len(sys.argv) != 1:
        patoolib.extract_archive(sys.argv[1], outdir=home_dir + '/.local/share/Steam/steamapps/sourcemods', verbosity=-1)
        print('\033[32m', 'Mod Installed Successfully')
        sleep(3)


if platform.system() == 'Linux':
    home_dir = os.path.expanduser('~')
    if len(sys.argv) == 1:
        print('\033[31m', "FATAL ERROR: No Input File")
        sleep(5)
        sys.exit(1)
thread = Thread(target=InstallingForLinux())
thread.start()
for time in range(InstallingForLinux()):
            sys.stdout.write("\r")
            sys.stdout.write("/".format(time))
            sys.stdout.flush()
            time.sleep(1)
if platform.system() == 'Windows':
    if len(sys.argv) == 1:
        print('\033[31m', "FATAL ERROR: No Input File")
        sleep(5)
        sys.exit(1)

    if len(sys.argv) != 1:
        patoolib.extract_archive(sys.argv[1], outdir="C:/Program Files (x86)/Steam/steamapps/sourcemods", verbosity=-1)
        print('\033[32m', 'Mod Installed Successfully')
    sleep(3)
