import os


def composer():
    print("[green]1. Install all")
    print("[blue]2. Install package")
    print("[green]3. Update package")
    print("[blue]4. Require package")
    print("[green]5. Dump autoload package")

    option = input("Select an option: ")
    if option == "1":
        os.system("docker-compose exec php-fpm composer install")
    elif option == "2":
        package = input("Enter the package name: ")
        os.system(f"docker-compose exec php-fpm composer require {package}")
    elif option == "3":
        package = input("Enter the package name: ")
        os.system(f"docker-compose exec php-fpm composer update {package}")
    elif option == "4":
        package = input("Enter the package name: ")
        os.system(f"docker-compose exec php-fpm composer require {package}")
    elif option == "5":
        os.system("docker-compose exec php-fpm composer dump-autoload")
    else:
        print("Invalid option")
        composer()
