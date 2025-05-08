import os
from rich import print
from pyfzf.pyfzf import FzfPrompt

fzf = FzfPrompt()

def nodeFunc():
    menu = [ "Exec", "Install"]

    menu_entry = fzf.prompt(menu, fzf_options='--layout=reverse')
    print(f'menu_entry: {menu_entry}')

    if menu_entry[0] == "Exec":
        print("[blue]Node Exec")
        command = input("Enter command: ")
        os.system(f"docker-compose exec node {command}")

    if menu_entry[0] == "Install":
        print("[blue]Node Install")
        command = input("Enter package name: ")
        os.system(f"docker-compose exec node npm install {command}")

