from core.runner import run


def check_services():

    print("\n[+] Checking running services")

    processes = run("ps aux")

    if not processes:
        print("[!] Could not read process list")
        return

    print("\n[INFO] Checking root-owned processes")

    for line in processes.split("\n"):

        if not line.startswith("root"):
            continue

        parts = line.split()

        if len(parts) < 11:
            continue

        command = " ".join(parts[10:])

        print(f"\n[INFO] Root process: {command}")

        # try extracting executable path
        words = command.split()

        for w in words:

            if w.startswith("/"):

                writable = run(f"test -w {w} && echo writable")

                if writable:
                    print(f"[HIGH] Writable service binary detected: {w}")
                else:
                    print(f"[OK] {w} not writable")

                break