import os

from py_libs.Select import Select
from rich import print


def nodeFunc():
    menu = ["Exec", "Install"]

    menu_entry = Select.select_fzf_one(menu)
    print(f"menu_entry: {menu_entry}")

    if menu_entry == "Exec":
        print("[blue]Node Exec")
        command = input("Enter command: ")
        os.system(f"docker compose exec node {command}")

    if menu_entry == "Install":
        print("[blue]Node Install")
        command = input("Enter package name: ")
        os.system(f"docker compose exec node npm install {command}")
