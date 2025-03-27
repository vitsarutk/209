from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="db_server",
    user="root",
    password="rootpassword",
    database="unidb"
)

@app.route('/')
def hello():
    return "Hello from Flask Backend!"

@app.route('/api/users')
def get_users():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM student")
    users = cursor.fetchall()
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
