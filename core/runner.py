import subprocess

def run(cmd):
    try:
        output = subprocess.check_output(cmd, shell=True)
        return output.decode().strip()
    except:
        return ""