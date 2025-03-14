import os

from classes.FilesHandle import FilesHandle
def componentFunc():
    create_class = input("Create class? (y/n), by default n: ")
    showDirPath()
    if create_class == "y":
        createComponent(True)
    else:
        createComponent()

def createComponent(with_class = False):
    if with_class:
        component_name = input("Enter the component name like FormInput: ")
    else:
        component_name = input("Enter the component name like form.input: ")
    if not component_name:
        print("[red]Component name is required")
        exit()
    if with_class:
        command = os.system(f"docker-compose exec php-fpm php artisan make:component {component_name}")
    else:
        command = os.system(f"docker-compose exec php-fpm php artisan make:component {component_name} --view")
    print(command)

def showDirPath():
    dir_path = 'resources/views/components/'
    files_handler = FilesHandle(dir_path)
    # files_handler.listDir()
    selected_dir = files_handler.createOrChooseDirectory()
    dir_path = files_handler.basepath + "/" + selected_dir
    print(f"dir_path: {dir_path}")
    if not os.path.exists(dir_path):
        print("[red]Directory does not exist")
        exit()
    files_handler.listFiles(dir_path)
    return dir_path
