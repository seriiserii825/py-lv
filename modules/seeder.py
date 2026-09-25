import os

from py_libs.Select import Select

menu_items = ["Create", "Run", "Exit"]


def seeeder():
    option = Select.select_fzf_one(menu_items)

    if option == "Create":
        seeder_name = input("Seeder name like 'Flights': ")
        seeder_name = seeder_name + "Seeder"
        os.system(f"docker compose exec php-fpm php artisan make:seeder {seeder_name}")
        exit()
    elif option == "Run":
        os.system("docker compose exec php-fpm php artisan db:seed")
        exit()
    elif option == "Exit":
        exit()
    else:
        exit()
