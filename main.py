from checks.system_check import system_info
from checks.sudo_check import check_sudo
from checks.writable_check import check_writable_files
from checks.passwd_check import check_passwd_hash
from checks.cron_check import check_cron
from checks.suid_check import check_suid
from checks.path_check import check_path
from checks.capabilities_check import check_capabilities
from checks.ssh_key_check import  check_ssh_keys
from checks.kernel_check import check_kernel
from checks.services_check import check_services


def main():
    print("=== pyPrivesc v1.0 by Sarma ===")

    system_info()
    check_sudo()
    check_writable_files()
    check_passwd_hash()
    check_cron()
    check_suid()
    check_path()
    check_capabilities()
    check_ssh_keys()
    check_kernel()
    check_services()



if __name__ == "__main__":
    main()

## In Python, if __name__ == "__main__" ensures that certain code runs only when the script is executed directly.
# When the file is imported as a module, the code inside this block does not run,
# which helps prevent unintended execution and improves modular program design.
