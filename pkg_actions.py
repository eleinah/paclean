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

def get_pkg_info(pkg: str):
    """
    Returns the full info of a given package (str: pkg)
    """
    payload = subprocess.run(
        ["pacman", "-Qi", pkg],
        capture_output=True,
        text=True
    )

    payload.check_returncode()
    info = payload.stdout.strip()
    return info

def get_pkg_size(pkg: str):
    """
    Returns the size of a given package (str: pkg)
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

def rem_cache(amt_kept: str = "0", dry: bool = False):
    """
    Clears the pacman cache and keeps the specified amount (str: amt_kept, default=0)
    """
    if amt_kept.isnumeric != True:
        raise Exception("amt_kept must only be numeric")
    if dry == True:
        payload = subprocess.run(
            ["paccache", "-d", "-vu", "-k", amt_kept],
            capture_output=True,
            text=True
        )
    else:
        payload = subprocess.run(
            ["paccache", "-r", "-vu", "-k", amt_kept],
            capture_output=True,
            text=True
        )
    payload_result = payload.stdout.strip()
    return payload_result