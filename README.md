virtualenv env
source env/bin/activate
pip install -r requirements.txt


run the following command in terminal
export FLASK_APP=app.py
flask run   			//for running flask app


-------------------data base set up--------------------------------
 Create database Flask_task_db;
CREATE USER 'Flask_task_user'@'localhost' IDENTIFIED BY 'Flask@123';
GRANT ALL ON Flask_task_db.* TO 'Flask_task_user'@'localhost';
FLUSH PRIVILEGES;


pip install flask_mysqldb
sudo apt-get install libmysqlclient-dev			// use this cmd only if you get error while running above command.


Flask_task_user
Flask_task_db
Flask@123
root
localhost
