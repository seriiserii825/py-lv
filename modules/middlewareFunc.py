import os

def middlewareFunc():
    middleware_name = input("Middleware name like 'CheckAge', will be 'CheckAgeMiddleware': ")
    name = middleware_name + "Middleware"
    os.system("docker-compose exec php-fpm php artisan make:middleware " + name)
    return True

