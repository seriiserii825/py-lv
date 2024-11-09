import os
from rich import print

def artisan():
    print("[green]1. Command")
    print("[red]6. Exit")

    option = input("Select an option: ")

    if option == '1':
        artisan_command = input("Artisan command like 'breez:install': ")
        os.system(f"docker-compose exec php-fpm php artisan {artisan_command}")
    elif option == '6':
        print("[red]Good bye!")
        exit()
    else:
        print("[red]Invalid option")
        artisan()

