from textual.app import App, ComposeResult
from elements import PackageList, PackageInfo, RunAndExit
import os
import sys

class PacLean(App):
    CSS_PATH = "layout.tcss"
    TITLE = "PacLean"
    SUB_TITLE = "An interactive package cleaner for Arch Linux"

    def compose(self) -> ComposeResult:
        yield PackageList()
        yield PackageInfo()
        yield RunAndExit()

def elevate():
    if os.getuid() != 0:
        cmd = ("sudo", sys.executable, *sys.argv)
        os.execvp("sudo", cmd)

if __name__ == "__main__":
    elevate()
    if os.geteuid() != 0:
        exit("PacLean must be run as root to properly access pacman operations.")
    else:
        PacLean().run()