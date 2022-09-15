docker-compose up -d --build

docker-compose down -v

docker container exec -it e92b514a8b30 /bin/bash

docker exec -it e92b514a8b30 psql -U hello_django -W hello_django_dev


---

docker-compose -f docker-compose.prod.yml up -d --build

docker-compose -f docker-compose.prod.yml down -v


https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71