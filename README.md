The project runs on pip environment.

therefore, clone the project and install pipenv virtual environment
install django, djangorestframework,djoser

MYSQL Connection is setup using pymysql as i am having Apple ARM chip and getting errors for the mysql client. therefore you might need to install pymysql client to work the database connection properly. Thank you for your patience.

These are the configurations that specifically changed for the MYSQL connection

1. open pipfile once you setup and activate your pipenv(as i was using pipenv)
2. replace mysqlclient="*" with pymysql="*"
3. Open __init__.py and add following,
    import pymysql;
    pymysql.install_as_MySQLdb()
4. Then in the terminal install pymysql by using 
    pipenv install pymysql



The API endpoints are.

to register a new user POST: http://localhost:8000/auth/users/
Generate Token for the registered user POST: http://127.0.0.1:8000/auth/token/login/

 Menu Items

Inseart a Menu Item POST : http://127.0.0.1:8000/restaurant/menu/
Retrieve the menu items GET : http://127.0.0.1:8000/restaurant/menu/
Edit a Menu ITEM PATCH : http://127.0.0.1:8000/restaurant/menu/<id>
Edit a Menu ITEM PUT : http://127.0.0.1:8000/restaurant/menu/<id>
Delete a Menu Item DELETE : http://127.0.0.1:8000/restaurant/menu/<id>


   Bookings
Booking a Table POST : http://127.0.0.1:8000/restaurant/booking/tables/

with following parameters , name=<name of the customer>
                            no_of_guests=<Number of Guests>
                            booking_date=<YYYY-MM-DD HH> formate Ex->2025-05-10 15

check the Booking Details GET : http://127.0.0.1:8000/restaurant/booking/tables/<Booking id>/
To Edit a Booking Partially PATCH: http://127.0.0.1:8000/restaurant/booking/tables/<Booking id>/
To Edit a Booking Fully PUT:                  http://127.0.0.1:8000/restaurant/booking/tables/<Booking id>/
Delete a Booking DELETE  :
 http://127.0.0.1:8000/restaurant/booking/tables/<Booking id>/



