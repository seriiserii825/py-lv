import os
from rich import print


def requestFunc():
    print("[green]1. Both")
    print("[blue]2. Store")
    print("[green]3. Update")
    print("[yellow]4. Back")
    print("[red]5. Exit")

    option = input("Select an option: ")

    if option == '1':
        request_name = input("Enter request name like 'Worker': ")
        os.system(f"docker-compose exec php-fpm php artisan make:request {request_name}/StoreRequest")
        os.system(f"docker-compose exec php-fpm php artisan make:request {request_name}/UpdateRequest")
    elif option == '2':
        request_name = input("Enter request name like 'Worker': ")
        os.system(f"docker-compose exec php-fpm php artisan make:request {request_name}/StoreRequest")
    elif option == '2':
        request_name = input("Enter request name like 'Worker': ")
        os.system(f"docker-compose exec php-fpm php artisan make:request {request_name}/UpdateRequest")
    elif option == '2':
        return True
    elif option == '2':
        print("[red]Good bye!")
        exit()
    else:
        print("[red]Invalid option")
        requestFunc()
