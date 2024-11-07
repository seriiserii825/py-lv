from rich import print

def middlewareFunc():
    print("[blue]Middleware function")
    middleware_name = input("Middleware name like 'CheckAgeMiddleware': ")
    print("docker-compose exec php-fpm php artisan make:middleware " + middleware_name)
    return True

