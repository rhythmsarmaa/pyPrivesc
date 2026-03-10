from core.runner import run


def check_suid():

    print("\n[+] Checking SUID binaries")

    suid_files = run("find / -perm -4000 2>/dev/null")

    if not suid_files:
        print("[!] No SUID files found or permission denied")
        return

    print("\n[INFO] SUID files found:")

    for file in suid_files.split("\n"):

        if not file.strip():
            continue

        print(file)

    # highlight interesting binaries
    print("\n[INFO] Checking for interesting SUID binaries")

    interesting = [
        "bash",
        "sh",
        "dash",
        "zsh",
        "find",
        "nmap",
        "vim",
        "nano",
        "perl",
        "python",
        "python3",
        "ruby",
        "tar",
        "cp",
        "mv",
        "less",
        "more"
    ]

    for file in suid_files.split("\n"):

        for name in interesting:

            if file.endswith(name):
                print(f"[HIGH] Interesting SUID binary found: {file}")