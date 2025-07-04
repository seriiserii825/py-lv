import os

from pyfzf.pyfzf import FzfPrompt

menu_items = ["Create", "Run", "Exit"]


def seeeder():
    fzf = FzfPrompt()
    option = fzf.prompt(menu_items)

    if option[0] == "Create":
        seeder_name = input("Seeder name like 'Flights': ")
        seeder_name = seeder_name + "Seeder"
        os.system(f"docker-compose exec php-fpm php artisan make:seeder {seeder_name}")
        exit()
    elif option[0] == "Run":
        os.system("docker-compose exec php-fpm php artisan db:seed")
        exit()
    elif option[0] == "Exit":
        exit()
    else:
        exit()
