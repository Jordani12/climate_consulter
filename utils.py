import subprocess, os
from time import sleep

def clean_terminal():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

def loading():
    quantities = 0
    while(quantities <= 2):
        print(".", end="", flush=True)
        quantities += 1
        sleep(1)
    print()
