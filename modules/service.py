import os
from classes.FilesHandle import FilesHandle
from pyfzf.pyfzf import FzfPrompt
fzf = FzfPrompt()

def service():
    service_path = "app/Services"
    if not os.path.exists(service_path):
        os.makedirs(service_path)
    files_handle = FilesHandle(service_path)
    selected_dir = files_handle.createOrChooseDirectory()
    selected_dir = os.path.join(service_path, selected_dir)
    files_handle.listFiles(selected_dir)
    file_name = files_handle.addFileName(selected_dir, 'Home, will be HomeService')
    class_name = f"{file_name}Service"
    file_path = os.path.join(selected_dir, class_name + ".php")
    files_handle.createFile(file_path)
    print(f"file_path: {file_path}")
    files_handle.listFiles(selected_dir)
    namespace = files_handle.filePathToNamespace(file_path)
    layout_code = f"""
<?php
{namespace}

class {class_name} {{

}}
    """
    files_handle.appendToFile(file_path, layout_code)
