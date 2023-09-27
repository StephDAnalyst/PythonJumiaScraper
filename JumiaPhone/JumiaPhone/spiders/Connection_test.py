import mysql.connector

# Database connection parameters
db_config = {
    'host':'hostname',
    'user':'your_username',
    'password':'your_password',
    'database':'your_database_name'
            }

try:
    # Attempt to connect to the database
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        print('Connected to MySQL database')
        # Add your further database operations here
        # ...

except mysql.connector.Error as err:
    print('Failed to connect to MySQL database:', err)

finally:
    # Close the database connection
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print('Database connection closed')
