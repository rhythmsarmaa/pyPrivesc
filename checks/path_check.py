from core.runner import run


def check_path():

    print("\n[+] Checking PATH hijacking possibilities")

    path = run("echo $PATH")

    if not path:
        print("[!] Could not read PATH")
        return

    print(f"\n[INFO] PATH = {path}")

    print("\n[INFO] Checking writable PATH directories")

    for directory in path.split(":"):

        directory = directory.strip()

        if not directory:
            continue

        writable = run(f"test -w {directory} && echo writable")

        if writable:
            print(f"[HIGH] Writable PATH directory detected: {directory}")
        else:
            print(f"[OK] {directory}")