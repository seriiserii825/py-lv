import os
from rich import print

def dockerFunc():
    print("[green]1. List containers")
    print("[red]2. Remove container")
    print("[green]3. List images")
    print("[red]4. Remove image")
    print("[red]6. Exit")

    option = input("Select an option: ")

    if option == '1':
        os.system("docker-compose ps")
        dockerFunc()
    elif option == '2':
        container = input("Enter container name: ")
        os.system(f"docker-compose stop {container}")
        os.system(f"docker-compose rm -f {container}")
        os.system(f"docker-compose build {container}")
        os.system(f"docker-compose up -d {container}")
        dockerFunc()
    elif option == '3':
        os.system("docker images")
        dockerFunc()
    elif option == '4':
        image = input("Enter image name: ")
        os.system(f"docker rmi {image}")
        dockerFunc()
    elif option == '6':
        print("[red]Good bye!")
        exit()
    else:
        print("[red]Invalid option")
        dockerFunc()

