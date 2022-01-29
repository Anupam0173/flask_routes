from flask import Flask
from flask_mysqldb import MySQL
from datetime import datetime

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
    cursor.execute(''' CREATE TABLE IF NOT EXISTS cnic_table (cnic_no  varchar(20)); ''')
    cursor.execute(''' CREATE TABLE IF NOT EXISTS date_of_birth_table (date_of_birth  Date); ''')
    cursor.execute(''' CREATE TABLE IF NOT EXISTS province_table (province  varchar(30)); ''')

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

@app.route("/cnic/<string:cnic>")
def get_cnic(cnic):
    is_length_less_than_14_char = True if len(cnic) < 14 else False
    clean_cnic_no = ''.join(char for char in cnic if char.isdigit())

    if is_length_less_than_14_char :
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO cnic_table VALUES('{0}')'''.format(clean_cnic_no))
        mysql.connection.commit()
        cursor.close()
        return f"your cnic has been saved in database : {cnic}</p>"
    else :
        return f"your cnic no is not valid: {cnic}</p>"

@app.route("/date/<string:date_of_birth>")
def get_date_of_birth(date_of_birth):
    try:
        input_date = datetime.strptime(date_of_birth, '%Y-%m-%d').date()
    except ValueError:
        return f"<p>Invalid date : {date_of_birth}</p>"
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO date_of_birth_table VALUES('{0}')'''.format(date_of_birth))
    mysql.connection.commit()
    cursor.close()
    return f"<p>saving date into db : {input_date}</p>"
    
@app.route("/province/<string:province>")
def get_province(province):
    valid_province_list = ["sindh", "punjab", "kpk", "gilgit baltistan"]
    is_valid_province = True if province.lower() in valid_province_list else False

    if is_valid_province :
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO province_table VALUES('{0}')'''.format(province))
        mysql.connection.commit()
        cursor.close()
        return f"your province has been saved in database : {province}</p>"
    else :
        return f"province is not valid: {province}</p>"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

