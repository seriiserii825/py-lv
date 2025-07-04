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

    files_handler = FilesHandle("app/Http/Controllers")
    result = files_handler.getDir()
    selected_dir = result["selected_dir"]
    controller_name = input("Controller name like 'Flight', will be FlightController: ")
    controller_name = selected_dir + "/" + controller_name
    controller_name = f"{controller_name}Controller"

    if option == "1":
        os.system(
            f"docker-compose exec php-fpm php artisan make:controller {controller_name}"
        )
    elif option == "2":
        os.system(
            f"docker-compose exec php-fpm php artisan make:controller {controller_name}\
            --resource"
        )
    elif option == "3":
        os.system(
            f"docker-compose exec php-fpm php artisan make:controller {controller_name}\
            --api"
        )
    elif option == "4":
        return True
    elif option == "5":
        print("[red]Good bye!")
        exit()
    else:
        exit()
