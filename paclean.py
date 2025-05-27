from textual.app import App, ComposeResult
from textual.widgets import Footer
from elements import PackageList, PackageInfo
import shutil
from sys import exit

class PacLean(App):
    CSS_PATH = "layout.tcss"
    TITLE = "PacLean"
    SUB_TITLE = "An interactive package cleaner for Arch Linux"

    def compose(self) -> ComposeResult:
        yield PackageList()
        yield PackageInfo()
        yield Footer()

if __name__ == "__main__":
    if shutil.which("expac") is not None:
        PacLean().run()
    else:
        print("Please install 'expac' to use this tool")
        exit(1)