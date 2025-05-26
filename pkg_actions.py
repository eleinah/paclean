import subprocess

def get_explicit_pkgs():
    """
    Returns all explicitly installed packages as individual strings inside a list
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

def get_pkg_deps(pkg: str):
    """
    Returns all dependencies of a given package (str: pkg) as a list
    """
    process_result = subprocess.run(
        ["expac", "-S", "%D", pkg],
        capture_output=True,
        text=True,
        check=True
    )

    deps = process_result.stdout.strip().split(" ")
    clean_deps = list(filter(None, deps))
    return clean_deps

def get_pkg_desc(pkg: str):
    """
    Returns the description of a given package (str: pkg)
    """
    process_result = subprocess.run(
        ["expac", "-S", "%d", pkg],
        capture_output=True,
        text=True,
        check=True
    )

    desc = process_result.stdout.strip()
    return desc

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

    size = process_result.stdout.strip()
    return size

def rem_cache(amt_kept: str = "0", dry: bool = False):
    """
    Clears the pacman cache and keeps the specified amount (str: amt_kept, default="0")
    """
    if amt_kept.strip().isnumeric() == True and 0 <= int(amt_kept) <= 9223372036854775807:
        pass
    else:
        raise Exception("amt_kept must only be numeric and 0-9223372036854775807")
    if dry:
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
    output = process_result.stdout.strip()
    return output