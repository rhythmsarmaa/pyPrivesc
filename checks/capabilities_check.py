from core.runner import run


def check_capabilities():

    print("\n[+] Checking Linux capabilities")

    caps = run("getcap -r / 2>/dev/null")

    if not caps:
        print("[OK] No capability-enabled binaries found")
        return

    print("\n[INFO] Capability binaries found:\n")

    for line in caps.split("\n"):

        if not line.strip():
            continue

        print(line)

    print("\n[INFO] Checking for interesting capability binaries")

    interesting_caps = [
        "cap_setuid",
        "cap_setgid",
        "cap_sys_admin",
        "cap_dac_override",
        "cap_dac_read_search"
    ]

    for line in caps.split("\n"):

        for cap in interesting_caps:

            if cap in line:
                print(f"[HIGH] Interesting capability found: {line}")