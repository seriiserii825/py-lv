import os
from classes.FilesHandle import FilesHandle
# import pyperclip
# import subprocess
from pyfzf.pyfzf import FzfPrompt
fzf = FzfPrompt()

def service():
    service_path = "app/Services"
    files_handle = FilesHandle(service_path)
    selected_dir = files_handle.createOrChooseDirectory()
    selected_dir = os.path.join(service_path, selected_dir)
    files_handle.listFiles(selected_dir)
    file_object = files_handle.addFileName(selected_dir, 'HomeService')
    print(f"file_object: {file_object}")
    file_path = file_object['file_path']
    class_name = file_object['file_name']
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
