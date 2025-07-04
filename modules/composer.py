import os

from rich import print


def composer():
    print("[green]1. Install all")
    print("[blue]2. Install package")
    print("[green]3. Update package")
    print("[blue]4. Require package")
    print("[green]5. Dump autoload package")
    print("[yellow]6. Back")
    print("[red]7. Exit")

    option = input("Select an option: ")
    if option == "1":
        os.system("docker-compose exec php-fpm composer install")
        composer()
    elif option == "2":
        package = input("Enter the package name: ")
        os.system(f"docker-compose exec php-fpm composer require {package}")
        composer()
    elif option == "3":
        package = input("Enter the package name: ")
        os.system(f"docker-compose exec php-fpm composer update {package}")
        composer()
    elif option == "4":
        package = input("Enter the package name: ")
        os.system(f"docker-compose exec php-fpm composer require {package}")
        composer()
    elif option == "5":
        os.system("docker-compose exec php-fpm composer dump-autoload")
        composer()
    elif option == "6":
        return True
    elif option == "7":
        print("[red]Good bye!")
        exit()
    else:
        print("[red]Invalid option")
        composer()
