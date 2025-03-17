import os

from modules.artisan import artisan
from modules.componentFunc import componentFunc
from modules.composer import composer
from modules.controller import controller
from modules.dockerFunc import dockerFunc
from modules.middlewareFunc import middlewareFunc
from modules.migration import migration
from modules.model import model
from modules.newTrait import newTrait
from modules.request import requestFunc
from modules.resourceFunc import resourceFunc
from rich import print
from pyfzf.pyfzf import FzfPrompt

from modules.viewFunc import viewFunc

## check for laravel project
if not os.path.exists("artisan"):
    print("[red]This is not a laravel project")
    exit()
    
menu_items = [
    "Routes",
    "Component",
    "Views",
    "Trait",
    "Composer",
    "Migration",
    "Model",
    "Controller",
    "Request",
    "Resource",
    "Middleware",
    "Artisan",
    "Key Generate",
    "Docker",
    "Clear",
    "Exit"
]

def menu():
    fzf = FzfPrompt()
    selected_item = fzf.prompt(menu_items)
    if not selected_item:
        print("[red]Good bye!")
        exit()

    if selected_item[0] == "Component":
        componentFunc()
        menu()
    elif selected_item[0] == "Routes":
        os.system("docker-compose exec php-fpm php artisan route:list")
        menu()
    elif selected_item[0] == "Views":
        viewFunc()
        menu()
    elif selected_item[0] == "Composer":
        composer()
        menu()
    elif selected_item[0] == "Migration":
        migration()
        menu()
    elif selected_item[0] == "Model":
        model()
        menu()
    elif selected_item[0] == "Controller":
        controller()
        menu()
    elif selected_item[0] == "Request":
        requestFunc()
        menu()
    elif selected_item[0] == "Resource":
        resourceFunc()
        menu()
    elif selected_item[0] == "Middleware":
        middlewareFunc()
        menu()
    elif selected_item[0] == "Artisan":
        artisan()
        menu()
    elif selected_item[0] == "Key Generate":
        os.system(f"docker-compose exec php-fpm php artisan key:generate")
        menu()
    elif selected_item[0] == "Trait":
        newTrait()
        menu()
    elif selected_item[0] == "Docker":
        dockerFunc()
        menu()
    elif selected_item[0] == "Clear":
        os.system("docker-compose exec php-fpm php artisan view:clear && docker-compose exec php-fpm php artisan cache:clear && docker-compose exec php-fpm php artisan config:clear && docker-compose exec php-fpm php artisan route:clear && docker-compose exec php-fpm php artisan php artisan optimize:clear")
        menu()
    elif selected_item[0] == "Exit":
        print("[red]Good bye!")
        exit()
if __name__ == "__main__":
    menu()
