import os

def artisan():
    artisan_command = input("Artisan command like 'breez:install': ")
    os.system(f"docker-compose exec php-fpm php artisan {artisan_command}")
    exit()
