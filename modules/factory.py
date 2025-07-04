import os

from pyfzf.pyfzf import FzfPrompt

menu_items = ["Create", "Exit"]


def factory():
    fzf = FzfPrompt()
    option = fzf.prompt(menu_items)

    if option[0] == "Create":
        factory_name = input("Factory name like 'Flights': ")
        factory_name = factory_name + "Factory"
        os.system(
            f"docker-compose exec php-fpm php artisan make:factory {factory_name}"
        )
        exit()
    elif option[0] == "Exit":
        exit()
    else:
        exit()
