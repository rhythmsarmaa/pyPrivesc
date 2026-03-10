from core.runner import run

def system_info():
    print("\n [+] System Information")

    print("User:")
    print(run("whoami"))

    print("\nUser ID:")
    print(run("id"))

    print("\nKernel:")
    print(run("uname -a"))
