import os


def controller():
    print("[green]1. Simple")
    print("[blue]2. Resource")
    print("[green]3. Api")
    print("[red]4. Exit")

    option = input("Select an option: ")
    if option == '' or option == '4':
        print("[red]Good bye!")
        exit()
    elif option == '1':
        controller_name = input("Controller name like 'FlightController': ")
        os.system(f"docker-compose exec php-fpm php artisan make:controller {controller_name}")
    elif option == '2':
        controller_name = input("Controller name like 'FlightController': ")
        os.system(f"docker-compose exec php-fpm php artisan make:controller {controller_name} --resource")
    elif option == '3':
        controller_name = input("Controller name like 'FlightController': ")
        os.system(f"docker-compose exec php-fpm php artisan make:controller {controller_name} --api")
    else:
        exit()

