import os

from py_libs.Select import Select

menu_items = ["Create", "Exit"]


def factory():
    option = Select.select_fzf_one(menu_items)

    if option == "Create":
        factory_name = input("Factory name like 'Flights': ")
        factory_name = factory_name + "Factory"
        os.system(
            f"docker compose exec php-fpm php artisan make:factory {factory_name}"
        )
        exit()
    elif option == "Exit":
        exit()
    else:
        exit()
