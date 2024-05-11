import mysql.connector

try:
    # Establish a connection to the MySQL server
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Replace 'your_password' with the actual password
        database="asd"  # Optionally, specify the database you want to connect to
    )

    # If connection is successful, print a success message
    print("Connected to MySQL database!")

    # Close the connection
    conn.close()

except mysql.connector.Error as e:
    # If connection fails, print the error message
    print(f"Error connecting to MySQL database: {e}")
