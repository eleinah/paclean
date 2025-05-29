from subprocess import run
from shutil import which
from sys import exit
from datetime import datetime
from os import path

log_dir = "/var/log/paclean"
log_filename = path.join(
    log_dir,
    f"run_{datetime.now().strftime('%Y%m%d-%H%M%S')}.log"
)

if which("expac") is not None:
    def get_explicit_pkgs() -> list:
        """Returns all explicitly installed packages as individual strings inside a list"""

        process_result = run(
        ["pacman", "-Qeqt"],
        capture_output=True,
        text=True,
        check=True
        )

        pkgs = process_result.stdout.strip().split("\n")
        return pkgs

    def get_pkg_info(pkg: str) -> str:
        """Returns the full info of a given package (pkg: str)"""

        process_result = run(
            ["pacman", "-Qi", pkg],
            capture_output=True,
            text=True,
            check=True
        )

        info = process_result.stdout.strip()
        return info

    def get_pkg_size(pkg: str) -> str:
        """Returns the size of a given package (pkg: str)"""

        process_result = run(
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
        process_result = run(
            ["paccache", "-r", "-vu", "-k", amt_kept],
            capture_output=True,
            text=True,
            check=True
        )
        output = process_result.stdout.strip()

        with open(log_filename, "a") as f:
            print(output, file=f)
        return output

    def rem_pkg(pkg: str) -> str:
        """Removes selected packages"""

        process_result = run(
            ["pacman", "--noprogressbar", "--noconfirm", "-Rns", pkg],
            capture_output=True,
            text=True,
            check=True
        )
        removed = process_result.stdout.strip()

        with open(log_filename, "a") as f:
            print(removed, file=f)
        return removed

else:
    print("Please install 'expac' to use this tool.")
    exit(1)