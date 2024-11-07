import os

from modules.composer import composer


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

if __name__ == "__main__":
    menu()
