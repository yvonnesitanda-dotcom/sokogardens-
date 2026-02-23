# import flask and its components
from flask import *

# Import the ptmsql module - it helps us create a connection between python flask and mysql database.
import pymysql

# Create a flask application and give it a name
app = Flask(__name__)


# Below is the sign up route
@app.route("/api/signup", methods= ["POST"])
def signup():
    if request.method == "POST":
        # Extract the different details entered on the form
        username = request.form["username"]
        email = request.form ["email"]
        password = request.form ["password"]
        phone = request.form ["phone"]

        
        # By use of the print function lets print all those details sent with the upcoming request
       # print(username, email, password , phone)

       # Establish a connection between flask and mysql
        connection  = pymysql.connect(host="localhost", user="root" , password="", database="sokogardenonline") 

        # Create a cursor to execute the sql queries
        cursor = connection.cursor()

        #Structure an sql to insert the detail received from the firm
        
        #The %S is a placeholder -> It stands in place of actual values i.e we shall replace them later on.

        sql ="INSERT INTO users(username,email,phone,password) VALUES(%s,%s,%s,%s)"

        # Create a tuple that will hold all the data gotten from the form
        data= (username, email, phone, password)

        # By use of the cursor , execute the sql as you replace the placeholders with actual values 
        cursor.execute(sql, data)

        # Commit the changes to the database
        connection.commit()

    return jsonify({"message":"User registered successfully"})


# Below is the login/sign in route
@app.route("/api/signin", methods=["POST"])
def signin():
    if request.method == "POST" :
        # Extract the two details on the form
        email= request.form ["email"]
        password = request.form ["password"]

        #Print out the details entered
       # print(email, password)

       # Create/ establish a connection to the database
       
    connection = pymysql . connect (host="localhost", user= "root", password="" , database ="sokogardenonline")

    # Create a cursor
    cursor= connection.cursor(pymysql.cursors.DictCursor)

    #Structure an sql to insert the detail received from the firm
    sql ="SELECT * FROM users WHERE email = %s AND password =%s"

    # put the data received from the form into a tuple
    data = (email, password)

    # by use of the cursor execute sql
    cursor. execute (sql,data)

    #Check whether there are rows returned and store thm on a variable
    count = cursor. rowcount 
    # print (count)


    # if there are records returned it means the password and the email are correct , other wise it means they are wrong
    if count== 0 :
        return jsonify ({"message":"Log in failed"})
    
    else:
        #There must be a user so we create a variable that will hold the detils of the user fetched from the database
        user = cursor.fetchone()
        # Return the details to the frontend as well as a message
        return jsonify ({"message": "User logged in successfully", "user": user})

    



# Run the application
app.run(debug= True)