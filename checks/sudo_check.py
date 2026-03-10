from core.runner import run

def check_sudo():

    print("\n[+] Checking sudo permissions")
    output = run("sudo -n -l 2>/dev/null")   #-n means non interactive mode. if asks pawword fails silently and moves to other task. does not hang..

    if "NOPASSWD" in output:
        print("[!] Passwordless sudo detected!")
        print(output)

    else:
        print("No obvious sudo misconfiguration found")
