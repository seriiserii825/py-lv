import os

from modules.artisan import artisan
from modules.composer import composer
from modules.controller import controller
from modules.middlewareFunc import middlewareFunc
from modules.migration import migration
from modules.model import model
from modules.request import requestFunc
from modules.resourceFunc import resourceFunc


def menu():
    print("[green]1. Routes")
    print("[blue]2. Composer")
    print("[green]3. Migration")
    print("[blue]4. Model")
    print("[green]5. Controller")
    print("[blue]6. Request")
    print("[green]7. Resource")
    print("[blue]8. Middleware")
    print("[green]9. Artisan")
    print("[red]10. Exit")

    option = input("Select an option: ")
    if option == "" or option == "10":
        print("[red]Good bye!")
        exit()
    elif option == "1":
        command = os.system("docker-compose exec php-fpm php artisan route:list")
        print(command)
    elif option == "2":
        composer()
    elif option == "3":
        migration()
    elif option == "4":
        model()
    elif option == "5":
        controller()
    elif option == "6":
        requestFunc()
    elif option == "7":
        resourceFunc()
    elif option == "8":
        middlewareFunc()
    elif option == "9":
        artisan()
    else:
        print("[red]Good bye!")
        exit()
if __name__ == "__main__":
    menu()
