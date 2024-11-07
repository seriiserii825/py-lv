import os


def resourceFunc():
    print("Enter resource name like 'Worker, will be WorkerResource'")
    resource_name = input("Enter resource name: ")
    os.system(f"docker-compose exec php-fpm php artisan make:resource {resource_name}Resource")
    print("[green]Resource created successfully!")
    return
