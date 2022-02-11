#
# ───────────────────────────────────────────────────────────────────────
#   :::::: I N S T A L L I N G : :  :   :    :     :        :          :
# ───────────────────────────────────────────────────────────────────────
#

import os
import subprocess
import sys
from update import filecomment

if os.geteuid() == 0:

    HEADER = '\033[95m'
    BLUE = '\033[94m'
    ORANGE = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    print(f"{BOLD}{UNDERLINE}{ORANGE}<========== Installing... ==========>{ENDC}")
    print(f"{BOLD}Where do you want to install simple-workspaces?{ENDC}\n\n\t1. /usr/bin <== Recommended\n\t2. Other")

    inp: str = input(f"{BOLD}Enter the number of your choice (Default is 1): {ENDC}")

    if inp == "2":
        PATH = input(f"{BOLD}Enter the path where you want to install simple-workspaces (You can edit it in the config/config file later): {ENDC}")
    else:
        PATH = "/usr/bin"

    print(f"\n\n{BOLD}Where do you want to save the workspaces?{ENDC}\n\n\t1. {os.getcwd()}/workspaces <== Recommended\n\n\t2. Other")
    inp = input(f"\n\n{BOLD}Enter the number of your choice (Default is 1: )")

    if inp == "2":
        print(f"{FAIL}{BOLD}⚠️ WARNING:{ENDC}{FAIL} Just enter the DIRECTORY, {BOLD}not the file{ENDC}")
        workspace_path = input(f"{BOLD}Enter the path where you want to save the workspaces: {ENDC}")

        if not os.path.exists(workspace_path):
            print(f"{BLUE}Path does not exit, creating {workspace_path}")
            os.mkdir(workspace_path)
    else:
        workspace_path = os.getcwd()

    # If the directory config does not exist, create it.
    try:
        os.mkdir("config")
    except:
        pass

    try:
        open(f"{workspace_path}/config/config")
    except:
        open(f'{workspace_path}config/config', 'x')
        print(f"{BLUE}Creating config/config file!{ENDC}")

    with open(f"{workspace_path}/config/config", "w") as f:
        f.write(f"PATH={PATH}\nWORKSPACES_PATH={workspace_path}")
        config_path = f"{workspace_path}/config/config"

    print(f"{BOLD}Installing binary...{ENDC}")

    # First, we create the binary

    print(f"{ORANGE}Creating binary...{ENDC}")
    with open(f"{PATH}/simple-workspaces", "w") as f:
        f.write(f"#!/bin/bash\npython3 {workspace_path}/mainscript.py {config_path} $@ || echo \"Path not found, if you want to uninstall simple-workspaces, run simple-workspaces uninstall\"\n\n if [ $1 = 'uninstall'] then rm -- \"$0\" fi")

    # And then we make it executable
    print(f"{ORANGE}Making it executable...{ENDC}")
    os.system(f"sudo chmod +x {PATH}/simple-workspaces")

    # Now, we create the workspaces directory
    try:
        os.mkdir(workspace_path)
    except:
        try:
            open(f"{workspace_path}/workspaces")
        except:
            try:
                open(f"{workspace_path}/workspaces", "x")
            except:
                print(f"{FAIL}ERROR: Cannot open directory{ENDC}")
                exit()
        else:
            with open(f"{workspace_path}/workspaces", "w") as f:
                f.write(filecomment)

    print(f"{BOLD}{HEADER}<========== Installed! ==========>{ENDC}")
else:
    subprocess.call(['sudo', 'python3'] + sys.argv)