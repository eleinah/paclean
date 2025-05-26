from textual.app import App, ComposeResult
from textual.widgets import Static


class PacLean(App):
    CSS_PATH = "layout.tcss"
    TITLE = "PacLean"
    SUB_TITLE = "An interactive package cleaner for Arch Linux"

    def compose(self: ComposeResult):
        yield Static("Left", classes="box", id="left-cell")
        yield Static("Top Right", classes="box")
        yield Static("Bottom Right", classes="box")

if __name__ == "__main__":
    PacLean().run()