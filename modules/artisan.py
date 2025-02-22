import os
from rich import print

def artisan():
    print("[green]1. Command")
    print("[red]6. Exit")

    artisan_command = input("Artisan command like 'breez:install': ")
    os.system(f"docker-compose exec php-fpm php artisan {artisan_command}")
    exit()
