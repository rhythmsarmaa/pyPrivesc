from core.runner import run


def check_ssh_keys():

    print("\n[+] Checking SSH keys")

    # STEP 1 — current user SSH folder
    print("\n[INFO] Checking current user SSH directory")

    current_keys = run("ls -ld ~/.ssh 2>/dev/null && ls -l ~/.ssh 2>/dev/null")

    if current_keys:
        print(current_keys)

        writable = run("find ~/.ssh -name authorized_keys -writable 2>/dev/null")
        if writable:
            print("[CRITICAL] Writable authorized_keys found → add your public key")

        priv = run("find ~/.ssh -type f \\( -name 'id_rsa' -o -name '*.key' \\) -readable 2>/dev/null")
        if priv:
            print("[CRITICAL] Readable private key found → possible SSH login")
            print(priv)

    else:
        print("[OK] No accessible ~/.ssh directory")

    # STEP 2 — root SSH folder
    print("\n[INFO] Checking root SSH directory")

    root_keys = run("ls -ld /root/.ssh 2>/dev/null && ls -l /root/.ssh 2>/dev/null")

    if root_keys:
        print("[HIGH] Accessible root SSH keys found:")
        print(root_keys)

        writable = run("find /root/.ssh -name authorized_keys -writable 2>/dev/null")
        if writable:
            print("[CRITICAL] Writable root authorized_keys → ROOT ACCESS possible")

        priv = run("find /root/.ssh -type f \\( -name 'id_rsa' -o -name '*.key' \\) -readable 2>/dev/null")
        if priv:
            print("[CRITICAL] Readable ROOT private key found → direct root login possible")
            print(priv)

    else:
        print("[OK] Root SSH directory not accessible")

    # STEP 3 — check other users
    print("\n[INFO] Checking other users' SSH directories")

    passwd = run("cat /etc/passwd")

    for line in passwd.split("\n"):

        if not line.strip():
            continue

        parts = line.split(":")

        if len(parts) >= 6:

            user = parts[0]
            home = parts[5]
            ssh_dir = f"{home}/.ssh"

            exists = run(f"test -d {ssh_dir} && echo yes")

            if exists:

                listing = run(f"ls -ld {ssh_dir} 2>/dev/null && ls -l {ssh_dir} 2>/dev/null")

                if listing:
                    print(f"\n[HIGH] Accessible SSH dir: {ssh_dir}")
                    print(listing)

                    writable = run(f"find {ssh_dir} -name authorized_keys -writable 2>/dev/null")
                    if writable:
                        print(f"[CRITICAL] Writable authorized_keys in {user} → add public key")

                    priv = run(f"find {ssh_dir} -type f \\( -name 'id_rsa' -o -name '*.key' \\) -readable 2>/dev/null")
                    if priv:
                        print(f"[CRITICAL] Readable private key for {user} → SSH login possible")
                        print(priv)

    # STEP 4 — FULL SYSTEM SEARCH (CTF MODE 🔥)

    print("\n[INFO] Running full system SSH key scan (may take time)")

    deep_keys = run("find / -type f \\( -name 'id_rsa*' -o -name '*.key' \\) 2>/dev/null")

    if deep_keys:
        print("\n[CRITICAL] Possible SSH keys found system-wide:")
        print(deep_keys)

        # check readability
        for key in deep_keys.split("\n"):
            if key.strip():
                perm = run(f"ls -l {key} 2>/dev/null")
                print(perm)

    else:
        print("[OK] No extra SSH keys found system-wide")