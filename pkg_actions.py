import subprocess
import shutil
from sys import exit

if shutil.which("expac") is not None:
    def get_explicit_pkgs() -> dict:
        """Returns all explicitly installed packages as individual strings inside a list"""

        process_result = subprocess.run(
        ["pacman", "-Qeqt"],
        capture_output=True,
        text=True,
        check=True
        )

        pkgs = process_result.stdout.strip().split("\n")
        return pkgs

    def get_pkg_info(pkg: str) -> str:
        """Returns the full info of a given package (pkg: str)"""

        process_result = subprocess.run(
            ["pacman", "-Qi", pkg],
            capture_output=True,
            text=True,
            check=True
        )

        info = process_result.stdout.strip()
        return info

    def get_pkg_size(pkg: str) -> str:
        """Returns the size of a given package (pkg: str)"""

        process_result = subprocess.run(
            ["expac", "-H", "M", "%m", pkg],
            capture_output=True,
            text=True,
            check=True
        )

        size = process_result.stdout.strip()
        return size

    def rem_cache(amt_kept: str = "0") -> str:
        """Clears the pacman cache and keeps the specified amount (amt_kept: str, default="0")"""

        if amt_kept.strip().isnumeric() == True and 0 <= int(amt_kept) <= 9223372036854775807:
            pass
        else:
            raise Exception("amt_kept must only be numeric and 0-9223372036854775807")
        process_result = subprocess.run(
            ["paccache", "-d", "-vu", "-k", amt_kept],
            capture_output=True,
            text=True,
            check=True
        )
        output = process_result.stdout.strip()
        return output

    def rem_pkg(pkg: str) -> str:
        """Removes selected packages"""

        process_result = subprocess.run(
            ["pacman", "--noprogressbar", "-Rns", pkg],
            capture_output=True,
            text=True,
            check=True
        )
        removed = process_result.stdout.strip()
        return removed

else:
    print("Please install 'expac' to use this tool.")
    exit(1)