# how to start

1. create venv
`python3 -m venv venv`
2. activate venv for mac `source venv/bin/activate`. for win `venv/bin/activate.bat`
3. install all requirements `pip3 install -r requirements.txt`

# how to run server
`cd littlelemon`

`python manage.py runserver`


# APIs
allowed IsAuthenticated Users
`http://127.0.0.1:8000/restaurant/menu-items` - get all menu-items 
`http://127.0.0.1:8000/restaurant/booking/tables/` - get/put/post - for book table