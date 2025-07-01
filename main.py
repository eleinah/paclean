import sys
from textual.app import App, ComposeResult
from elements import PackageList, PackageInfo, RunAndExit
from pkg_actions import log_filename, log_dir
from os import getuid, execvp, path, makedirs


def get_style_path(filename: str) -> str:
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = path.abspath(path.dirname(__file__))
    return path.join(base_path, filename)

class PacLean(App):
    CSS_PATH = get_style_path("layout.tcss")
    TITLE = "PacLean"
    SUB_TITLE = "An interactive package cleaner for Arch Linux"

    def compose(self) -> ComposeResult:
        yield PackageList()
        yield PackageInfo()
        yield RunAndExit()

def elevate():
    if getuid() != 0:
        cmd = ("sudo", sys.executable, *sys.argv)
        execvp("sudo", cmd)

if __name__ == "__main__":
    elevate()
    makedirs(log_dir, exist_ok=True)
    result = PacLean().run()

    if result == "process complete":
        print(f"PacLean finished running. See '{log_filename}' to review what was done and removed.")