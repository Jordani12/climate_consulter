import subprocess, os

def clean_terminal():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)