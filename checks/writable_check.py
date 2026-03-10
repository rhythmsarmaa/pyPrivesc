from core.runner import run

def check_writable_files():
    print("\n[+] Checking sensitive file permissions...")

    sensitive_files = [
        "/etc/passwd",
        "/etc/shadow",
        "/etc/sudoers",
        "/etc/crontab"
    ]
    # Take each item from the list sensitive_files one by one and store it in the variable file.
    for file in sensitive_files:

        # Use an f-string to interpolate the variable.
        # Without `f`, "{file}" is treated as a literal string and will not be replaced.
        # Example: f"ls -l {file}" -> "ls -l /etc/passwd"

        writable = run(f"test -w {file} && echo writable")
        readable = run(f"test -r {file} && echo readable")

        #show actual permissions
        perm = run(f"ls -l {file}")

        if writable:
            print(f"[!] {file} is WRITABLE! POssible Priviledge Escalation ...")
            print("Permission details:")
            print(perm)

        elif file == "/etc/shadow" and readable:
            print(f"[!] {file} is READABLE! Password hashes may be exposed...")  # even if shadow file is readable we can crack hashes unlike other files.
            print("Permission details:")
            print(perm)

        else:
            print(f"[OK] {file} Permission looks Normal")
            print(perm)
            

