import subprocess

def get_explicit_pkgs():
    payload = subprocess.run(
    ["pacman", "-Qeqt"],
    capture_output=True,
    text=True
    )

    payload.check_returncode()
    return payload.stdout.strip()



def main():
    pass




if __name__ == "__main__":
    main()
