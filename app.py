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








# Run the application
app.run(debug= True)