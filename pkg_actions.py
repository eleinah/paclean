import subprocess

def get_explicit_pkgs():
    """
    Returns all explicitly installed packages as individual strings inside of a list
    """
    payload = subprocess.run(
    ["pacman", "-Qeqt"],
    capture_output=True,
    text=True
    )

    payload.check_returncode()
    pkgs = payload.stdout.strip().split("\n")
    return pkgs

def get_pkg_info(pkg):
    """
    Returns the full info of a given package (pkg)
    """
    payload = subprocess.run(
        ["pacman", "-Qi", pkg],
        capture_output=True,
        text=True
    )

    payload.check_returncode()
    info = payload.stdout.strip()
    return info

def get_pkg_size(pkg):
    """
    Returns the size of a given package (pkg)
    """
    payload = subprocess.run(
        ["expac", "-H", "M", "%m", pkg],
        capture_output=True,
        text=True
    )

    payload.check_returncode()
    unsplit_return = payload.stdout.strip()
    split_return = unsplit_return.split("\t")
    size = split_return[0]
    return size
