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
    terminal_menu = TerminalMenu(menu_items)
    menu_entry_index = terminal_menu.show()
    if menu_entry_index is None:
        exit()

    if menu_entry_index == 0:
        print("[blue]Routes")
        os.system("docker-compose exec php-fpm php artisan route:list")
        menu()
    elif menu_entry_index == 1:
        print("[blue]Component")
        componentFunc()
        menu()
    elif menu_entry_index == 2:
        print("[blue]Views")
        viewFunc()
        menu()
    elif menu_entry_index == 3:
        print("[blue]Trait")
        newTrait()
        menu()
    elif menu_entry_index == 4:
        print("[blue]Composer")
        composer()
        menu()
    elif menu_entry_index == 5:
        print("[blue]Migration")
        migration()
        menu()
    elif menu_entry_index == 6:
        print("[blue]Model")
        model()
        menu()
    elif menu_entry_index == 7:
        print("[blue]Controller")
        controller()
        menu()
    elif menu_entry_index == 8:
        print("[blue]Request")
        requestFunc()
        menu()
    elif menu_entry_index == 9:
        print("[blue]Resource")
        resourceFunc()
        menu()
    elif menu_entry_index == 10:
        print("[blue]Middleware")
        middlewareFunc()
        menu()
    elif menu_entry_index == 11:
        print("[blue]Artisan")
        artisan()
        menu()
    elif menu_entry_index == 12:
        print("[blue]Key Generate")
        os.system(f"docker-compose exec php-fpm php artisan key:generate")
        menu()
    elif menu_entry_index == 13:
        print("[blue]Docker")
        dockerFunc()
        menu()
    elif menu_entry_index == 14:
        print("[blue]Clear")
        os.system("docker-compose exec php-fpm php artisan view:clear && docker-compose exec php-fpm php artisan cache:clear && docker-compose exec php-fpm php artisan config:clear && docker-compose exec php-fpm php artisan route:clear && docker-compose exec php-fpm php artisan php artisan optimize:clear")
        menu()
    elif menu_entry_index == 15:
        print("[red]Good bye!")
        exit()
if __name__ == "__main__":
    menu()
