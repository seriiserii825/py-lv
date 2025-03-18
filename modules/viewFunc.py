import os
from rich import print

from classes.FilesHandle import FilesHandle
def viewFunc():
    dir_path = 'resources/views'
    dir_path = getCreateChooseDirPath(dir_path)
    first_dir_path = dir_path
    if not os.path.exists(dir_path):
        print("[red]Directory does not exist")
        exit()
    second_level = input("[blue]Do you want to choose or create a file in a sub-directory? (y/n):")
    if second_level == 'y':
        dir_path = getCreateChooseDirPath(dir_path)
        if not os.path.exists(dir_path):
            print("[red]Directory does not exist")
            exit()
    third_level = input("[blue]Do you want to choose or create a file in a sub-directory? (y/n):")
    if third_level == 'y':
        dir_path = getCreateChooseDirPath(dir_path)
        if not os.path.exists(dir_path):
            print("[red]Directory does not exist")
            exit()
    new_file = input("[blue]Enter file name like show(show.blade.php):")
    if new_file == '':
        print("[red]File name is required")
        exit()
    file_path = dir_path + "/" + new_file + ".blade.php"
    if os.path.exists(file_path):
        print("[red]File already exists")
        exit()
    else:
        os.system("touch " + file_path)
        print("[green]File created")
        files_handler = FilesHandle(first_dir_path)
        files_handler.drawTree(first_dir_path)

def getCreateChooseDirPath(dir_path):
    files_handler = FilesHandle(dir_path)
    files_handler.drawTree(dir_path)
    selected_dir = files_handler.createOrChooseDirectory()
    full_path = files_handler.basepath + "/" + selected_dir
    # if full_path has directories inside
    if os.path.isdir(full_path):
        files_handler.drawTree(full_path)
    return full_path
