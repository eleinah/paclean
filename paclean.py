from rich.table import Table

from textual.app import App, ComposeResult
from textual.widgets import Static, Footer

from pkg_actions import get_explicit_pkgs, get_pkg_size, get_install_date


class PackageList(Static):

    def on_mount(self: None):
        pkg_list = get_explicit_pkgs()
        table = Table("Packages", "Size", "Installed On")
        for pkg in pkg_list:
            size = get_pkg_size(pkg)
            date = get_install_date(pkg)
            table.add_row(pkg, size, date)
        self.update(table)

class PacLean(App):
    CSS_PATH = "layout.tcss"
    TITLE = "PacLean"
    SUB_TITLE = "An interactive package cleaner for Arch Linux"
    BINDINGS = [
        ("up", "TEST")
    ]

    def compose(self: ComposeResult):
        yield PackageList()


        yield Footer()

if __name__ == "__main__":
    PacLean().run()