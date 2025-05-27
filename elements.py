from textual.containers import ScrollableContainer
from textual.widgets import SelectionList, Static
from textual.widgets.selection_list import Selection
from pkg_actions import get_explicit_pkgs, get_pkg_size, get_pkg_info


class PackageList(SelectionList):
    """Widget that displays a table of packages with sizes and install dates"""

    pkg_list = get_explicit_pkgs()

    selections = []

    for pkg in pkg_list:
        size = get_pkg_size(pkg)
        display_txt = rf"{pkg}   \[{size}]"
        selections.append(Selection(display_txt, pkg))

    def on_mount(self) -> None:
        self.add_options(self.selections)

        if self.selections:
            self.highlighted = 0

    def on_selection_list_selection_highlighted(self, event: SelectionList.SelectionHighlighted) -> None:
        """Called when a selection is highlighted"""
        if event.selection is not None:
            pkg_name = event.selection.value
            package_info_widget = self.app.query_one(PackageInfo)
            package_info_widget.update_package_info(pkg_name)

class PackageInfo(ScrollableContainer):
    """Widget that displays information about a selected package"""

    def on_mount(self) -> None:
        pkg_list = get_explicit_pkgs()

        if pkg_list:
            first_pkg = pkg_list[0]
            self.update_package_info(first_pkg)
        else:
            self.mount(Static("No packages found"))

    def update_package_info(self, pkg_name: str) -> None:
        """Update the display with the info about the selected package"""
        try:
            package_info = get_pkg_info(pkg_name)
            self.remove_children()
            self.mount(Static(package_info))
        except Exception as e:
            self.remove_children()
            self.mount(Static(f"Error getting info for {pkg_name}: {e}"))