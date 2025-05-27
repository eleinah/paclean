from textual.app import App, ComposeResult
from elements import PackageList, PackageInfo, RunAndExit


class PacLean(App):
    CSS_PATH = "layout.tcss"
    TITLE = "PacLean"
    SUB_TITLE = "An interactive package cleaner for Arch Linux"

    def compose(self) -> ComposeResult:
        yield PackageList()
        yield PackageInfo()
        yield RunAndExit()

if __name__ == "__main__":
    PacLean().run()