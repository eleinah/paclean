from rich.table import Table
from textual.widgets import Static

from pkg_actions import get_explicit_pkgs, get_pkg_size, get_install_date


class PackageList(Static):
    """Widget that displays a table of packages with sizes and install dates"""

    def on_mount(self: None):
        pkg_list = get_explicit_pkgs()
        table = Table("Packages", "Size", "Installed On", expand=True)
        for pkg in pkg_list:
            size = get_pkg_size(pkg)
            date = get_install_date(pkg)
            table.add_row(pkg, size, date)
        self.update(table)

class PackageInfo(Static):
    """Widget that displays information about a selected package"""

    def on_mount(self: None):
        self.update(PackageList())