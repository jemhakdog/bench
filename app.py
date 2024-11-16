from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Define your MySQL connection
mydb = mysql.connector.connect(
    host="Jemcarlo.mysql.pythonanywhere-services.com",
    user="Jemcarlo",
    password="admin*1234",
    database='Jemcarlo$default'
)

# Create a cursor object to execute SQL queries
cursor = mydb.cursor()

# Define your routes and functions
@app.route('/')
def home():
    # Your home route logic here
    return 'Hello, Jem!'

@app.route('/execute_command/<command>', methods=['get'])
def execute_command(command):
    # Get command from request
    #command = request.form.get('command')

    # Execute the command
    cursor.execute(command)
    mydb.commit()

    # Return a response
    return 'Command executed successfully.'

@app.route('/view_tables')
def view_tables():
    # Get a list of tables
    cursor.execute("SHOW TABLES")
    tables = [table[0] for table in cursor.fetchall()]

    # Return the list of tables
    return jsonify(tables)

@app.route('/view_table/<table_name>')
def view_table(table_name):
    # Fetch all records from the specified table
    cursor.execute(f"SELECT * FROM {table_name}")
    table_content = cursor.fetchall()

    # Return the table content
    return jsonify(table_content)
@app.route('/lastrowid')
def lastrowid():
    return {1:cursor.lastrowid}

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)