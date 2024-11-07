import os


def requestFunc():
    print("[green]1. Both")
    print("[blue]2. Store")
    print("[green]3. Update")
    print("[red]4. Exit")

    option = input("Select an option: ")

    if option == '' or option == '4':
        print("[red]Good bye!")
        exit()
    elif option == '1':
        request_name = input("Enter request name like 'Worker': ")
        os.system(f"docker-compose exec php-fpm php artisan make:request {request_name}/StoreRequest")
        os.system(f"docker-compose exec php-fpm php artisan make:request {request_name}/UpdateRequest")
    elif option == 2:
        request_name = input("Enter request name like 'Worker': ")
        os.system(f"docker-compose exec php-fpm php artisan make:request {request_name}/StoreRequest")
    elif option == 3:
        request_name = input("Enter request name like 'Worker': ")
        os.system(f"docker-compose exec php-fpm php artisan make:request {request_name}/UpdateRequest")
    else:
        print("[red]Good bye!")
        exit()
