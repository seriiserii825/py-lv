import os
from simple_term_menu import TerminalMenu
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
    "Artisan",
    "Clear",
    "Component",
    "Composer",
    "Controller",
    "Docker",
    "Exit",
    "Key Generate",
    "Middleware",
    "Migration",
    "Model",
    "Request",
    "Resource",
    "Routes",
    "Trait",
    "Views",
]


def menu():
    fzf = FzfPrompt()
    menu_entry = fzf.prompt(menu_items)

    if menu_entry[0] == "Artisan":
        print("[blue]Artisan")
        artisan()
        menu()
    elif menu_entry[0] == "Clear":
        print("[blue]Clear")
        os.system("docker-compose exec php-fpm php artisan view:clear && docker-compose exec php-fpm php artisan cache:clear && docker-compose exec php-fpm php artisan config:clear && docker-compose exec php-fpm php artisan route:clear && docker-compose exec php-fpm php artisan php artisan optimize:clear")
        menu()
    elif menu_entry[0] == "Component":
        print("[blue]Component")
        componentFunc()
        menu()
    elif menu_entry[0] == "Composer":
        print("[blue]Composer")
        composer()
        menu()
    elif menu_entry[0] == "Controller":
        print("[blue]Controller")
        controller()
        menu()
    elif menu_entry[0] == "Routes":
        print("[blue]Routes")
        os.system("docker-compose exec php-fpm php artisan route:list")
        menu()
    elif menu_entry[0] == "Views":
        print("[blue]Views")
        viewFunc()
    elif menu_entry[0] == "Trait":
        print("[blue]Trait")
        newTrait()
        menu()
    elif menu_entry[0] == "Migration":
        print("[blue]Migration")
        migration()
        menu()
    elif menu_entry[0] == "Model":
        print("[blue]Model")
        model()
        menu()
    elif menu_entry[0] == "Request":
        print("[blue]Request")
        requestFunc()
        menu()
    elif menu_entry[0] == "Resource":
        print("[blue]Resource")
        resourceFunc()
        menu()
    elif menu_entry[0] == "Middleware":
        print("[blue]Middleware")
        middlewareFunc()
        menu()
    elif menu_entry[0] == "Key Generate":
        print("[blue]Key Generate")
        os.system(f"docker-compose exec php-fpm php artisan key:generate")
        menu()
    elif menu_entry[0] == "Docker":
        print("[blue]Docker")
        dockerFunc()
        menu()
    elif menu_entry[0] == "Exit":
        print("[red]Good bye!")
        exit()
if __name__ == "__main__":
    menu()
