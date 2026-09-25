import os

from py_libs.Select import Select

menu_items = [
    "Show",
    "Create",
    "Migration",
    "Migration Seeder",
    "Migration Seeder Factory",
    "Exit",
]


def model():
    option = Select.select_fzf_one(menu_items)

    if option == "Show":
        model_name = input("Model name like 'Flight': ")
        os.system(f"docker compose exec php-fpm php artisan model:show {model_name}")
        exit()
    elif option == "Create":
        model_name = input("Model name like 'Flight': ")
        os.system(f"docker compose exec php-fpm php artisan make:model {model_name}")
        exit()
    elif option == "Migration":
        model_name = input("Model name like 'Flight': ")
        os.system(f"docker compose exec php-fpm php artisan make:model {model_name} -m")
        exit()
    elif option == "Migration Seeder":
        model_name = input("Model name like 'Flight': ")
        os.system(
            f"docker compose exec php-fpm php artisan make:model {model_name} -ms"
        )
        exit()
    elif option == "Migration Seeder Factory":
        model_name = input("Model name like 'Flight': ")
        os.system(
            f"docker compose exec php-fpm php artisan make:model {model_name} -msf"
        )
        exit()
    elif option == "Exit":
        exit()
