from flask import Flask, request, render_template
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

@app.route("/first_name", methods =["POST"])
def get_first_name():
    if request.method == "POST":
        first_name = request.form.get("fname")
        f_name_is_lower = first_name.islower()
        is_space_not_available = True if ' ' not in first_name else False
        is_length_less_than_21_char = True if len(first_name) < 21 else False

        if f_name_is_lower and is_space_not_available and is_length_less_than_21_char:
            cursor = mysql.connection.cursor()
            cursor.execute(''' INSERT INTO first_name_table VALUES('{0}')'''.format(first_name))
            mysql.connection.commit()
            cursor.close()
            return render_template('response.html',route_name="first_name",value=first_name, valid=True)
        else :
            return render_template('response.html',route_name="first_name",value=first_name, valid=False)

@app.route("/last_name", methods =["POST"])
def get_last_name():
    if request.method == "POST":
        last_name = request.form.get("lname")
        f_name_is_lower = last_name.islower()
        is_space_not_available = True if ' ' not in last_name else False
        is_length_less_than_21_char = True if len(last_name) < 21 else False

        if f_name_is_lower and is_space_not_available and is_length_less_than_21_char:
            cursor = mysql.connection.cursor()
            cursor.execute(''' INSERT INTO last_name_table VALUES('{0}')'''.format(last_name))
            mysql.connection.commit()
            cursor.close()
            return render_template('response.html',route_name="last_name",value=last_name, valid=True)
        else :
            return render_template('response.html',route_name="last_name",value=last_name, valid=False)


@app.route("/cnic", methods =["POST"])
def get_cnic():
    if request.method == "POST":
        cnic = request.form.get("cnic")
        is_length_less_than_14_char = True if len(cnic) < 14 else False
        clean_cnic_no = ''.join(char for char in cnic if char.isdigit())

        if is_length_less_than_14_char :
            cursor = mysql.connection.cursor()
            cursor.execute(''' INSERT INTO cnic_table VALUES('{0}')'''.format(clean_cnic_no))
            mysql.connection.commit()
            cursor.close()
            return render_template('response.html',route_name="Cnic NO",value=cnic, valid=True)
        else :
            return render_template('response.html',route_name="Cnic NO",value=cnic, valid=False)


@app.route("/date", methods =["POST"])
def get_date_of_birth():
    if request.method == "POST":
        input_date = request.form.get("dob")
        try:
            date_of_birth = datetime.strptime(input_date, '%Y-%m-%d').date()
        except ValueError:
            return render_template('response.html',route_name="Date OF Birth",value=input_date, valid=False)
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO date_of_birth_table VALUES('{0}')'''.format(date_of_birth))
        mysql.connection.commit()
        cursor.close()
        return render_template('response.html',route_name="Date OF Birth",value=date_of_birth, valid=True)

    
@app.route("/province", methods =["POST"])
def get_province():
    if request.method == "POST":
        province = request.form.get("province_input")
    valid_province_list = ["sindh", "punjab", "kpk", "gilgit baltistan"]
    is_valid_province = True if province.lower() in valid_province_list else False

    if is_valid_province :
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO province_table VALUES('{0}')'''.format(province))
        mysql.connection.commit()
        cursor.close()
        return render_template('response.html',route_name="province Name",value=province, valid=True)
    else :
        return render_template('response.html',route_name="province Name",value=province, valid=False)


@app.route("/")
def home_route():
    return render_template('home.html')

