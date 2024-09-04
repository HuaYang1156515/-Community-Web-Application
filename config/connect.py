import mysql.connector
from mysql.connector import Error

# Database connection details
dbuser = "root"   
dbpass = "abcd1234"   
dbhost = "localhost" 
dbport = "3306"
dbname = "community_event_planner"



db_config = {
    'user': 'HuaYang',                   # MySQL username
    'password': 'abcd1234',              # MySQL password
    'host': 'HuaYang.mysql.pythonanywhere-services.com', # MySQL host
    'database': 'community_event_planner',    # MySQL database name
    'port': 3306                         # MySQL port, if needed
}

try:
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        print("Connected to the database")
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
