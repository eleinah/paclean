from textual.widgets import SelectionList, Static
from textual.widgets.selection_list import Selection
from pkg_actions import get_explicit_pkgs, get_pkg_size, get_install_date


class PackageList(SelectionList):
    """Widget that displays a table of packages with sizes and install dates"""

    pkg_list = get_explicit_pkgs()

    selections = []

    for pkg in pkg_list:
        size = get_pkg_size(pkg)
        display_txt = rf"{pkg}   \[{size}]"
        selections.append(Selection(display_txt, pkg))

    async def on_mount(self) -> None:
        self.pkg_list = get_explicit_pkgs()
        selections = []

        for pkg in self.pkg_list:
            size = get_pkg_size(pkg)
            display_txt = rf"{pkg}   \[{size}]"
            selections.append(Selection(display_txt, pkg))

        self.add_options(selections)

class PackageInfo(Static):
    """Widget that displays information about a selected package"""

    def on_mount(self) -> None:
        self.update("Select a package to view its information")