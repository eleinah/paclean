import subprocess

def get_explicit_pkgs():
    """
    Returns all explicitly installed packages as individual strings inside of a list
    """
    process_result = subprocess.run(
    ["pacman", "-Qeqt"],
    capture_output=True,
    text=True,
    check=True
    )

    pkgs = process_result.stdout.strip().split("\n")
    return pkgs

def get_pkg_info(pkg: str):
    """
    Returns the full info of a given package (str: pkg)
    """
    process_result = subprocess.run(
        ["pacman", "-Qi", pkg],
        capture_output=True,
        text=True,
        check=True
    )

    info = process_result.stdout.strip()
    return info

def get_pkg_size(pkg: str):
    """
    Returns the size of a given package (str: pkg)
    """
    process_result = subprocess.run(
        ["expac", "-H", "M", "%m", pkg],
        capture_output=True,
        text=True,
        check=True
    )

    unsplit_return = process_result.stdout.strip()
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
        process_result = subprocess.run(
            ["paccache", "-d", "-vu", "-k", amt_kept],
            capture_output=True,
            text=True,
            check=True
        )
    else:
        process_result = subprocess.run(
            ["paccache", "-r", "-vu", "-k", amt_kept],
            capture_output=True,
            text=True,
            check=True
        )
    process_result_result = process_result.stdout.strip()
    return process_result_result