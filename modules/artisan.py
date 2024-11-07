import os
from rich import print

def artisan():
    print("[green]1. Both")
    print("[blue]2. ShowModel")
    print("[green]3. Tinker")
    print("[red]4. Develop")
    print("[yellow]5. Back")
    print("[red]6. Exit")

    option = input("Select an option: ")

    if option == '1':
        artisan_command = input("Artisan command like 'breez:install': ")
        os.system(f"docker-compose exec php-fpm php artisan {artisan_command}")
    elif option == '2':
        model_name = input("Model name like 'Flight': ")
        os.system(f"docker-compose exec php-fpm php artisan model:show {model_name}")
    elif option == '3':
        os.system("docker-compose exec php-fpm php artisan tinker")
    elif option == '4':
        os.system("docker-compose exec php-fpm php artisan develop")
    elif option == '5':
        return True
    elif option == '6':
        print("[red]Good bye!")
        exit()
    else:
        print("[red]Invalid option")
        artisan()

