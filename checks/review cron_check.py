'''from core.runner import run


def check_cron():

    print("\n[+] Checking cron jobs")

    # STEP 1 — read system crontab
    crontab = run("cat /etc/crontab")

    if not crontab:
        print("[!] Could not read /etc/crontab")
        return

    lines = crontab.split("\n")

    cron_jobs = []
    cron_path = ""

    # STEP 2 — extract PATH and root jobs
    for line in lines:

        line = line.strip()

        if not line or line.startswith("#"):
            continue

        if line.startswith("PATH="):
            cron_path = line.split("=", 1)[1]
            continue

        parts = line.split()

        # cron format → m h dom mon dow user command
        if len(parts) >= 7:

            user = parts[5]
            command = " ".join(parts[6:])

            if user == "root":
                cron_jobs.append(command)

    # STEP 3 — process each cron job
    for job in cron_jobs:

        print(f"\n[INFO] Root cron job found: {job}")

        # CASE 1 — FULL PATH
        if job.startswith("/"):

            writable = run(f"test -w {job} && echo writable")

            if writable:
                print(f"[HIGH] Writable cron script detected: {job}")

            else:
                print("[OK] Not writable")

        # CASE 2 — NO FULL PATH (PATH SEARCH)
        else:

            print("[INFO] No full path used. Checking PATH...")

            paths = cron_path.split(":")

            found = False

            for p in paths:

                possible = f"{p}/{job}"

                exists = run(f"test -f {possible} && echo yes")

                if exists:
                    found = True

                    writable = run(f"test -w {possible} && echo writable")

                    if writable:
                        print(f"[HIGH] Writable cron script detected: {possible}")
                    else:
                        print(f"[OK] Found at {possible}, not writable")

                    break

            # CASE 3 — PATH HIJACK
            if not found:

                print("[WARNING] Script not found in PATH")

                first_path = paths[0]

                writable_dir = run(f"test -w {first_path} && echo writable")

                if writable_dir:
                    print(f"[HIGH] PATH HIJACK possible!")
                    print(f"Create malicious script at: {first_path}/{job}")

                else:
                    print("[OK] PATH hijack not possible")

    # STEP 4 — check other cron directories
    print("\n[+] Checking other cron locations")

    cron_dirs = [
        "/etc/cron.d",
        "/etc/cron.daily",
        "/etc/cron.hourly",
        "/var/spool/cron"
    ]

    for d in cron_dirs:

        print(f"\n[INFO] Checking {d}")

        files = run(f"ls {d}")

        if not files:
            print("[OK] No files found or access denied")
            continue

        for f in files.split("\n"):

            path = f"{d}/{f}"

            writable = run(f"test -w {path} && echo writable")

            if writable:
                print(f"[HIGH] Writable cron file detected: {path}")
            else:
                print(f"[OK] {path}")
'''