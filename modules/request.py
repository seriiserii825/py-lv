import os

from rich import print

from classes.FilesHandle import FilesHandle


def getName():
    name = input("Enter name like 'Worker, will be Worker': ")
    if name == "":
        print("[red]Name cannot be empty")
        getName()
    print(f"name: {name}")
    return name


def requestFunc():
    dir_path = "app/Http/Requests"
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_handler = FilesHandle("app/Http/Requests")
    result = file_handler.getDir()
    selected_dir = result["selected_dir"]
    dir_path = f"app/Http/Requests/{selected_dir}"

    file_handler.listFiles(dir_path)

    request_name = getName()
    store_name = f"{selected_dir}/{request_name}Request"
    print(f"store_name: {store_name}")
    update_name = f"{selected_dir}/{request_name}UpdateRequest"
    print(f"update_name: {update_name}")

    print("[green]1. Both")
    print("[blue]2. Store")
    print("[green]3. Update")
    print("[yellow]4. Back")
    print("[red]5. Exit")

    option = input("Select an option: ")

    if option == "1":
        os.system(f"docker-compose exec php-fpm php artisan make:request {store_name}")
        os.system(f"docker-compose exec php-fpm php artisan make:request {update_name}")
    elif option == "2":
        os.system(f"docker-compose exec php-fpm php artisan make:request {store_name}")
    elif option == "3":
        os.system(f"docker-compose exec php-fpm php artisan make:request {update_name}")
    elif option == "4":
        return True
    elif option == "5":
        print("[red]Good bye!")
        exit()
    else:
        print("[red]Invalid option")
        requestFunc()
