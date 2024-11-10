import os

def middlewareFunc():
    middleware_name = input("Middleware name like 'CheckAgeMiddleware': ")
    os.system("docker-compose exec php-fpm php artisan make:middleware " + middleware_name)
    return True

