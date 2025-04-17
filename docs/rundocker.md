https://www.docker.com/blog/how-to-dockerize-django-app/

docker build -t hexadrf .

docker compose up --build

docker-compose up -d --build

docker compose run api python manage.py makemigrations

docker compose run api python manage.py migrate

docker compose run api python manage.py createsuperuser

### or go docker shell
docker exec -it containerid bash

python manage.py createsuperuser
