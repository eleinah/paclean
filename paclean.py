from textual.app import App, ComposeResult
from elements import PackageList, PackageInfo, RunAndExit
from pkg_actions import log_filename
from os import getuid, execvp
from sys import argv, executable

class PacLean(App):
    CSS_PATH = "layout.tcss"
    TITLE = "PacLean"
    SUB_TITLE = "An interactive package cleaner for Arch Linux"

    def compose(self) -> ComposeResult:
        yield PackageList()
        yield PackageInfo()
        yield RunAndExit()

def elevate():
    if getuid() != 0:
        cmd = ("sudo", executable, *argv)
        execvp("sudo", cmd)

if __name__ == "__main__":
    elevate()
    result = PacLean().run()

    if result == "process complete":
        print(f"PacLean finished running. See '{log_filename}' to review what was done and removed.")