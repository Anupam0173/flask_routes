from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

#mysal db connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'Flask_task_user'
app.config['MYSQL_PASSWORD'] = 'Flask@123'
app.config['MYSQL_DB'] = 'Flask_task_db'
 
mysql = MySQL(app)

with app.app_context():
    #Creating a connection cursor
    cursor = mysql.connection.cursor()
    
    #Executing SQL Statements
    cursor.execute(''' CREATE TABLE IF NOT EXISTS first_name_table (f_name  varchar(20)); ''')
    cursor.execute(''' CREATE TABLE IF NOT EXISTS last_name_table (l_name  varchar(20)); ''')
    
    #Saving the Actions performed on the DB
    mysql.connection.commit()
    
    #Closing the cursor
    cursor.close()

@app.route("/first_name/<string:first_name>")
def get_first_name(first_name):
    f_name_is_lower = first_name.islower()
    is_space_not_available = True if ' ' not in first_name else False
    is_length_less_than_21_char = True if len(first_name) < 21 else False

    if f_name_is_lower and is_space_not_available and is_length_less_than_21_char:
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO first_name_table VALUES('{0}')'''.format(first_name))
        mysql.connection.commit()
        cursor.close()
        return f"your fist_Name has been saved in database : {first_name}</p>"
    else :
        return f"fist_name is not valid: {first_name}</p>"

@app.route("/last_name/<string:last_name>")
def get_last_name(last_name):
    f_name_is_lower = last_name.islower()
    is_space_not_available = True if ' ' not in last_name else False
    is_length_less_than_21_char = True if len(last_name) < 21 else False

    if f_name_is_lower and is_space_not_available and is_length_less_than_21_char:
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO last_name_table VALUES('{0}')'''.format(last_name))
        mysql.connection.commit()
        cursor.close()
        return f"your last_Name has been saved in database : {last_name}</p>"
    else :
        return f"last_name is not valid: {last_name}</p>"


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
