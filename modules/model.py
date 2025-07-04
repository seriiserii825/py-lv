import os

from pyfzf.pyfzf import FzfPrompt

menu_items = [
    "Show",
    "Create",
    "Migration",
    "Migration Seeder",
    "Migration Seeder Factory",
    "Exit",
]


def model():
    fzf = FzfPrompt()
    option = fzf.prompt(menu_items)

    if option[0] == "Show":
        model_name = input("Model name like 'Flight': ")
        os.system(f"docker-compose exec php-fpm php artisan model:show {model_name}")
        exit()
    elif option[0] == "Create":
        model_name = input("Model name like 'Flight': ")
        os.system(f"docker-compose exec php-fpm php artisan make:model {model_name}")
        exit()
    elif option[0] == "Migration":
        model_name = input("Model name like 'Flight': ")
        os.system(f"docker-compose exec php-fpm php artisan make:model {model_name} -m")
        exit()
    elif option[0] == "Migration Seeder":
        model_name = input("Model name like 'Flight': ")
        os.system(
            f"docker-compose exec php-fpm php artisan make:model {model_name} -ms"
        )
        exit()
    elif option[0] == "Migration Seeder Factory":
        model_name = input("Model name like 'Flight': ")
        os.system(
            f"docker-compose exec php-fpm php artisan make:model {model_name} -msf"
        )
        exit()
    elif option[0] == "Exit":
        exit()
