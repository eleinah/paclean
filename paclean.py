from textual.app import App, ComposeResult
from textual.widgets import Footer
from elements import PackageList, PackageInfo


class PacLean(App):
    CSS_PATH = "layout.tcss"
    TITLE = "PacLean"
    SUB_TITLE = "An interactive package cleaner for Arch Linux"

    def compose(self) -> ComposeResult:
        yield PackageList()
        yield PackageInfo()
        yield Footer()

if __name__ == "__main__":
    PacLean().run()