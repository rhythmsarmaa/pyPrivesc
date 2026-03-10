from core.runner import run


def check_services():

    print("\n[+] Checking running services (filtered)")

    processes = run("ps aux")

    if not processes:
        print("[!] Could not read process list")
        return

    interesting_paths = ["/home", "/opt", "/usr/local"]

    for line in processes.split("\n"):

        if not line.startswith("root"):
            continue

        parts = line.split()

        if len(parts) < 11:
            continue

        command = " ".join(parts[10:])

        words = command.split()

        for w in words:

            if w.startswith("/"):

                # show only interesting paths
                if not any(w.startswith(p) for p in interesting_paths):
                    continue

                print(f"\n[INFO] Root service: {command}")

                writable = run(f"test -w {w} && echo writable")

                if writable:
                    print(f"[HIGH] Writable service binary detected: {w}")
                else:
                    print(f"[OK] {w} not writable")

                break