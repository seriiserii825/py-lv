import os

from modules.artisan import artisan
from modules.composer import composer
from modules.controller import controller
from modules.dockerFunc import dockerFunc
from modules.middlewareFunc import middlewareFunc
from modules.migration import migration
from modules.model import model
from modules.request import requestFunc
from modules.resourceFunc import resourceFunc
from rich import print

## check for laravel project
if not os.path.exists("artisan"):
    print("[red]This is not a laravel project")
    exit()

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
    print("[green]10. Docker")
    print("[red]11. Exit")

    option = input("Select an option: ")
    if option == "1":
        command = os.system("docker-compose exec php-fpm php artisan route:list")
        print(command)
        menu()
    elif option == "2":
        composer()
        menu()
    elif option == "3":
        migration()
        menu()
    elif option == "4":
        model()
        menu()
    elif option == "5":
        controller()
        menu()
    elif option == "6":
        requestFunc()
        menu()
    elif option == "7":
        resourceFunc()
        menu()
    elif option == "8":
        middlewareFunc()
        menu()
    elif option == "9":
        artisan()
        menu()
    elif option == "10":
        dockerFunc()
        menu()
    elif option == "11":
        print("[red]Good bye!")
        exit()
    else:
        print("[red]Invalid option")
        menu()
if __name__ == "__main__":
    menu()
