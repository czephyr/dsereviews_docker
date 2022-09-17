# DseReviews

An SSL certified webapp running at the domain [dsereviews.live](https://dsereviews.live), hosted on a remote Ubuntu vm, written in django, using postgres as db, nginx as a reverse-proxy, fully deployable through docker-compose with a single command.  

The platform allows the registration, and confirmation through mail, to unimi students in order to post reviews of the degree courses.

### Docker dev environment deploy

To deploy the containers locally 
        
        docker-compose up -d --build

To stop the containers and delete the volumes

        docker-compose down -v

#### Needed set up

Create an **.env.dev** file in the home folder of the project the content has to be the following env variables:
* _needed by django_

        DEBUG=1 _debug variable to True, will load dev html error pages_ 
        SECRET_KEY=foo _django secret key, not important for dev environment_
        DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] _allowed hosts, has to be set like this for docker networking_
        SQL_ENGINE=django.db.backends.postgresql _db engine of your choice_
        SQL_DATABASE=db_dev _name of the db on the db image_
        SQL_USER=usernamedb _username for the db_
        SQL_PASSWORD=passworddb _password for the db_
        SQL_HOST=db _address of the db service so django knows it's network interface_
        SQL_PORT=5432 _port of the db on the db image_
        DATABASE=postgres _env variable set for the entrypoint.sh to know that the database is postgres_

* _needed for registration confirmation functionality_

        EMAIL_HOST= _email host provider_
        EMAIL_HOST_USER= _email host user_
        EMAIL_HOST_PASSWORD= _email host password_
        EMAIL_PORT= _email host port_
        EMAIL_USE_TLS= _email use tls_

* _needed for django admin functionality_

        ADMIN_USERNAME=admin _django superuser username_
        ADMIN_PASSWORD=admin _django superuser password_
        ADMIN_EMAIL=admin@admin.com _django superuser email_


### Docker production environment deploy

To deploy the production on the nginx proxy 
        
        docker-compose -f docker-compose.prod.yml up -d --build

To stop the containers and delete the volumes

        docker-compose -f docker-compose.prod.yml down -v

#### Needed set up

Create an **.env.prod** file in the home folder of the project:

        DEBUG=0 _debug variable to False, won't load dev html error pages_ 
        SECRET_KEY=yourkey _django secret key, important for production environment_
        DJANGO_ALLOWED_HOSTS=yourdomain.com _allow your domain_
        SQL_ENGINE=django.db.backends.postgresql _db engine of your choice_
        SQL_DATABASE=namedb_prod _name of the db on the db image_
        SQL_USER=usernamedb _username for the db_
        SQL_PASSWORD=passworddb _password for the db_
        SQL_HOST=db _address of the db service so django knows it's network interface_
        SQL_PORT=5432 _port of the db on the db image_
        DATABASE=postgres _env variable set for the entrypoint.sh to know that the database is postgres_

        EMAIL_HOST= _email host provider_
        EMAIL_HOST_USER= _email host user_
        EMAIL_HOST_PASSWORD= _email host password_
        EMAIL_PORT= _email host port_
        EMAIL_USE_TLS= _email use tls_

        ADMIN_USERNAME=username _django superuser username_
        ADMIN_PASSWORD=password _django superuser password_
        ADMIN_EMAIL=email@gmail.com _django superuser email_

Create an **.env.prod.db** file in the home folder of the project:

        POSTGRES_USER=username
        POSTGRES_PASSWORD=password
        POSTGRES_DB=dbname_prod

In order to setup the certbot SSL certificate refer to [this link](https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71) for the procedure.


#### Random useful commands 

        docker container exec -it e92b514a8b30 /bin/bash

        docker exec -it e92b514a8b30 psql -U user -W dbname
