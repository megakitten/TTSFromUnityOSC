import subprocess

def run(self, cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed