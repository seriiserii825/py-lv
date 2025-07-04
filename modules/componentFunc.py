import os

from classes.FilesHandle import FilesHandle


def componentFunc():
    create_class = input("Create class? (y/n), by default n: ")
    files_handler = FilesHandle("resources/views/components/")
    result = files_handler.getDir()
    selected_dir = result["selected_dir"]
    dir_path = result["dir_path"]
    if create_class == "y":
        createComponent(True, selected_dir, dir_path)
    else:
        createComponent(False, selected_dir, dir_path)


def createComponent(with_class=False, dir="", dir_path=""):
    if with_class:
        component_name = input("Enter the component name like FormInput: ")
    else:
        component_name = input("Enter the component name like input: ")
    component_name = dir + "." + component_name
    if not component_name:
        print("[red]Component name is required")
        exit()
    if with_class:
        os.system(
            f"docker-compose exec php-fpm php artisan make:component {component_name}"
        )
    else:
        os.system(
            f"docker-compose exec\
            php-fpm php artisan make:component {component_name} --view"
        )
    files_handler = FilesHandle(dir_path)
    files_handler.drawTree(dir_path)
