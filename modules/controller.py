import os
from rich import print

from classes.FilesHandle import FilesHandle


def controller():
    print("[green]1. Simple")
    print("[blue]2. Resource")
    print("[green]3. Api")
    print("[yellow]4. Back")
    print("[red]5. Exit")

    option = input("Select an option: ")

    result = getDir()
    selected_dir = result["selected_dir"]
    controller_name = input("Controller name like 'FlightController': ")
    controller_name = selected_dir + "/" + controller_name

    if option == '1':
        os.system(f"docker-compose exec php-fpm php artisan make:controller {controller_name}")
    elif option == '2':
        os.system(f"docker-compose exec php-fpm php artisan make:controller {controller_name} --resource")
    elif option == '3':
        os.system(f"docker-compose exec php-fpm php artisan make:controller {controller_name} --api")
    elif option == '4':
        return True
    elif option == '5':
        print("[red]Good bye!")
        exit()
    else:
        exit()

def getDir():
    dir_path = 'app/Http/Controllers'
    files_handler = FilesHandle(dir_path)
    selected_dir = files_handler.createOrChooseDirectory()
    dir_path = files_handler.basepath + "/" + selected_dir
    files_handler.drawTree(dir_path)
    print(f"dir_path: {dir_path}")
    if not os.path.exists(dir_path):
        print("[red]Directory does not exist")
        exit()
    return {
        "dir_path": dir_path,
        "selected_dir": selected_dir
    }
