import os

from pyfzf.pyfzf import FzfPrompt

menu_items = ["Create", "Run", "Fresh", "Rollback", "Rollback_step", "Reset", "Exit"]


def migration():
    fzf = FzfPrompt()
    option = fzf.prompt(menu_items)

    if option[0] == "Create":
        migration_name = input("Migration name like 'create_flights_table': ")
        os.system(
            f"docker-compose exec php-fpm php artisan make:migration {migration_name}"
        )
        exit()
    elif option[0] == "Run":
        os.system("docker-compose exec php-fpm php artisan migrate")
        exit()
    elif option[0] == "Fresh":
        os.system("docker-compose exec php-fpm php artisan migrate:fresh --seed")
        exit()
    elif option[0] == "Rollback":
        os.system("docker-compose exec php-fpm php artisan migrate:rollback")
        exit()
    elif option[0] == "Rollback_step":
        step = input("How many steps you want to rollback: ")
        os.system(
            f"docker-compose exec php-fpm php artisan migrate:rollback --step={step}"
        )
        exit()
    elif option[0] == "Reset":
        os.system("docker-compose exec php-fpm php artisan migrate:reset")
        exit()
    elif option[0] == "Exit":
        exit()
    else:
        exit()
