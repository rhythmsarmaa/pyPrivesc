from core.runner import run


def check_cron():

    print("\n[+] Checking cron jobs")

    crontab = run("cat /etc/crontab")

    if not crontab:
        print("[!] Could not read /etc/crontab")
        return

    print("\n[INFO] Checking root cron jobs")

    for line in crontab.split("\n"):

        line = line.strip()

        if not line or line.startswith("#"):
            continue

        parts = line.split()

        # cron format → m h dom mon dow user command
        if len(parts) >= 7:

            user = parts[5]
            command = " ".join(parts[6:])

            if user != "root":
                continue

            print(f"\n[INFO] Root job: {command}")

            # CASE 1 — full path check
            words = command.split()

            for w in words:

                if w.startswith("/"):

                    writable = run(f"test -w {w} && echo writable")

                    if writable:
                        print(f"[HIGH] Writable cron script: {w}")
                    else:
                        print(f"[OK] {w} not writable")

                    break

            else:
                print("[WARNING] No full path used (possible PATH hijack)")

    # STEP 2 — check cron directories

    print("\n[INFO] Checking cron directories")

    dirs = [
        "/etc/cron.d",
        "/etc/cron.daily",
        "/etc/cron.hourly",
        "/var/spool/cron"
    ]

    for d in dirs:

        writable = run(f"test -w {d} && echo writable")

        if writable:
            print(f"[HIGH] Writable directory: {d}")
        else:
            print(f"[OK] {d}")