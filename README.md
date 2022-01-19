# smartbear-anguphy-api

Please follow the steps below:

1. python -m venv venv 

2. source venv/bin/activate

3. pip install -r smartbear-anguphy/requirements.txt

4. create database anguphydb with credentials user: angyphy, password: password

5. cd smartbear-anguphy

6. python manage.py migrate

7. python manage.py runserver

# Start Commands for docker-compose file
Builds, (re)creates, starts, and attaches to containers for a service.  
`docker-compose up`