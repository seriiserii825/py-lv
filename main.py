import os

from py_libs.Select import Select
from rich import print

from modules.artisan import artisan
from modules.componentFunc import componentFunc
from modules.composer import composer
from modules.controller import controller
from modules.dockerFunc import dockerFunc
from modules.factory import factory
from modules.middlewareFunc import middlewareFunc
from modules.migration import migration
from modules.model import model
from modules.newTrait import newTrait
from modules.nodeFunc import nodeFunc
from modules.request import requestFunc
from modules.resourceFunc import resourceFunc
from modules.seeder import seeeder
from modules.service import service
from modules.viewFunc import viewFunc

# check for laravel project
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
    "Factory",
    "Key Generate",
    "Middleware",
    "Migration",
    "Model",
    "Request",
    "Resource",
    "Routes",
    "Seeder",
    "Service",
    "Trait",
    "Views",
    "Node",
]


def menu():
    menu_entry = Select.select_fzf_one(menu_items)

    if menu_entry == "Artisan":
        print("[blue]Artisan")
        artisan()
    elif menu_entry == "Clear":
        print("[blue]Clear")
        os.system(
            "docker compose exec php-fpm php artisan view:clear \
                    && docker compose exec php-fpm php artisan cache:clear \
                    && docker compose exec php-fpm php artisan config:clear \
                    && docker compose exec php-fpm php artisan route:clear \
                    && docker compose exec php-fpm php artisan optimize:clear"
        )
    elif menu_entry == "Component":
        print("[blue]Component")
        componentFunc()
    elif menu_entry == "Composer":
        print("[blue]Composer")
        composer()
    elif menu_entry == "Controller":
        print("[blue]Controller")
        controller()
    elif menu_entry == "Factory":
        print("[blue]Factory")
        factory()
    elif menu_entry == "Routes":
        print("[blue]Routes")
        os.system("docker compose exec php-fpm php artisan route:list")
    elif menu_entry == "Views":
        print("[blue]Views")
        viewFunc()
    elif menu_entry == "Trait":
        print("[blue]Trait")
        newTrait()
    elif menu_entry == "Migration":
        print("[blue]Migration")
        migration()
    elif menu_entry == "Seeder":
        print("[blue]Seeder")
        seeeder()
    elif menu_entry == "Service":
        print("[blue]Service")
        service()
    elif menu_entry == "Model":
        print("[blue]Model")
        model()
    elif menu_entry == "Request":
        print("[blue]Request")
        requestFunc()
    elif menu_entry == "Resource":
        print("[blue]Resource")
        resourceFunc()
    elif menu_entry == "Middleware":
        print("[blue]Middleware")
        middlewareFunc()
    elif menu_entry == "Key Generate":
        print("[blue]Key Generate")
        os.system(f"docker compose exec php-fpm php artisan key:generate")
    elif menu_entry == "Docker":
        print("[blue]Docker")
        dockerFunc()
    elif menu_entry == "Node":
        print("[blue]Node")
        nodeFunc()
    elif menu_entry == "Exit":
        print("[red]Good bye!")
        exit()


if __name__ == "__main__":
    menu()
