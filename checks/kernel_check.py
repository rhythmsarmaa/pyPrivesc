from core.runner import run


def check_kernel():

    print("\n[+] Checking kernel information")

    # STEP 1 — kernel version
    kernel_version = run("uname -r")

    if kernel_version:
        print(f"\n[INFO] Kernel version: {kernel_version}")
    else:
        print("[!] Could not detect kernel version")

    # STEP 2 — full system info
    full_info = run("uname -a")

    if full_info:
        print("\n[INFO] Full kernel info:")
        print(full_info)

    # STEP 3 — basic warning logic (simple)
    print("\n[INFO] Basic kernel risk check")

    try:
        version_parts = kernel_version.split(".")
        major = int(version_parts[0])
        minor = int(version_parts[1])

        if major < 4:
            print("[HIGH] Very old kernel detected → high chance of exploits")

        elif major == 4 and minor < 8:
            print("[WARNING] Old kernel detected → check exploit-db")

        else:
            print("[OK] Kernel not obviously vulnerable")

    except:
        print("[INFO] Could not analyze kernel version")