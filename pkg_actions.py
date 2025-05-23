import subprocess

def get_explicit_pkgs():
    '''
    Returns all explicitly installed packages as individual strings inside of a list
    '''
    payload = subprocess.run(
    ["pacman", "-Qeqt"],
    capture_output=True,
    text=True
    )

    payload.check_returncode()
    pkgs = payload.stdout.strip().split("\n")
    return pkgs