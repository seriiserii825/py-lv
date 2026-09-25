import os

from py_libs.Select import Select

menu_items = ["Create", "Run", "Fresh", "Rollback", "Rollback_step", "Reset", "Exit"]


def migration():
    option = Select.select_fzf_one(menu_items)

    if option == "Create":
        migration_name = input("Migration name like 'create_flights_table': ")
        os.system(
            f"docker compose exec php-fpm php artisan make:migration {migration_name}"
        )
        exit()
    elif option == "Run":
        os.system("docker compose exec php-fpm php artisan migrate")
        exit()
    elif option == "Fresh":
        os.system("docker compose exec php-fpm php artisan migrate:fresh --seed")
        exit()
    elif option == "Rollback":
        os.system("docker compose exec php-fpm php artisan migrate:rollback")
        exit()
    elif option == "Rollback_step":
        step = input("How many steps you want to rollback: ")
        os.system(
            f"docker compose exec php-fpm php artisan migrate:rollback --step={step}"
        )
        exit()
    elif option == "Reset":
        os.system("docker compose exec php-fpm php artisan migrate:reset")
        exit()
    elif option == "Exit":
        exit()
    else:
        exit()
