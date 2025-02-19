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

from modules.viewFunc import viewFunc

## check for laravel project
if not os.path.exists("artisan"):
    print("[red]This is not a laravel project")
    exit()

def menu():
    print("[green]1. Component")
    print("[green]1.1 Routes")
    print("[green]1.2 Views")
    print("[blue]2. Composer")
    print("[green]3. Migration")
    print("[blue]4. Model")
    print("[green]5. Controller")
    print("[blue]6. Request")
    print("[green]7. Resource")
    print("[blue]8. Middleware")
    print("[green]9. Artisan")
    print("[green]9.1 Key Generate")
    print("[green]9.2 Tinker")
    print("[blue]10. Docker")
    print("[green]11. Clear")
    print("[red]12. Exit")

    option = input("Select an option: ")
    if option == "1":
        conponent_name = input("Enter the component name: ")
        if not conponent_name:
            print("[red]Component name is required")
            menu()
        command = os.system(f"docker-compose exec php-fpm php artisan make:component {conponent_name}")
        print(command)
        menu()
    elif option == "1.1":
        command = os.system("docker-compose exec php-fpm php artisan route:list")
        print(command)
        menu()
    elif option == "1.2":
        viewFunc()
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
    elif option == "9.1":
        os.system(f"docker-compose exec php-fpm php artisan key:generate")
        menu()
    elif option == "9.2":
        os.system(f"docker-compose exec php-fpm php artisan tinker")
        menu()
    elif option == "10":
        dockerFunc()
        menu()
    elif option == "11":
        os.system("docker-compose exec php-fpm php artisan view:clear && docker-compose exec php-fpm php artisan cache:clear && docker-compose exec php-fpm php artisan config:clear && docker-compose exec php-fpm php artisan route:clear")
        menu()
    elif option == "12":
        print("[red]Good bye!")
        exit()
    else:
        print("[red]Invalid option")
        menu()
if __name__ == "__main__":
    menu()
