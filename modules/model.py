import os


def model():
    print("[green]1. Create_model")
    print("[blue]2. Model_migration")
    print("[green]3. Model_factory")
    print("[blue]4. Model_factory_migration")
    print("[green]5. Model_factory_migrationSeeder")
    print("[blue]6. Model_migration_controller_resource")
    print("[green]7. Model_migration_factory_controller_resource")
    print("[red]8. Exit")

    option = input("Select an option: ")
    if option == '' or option == '8':
        print("[red]Good bye!")
        exit()
    elif option == '1':
        model_name = input("Model name like 'Flight': ")
        os.system(f"docker-compose exec php-fpm php artisan make:model {model_name}")
    elif option == '2':
        model_name = input("Model name like 'Flight': ")
        os.system(f"docker-compose exec php-fpm php artisan make:model {model_name} -m")
    elif option == '3':
        model_name = input("Model name like 'Flight': ")
        os.system(f"docker-compose exec php-fpm php artisan make:model {model_name} -f")
    elif option == '4':
        model_name = input("Model name like 'Flight': ")
        os.system(f"docker-compose exec php-fpm php artisan make:model {model_name} -mf")
    elif option == '5':
        model_name = input("Model name like 'Flight': ")
        os.system(f"docker-compose exec php-fpm php artisan make:model {model_name} -mfs")
    elif option == '6':
        model_name = input("Model name like 'Flight': ")
        os.system(f"docker-compose exec php-fpm php artisan make:model {model_name} -mcr")
    elif option == '7':
        model_name = input("Model name like 'Flight': ")
        os.system(f"docker-compose exec php-fpm php artisan make:model {model_name} -mfcr")
    else:
        exit()
