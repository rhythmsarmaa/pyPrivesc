from core.runner import run

def check_passwd_hash():

    print("\n[+] Checking for password hashes in /etc/passwd")

    passwd_content = run("cat /etc/passwd")
    #loop through each line in /etc/passwd

    for line in passwd_content.splitlines():
        # splitlines() converts the text into individual lines
        # Split the line using ":" because /etc/passwd fields are separated by colon root:x:0:0:root:/root:/bin/bash
        parts = line.split(":")

        if len(parts) > 1: #means if lenght of parts is gt 1 .. it is a safety check to proceed further

            password_field = parts[1]

            if password_field.startswith("$"):
                print(f"[!] Password hash found in /etc/passwd for user: {parts[0]}")


