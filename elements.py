from rich.table import Table
from textual.widgets import Static

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
