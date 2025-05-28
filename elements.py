from rich.text import Text
from textual.containers import ScrollableContainer
from textual.widgets import SelectionList, Static, Button
from textual.widgets.selection_list import Selection
from pkg_actions import get_explicit_pkgs, get_pkg_size, get_pkg_info, rem_pkg, rem_cache
from shutil import which
from datetime import datetime

class PackageList(SelectionList):
    """Widget that displays a table of packages with sizes and install dates"""

    pkg_list = get_explicit_pkgs()

    selections = []
    selected_pkgs = []
    clear_cache = []

    if which("paccache") is not None:
        selections.append(Selection(Text("**CLEAR PACMAN CACHE?**", style="italic"), True))
    else:
        selections.append(Selection(Text("**CLEAR PACMAN CACHE?** (must install pacman-contrib)", style="italic"), True, disabled=True))

    for pkg in pkg_list:
        size = get_pkg_size(pkg)
        display_txt = Text(f"{pkg}   ", style="bold") + Text(f"{size}", style="italic")
        selections.append(Selection(display_txt, pkg))

    def on_mount(self) -> None:
        self.border_title = "Package List"
        self.add_options(self.selections)

        if self.selections:
            self.highlighted = 0

    def on_selection_list_selection_highlighted(self, event: SelectionList.SelectionHighlighted) -> None:
        """Called when a selection is highlighted"""
        if event.selection is not None:
            if event.selection.prompt == "**CLEAR PACMAN CACHE?**":
                try:
                    info_placeholder = Text("Select this to clear the pacman cache with paccache. (runs 'paccache -r -vu -k 0')")
                    package_info_widget = self.app.query_one(PackageInfo)
                    package_info_widget.remove_children()
                    package_info_widget.mount(Static(info_placeholder))
                except Exception as e:
                    error = Text(f"Failed to display info placeholder for cache clear option: {str(e)}")
                    package_info_widget = self.app.query_one(PackageInfo)
                    package_info_widget.remove_children()
                    package_info_widget.mount(Static(error))

            else:
                try:
                    pkg_name = event.selection.value
                    package_info_widget = self.app.query_one(PackageInfo)
                    package_info_widget.update_package_info(pkg_name)
                except Exception as e:
                    pkg_name = event.selection.value
                    error = Text(f"Failed to display {pkg_name}: {str(e)}")
                    package_info_widget = self.app.query_one(PackageInfo)
                    package_info_widget.remove_children()
                    package_info_widget.mount(Static(error))

    def on_selection_list_selection_toggled(self, event: SelectionList.SelectionToggled) -> None:
        """Called when a selection is toggled"""

        if event.selection is not None:
            if event.selection.prompt == "**CLEAR PACMAN CACHE?**":
                if event.selection.value not in self.clear_cache:
                    self.clear_cache.append(event.selection.value)
                elif event.selection.value in self.clear_cache:
                    del self.clear_cache[self.clear_cache.index(event.selection.value)]
            else:
                pkg_name = event.selection.value
                if pkg_name not in self.selected_pkgs:
                    self.selected_pkgs.append(pkg_name)
                elif pkg_name in self.selected_pkgs:
                    del self.selected_pkgs[self.selected_pkgs.index(pkg_name)]

class PackageInfo(ScrollableContainer):
    """Widget that displays information about a selected package"""

    def on_mount(self) -> None:
        self.border_title = "Package Info"
        info_placeholder = Text("")
        self.mount(Static(info_placeholder))

    def update_package_info(self, pkg_name: str) -> None:
        """Update the display with the info about the selected package"""
        try:
            package_info = get_pkg_info(pkg_name)
            if pkg_name in PackageList.selected_pkgs:
                text = Text(package_info, style="red")
            if pkg_name not in PackageList.selected_pkgs:
                text = Text(package_info)
            self.remove_children()
            self.mount(Static(text))
        except Exception as e:
            self.remove_children()
            self.mount(Static(f"Error getting info for {pkg_name}: {e}"))

class RunAndExit(Button):

    def on_mount(self) -> None:
        self.border_title = "Run & Exit"
        self.label = "Clear selected packages"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        pass
