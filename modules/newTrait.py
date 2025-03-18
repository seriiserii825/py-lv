import os
from classes.FilesHandle import FilesHandle


def newTrait():
    dir_path = 'app/Traits'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    files_handler = FilesHandle(dir_path)
    files_handler.drawTree(dir_path)
    print("============================================")
    new_file = input("[blue]Enter file name like show(Trait):")
    if new_file == '':
        print("[red]File name is required")
        exit()
    file_path = dir_path + "/" + new_file + ".php"
    files_handler.createFile(file_path)
    trait_content = '''<?php
    namespace App\\Traits;
    
    trait ''' + new_file + ''' 
    {
    
    }
    '''

    files_handler.appendToFile(file_path, trait_content);
    print("[green]Trait created successfully")
    files_handler.drawTree(dir_path)
