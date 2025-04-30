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
    files_handle.addFileName(selected_dir, 'HomeService')
    files_handle.listFiles(selected_dir)

    #  # Use `find` command to list all files
    # result = subprocess.run(
    #     ## exclude directory vendor
    #     # ["find", ".",  "-name",  "*Service*", "-type", "f"],
    #     ["find", ".",  "-name",  "*Service*", "-type", "f", "-not", "-path", "./vendor/*"],
    #     stdout=subprocess.PIPE,
    #     stderr=subprocess.DEVNULL,
    #     text=True
    # )
    #
    # # Split the output into a list of file paths
    # file_list = result.stdout.strip().split('\n')
    #
    # # Prompt the user to select a file using fzf
    # selected = fzf.prompt(file_list)
    #
    # if selected:
    #     file_path = selected[0]
    #     print(f"Selected file: {file_path}")
    #     # split in to array file path
    #     file_path = file_path.split("/")
    #     new_file_path = file_path[2::]
    #     # remove last element
    #     new_file_path = new_file_path[:-1]
    #     # join the array with \
    #     new_file_path = "\\".join(new_file_path)
    #     new_file_path = f"namespace App\\{new_file_path};"
    #     # Copy to clipboard
    #     pyperclip.copy(new_file_path.strip())
    #     
    #     subprocess.run(['notify-send', new_file_path], check=True)
    # else:
    #     print("No file selected.")
    #     return None

