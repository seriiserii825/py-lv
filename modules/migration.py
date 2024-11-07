import os
from rich import print


def migration():
    print("[green]1. Creat_migration")
    print("[green]2. Create_migration_with_table")
    print("[blue]3. Run_migration")
    print("[green]4. Create_seeder")
    print("[blue]5. Seed")
    print("[green]6. Create_factory")
    print("[blue]7. Fresh_seed")
    print("[blue]7.1. Fresh(drop tables and re-run all migrations)")
    print("[blue]8. Rollback")
    print("[blue]9. Rollback_step")
    print("[red]10. Reset")
    print("[blue]11. Clear")
    print("[yellow]12. Back")
    print("[red]13. Exit")
    
    option = input("Select an option: ")
    if option == '':
        print("[red]Good bye!")
        exit()
    elif option == '1':
        migration_name = input("Migration name like 'create_flights_table': ")
        os.system(f"docker-compose exec php-fpm php artisan make:migration {migration_name}")
        migration()
    elif option == '2':
        migration_name = input("Migration name like 'create_flights_table': ")
        table_name = input("Table name like 'flights': ")
        os.system(f"docker-compose exec php-fpm php artisan make:migration {migration_name} --table={table_name}")
        migration()
    elif option == '3':
        os.system("docker-compose exec php-fpm php artisan migrate")
        migration()
    elif option == '4':
        seeder_name = input("Seeder name like 'FlightsTableSeeder': ")
        os.system(f"docker-compose exec php-fpm php artisan make:seeder {seeder_name}")
        migration()
    elif option == '5':
        os.system("docker-compose exec php-fpm php artisan db:seed")
        migration()
    elif option == '6':
        factory_name = input("Factory name like 'FlightsFactory': ")
        os.system(f"docker-compose exec php-fpm php artisan make:factory {factory_name}")
        migration()
    elif option == '7':
        os.system("docker-compose exec php-fpm php artisan migrate:fresh --seed")
        migration()
    elif option == '7.1':
        os.system("docker-compose exec php-fpm php artisan migrate:fresh")
        migration()
    elif option == '8':
        os.system("docker-compose exec php-fpm php artisan migrate:rollback")
        migration()
    elif option == '9':
        step = input("How many steps you want to rollback: ")
        os.system(f"docker-compose exec php-fpm php artisan migrate:rollback --step={step}")
        migration()
    elif option == '10':
        os.system("docker-compose exec php-fpm php artisan migrate:reset")
        migration()
    elif option == '11':
        os.system("docker-compose exec php-fpm php artisan view:clear && docker-compose exec php-fpm php artisan cache:clear && docker-compose exec php-fpm php artisan config:cache && docker-compose exec php-fpm php artisan route:clear")
        migration()
    elif option == '12':
        return True
    elif option == '13':
        print("[red]Good bye!")
        exit()
    else:
        print("[red]Invalid option")
        migration()
