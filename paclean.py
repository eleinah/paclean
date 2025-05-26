from textual.app import App, ComposeResult
from textual.widgets import Footer

from elements import PackageList


class PacLean(App):
    CSS_PATH = "layout.tcss"
    TITLE = "PacLean"
    SUB_TITLE = "An interactive package cleaner for Arch Linux"
    BINDINGS = [
        ("up", "ACTION_UP", "Up"),
        ("down", "ACTION_DOWN", "Down")
    ]

    def compose(self: ComposeResult):
        yield PackageList()


        yield Footer()

if __name__ == "__main__":
    PacLean().run()