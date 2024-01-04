import platform
import os

def is_windows_vm():
    if platform.system() != "Windows":
        return False

    try:
        # Check for the presence of the VMware Tools registry key
        key_path = r"SOFTWARE\VMware, Inc.\VMware Tools"
        with open(os.devnull, 'wb') as fnull:
            return os.system(f'reg query "{key_path}" > {fnull} 2>&1') == 0
    except Exception:
        return False

if is_windows_vm():
    print("The system is running on a Windows virtual machine.")
else:
    print("The system is not running on a Windows virtual machine or detection failed.")
