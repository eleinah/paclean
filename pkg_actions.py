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

def get_install_date(pkg):
    """
    Returns the installation date of a given package (str: pkg)
    """
    raw_date = subprocess.Popen(
        ["expac", "-Q", "%l", pkg],
        stdout=subprocess.PIPE
    )

    filtered_date = subprocess.Popen(
        ["awk", "{print $2, $3, $5}"],
        stdin=raw_date.stdout,
        stdout=subprocess.PIPE,
        text=True
    )

    stdout, stderr = filtered_date.communicate()
    return stdout.strip()

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