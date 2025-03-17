import os
from rich import print

from classes.FilesHandle import FilesHandle
def viewFunc():
    dir_path = 'resources/views'
    files_handler = FilesHandle(dir_path)
    files_handler.listDir()
    selected_dir = files_handler.createOrChooseDirectory()
    dir_path = files_handler.basepath + "/" + selected_dir
    print(f"dir_path: {dir_path}")
    if not os.path.exists(dir_path):
        print("[red]Directory does not exist")
        exit()
    second_level = input("[blue]Do you want to create a file in a sub-directory? (y/n):")
    if second_level == 'y':
        files_handler.listDir(dir_path)
        selected_dir = files_handler.createOrChooseDirectory()
        dir_path = dir_path + "/" + selected_dir
        print(f"dir_path: {dir_path}")
        if not os.path.exists(dir_path):
            print("[red]Directory does not exist")
            exit()
    files_handler.listFiles(dir_path)
    print("")
    new_file = input("[blue]Enter file name like show(show.blade.php):")
    if new_file == '':
        print("[red]File name is required")
        exit()
    file_path = dir_path + "/" + new_file + ".blade.php"
    files_handler.createFile(file_path)
    files_handler.listFiles(dir_path)
