https://www.docker.com/blog/how-to-dockerize-django-app/

docker build -t hexadrf .

docker compose up --build

docker-compose up -d --build

docker compose run api python manage.py makemigrations

docker compose run api python manage.py migrate

docker compose run api python manage.py createsuperuser
docker compose run api python manage.py create_dev_superuser

### or go docker shell
docker exec -it containerid sh

python manage.py createsuperuser


