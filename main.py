from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="codewipe",
    password="Robotics26!",
    database="codewipe"
)

cursor = db.cursor(dictionary=True)


# 1️⃣ Insert Record
@app.route('/insert_record', methods=['POST'])
def insert_record():

    data = request.json

    query = """
    INSERT INTO wipetable
    (username,email,Disk,Algorithm,Certificategenrated)
    VALUES (%s,%s,%s,%s,'No')
    """

    cursor.execute(query,(
        data['username'],
        data['email'],
        data['Disk'],
        data['Algorithm']
    ))

    db.commit()

    return jsonify({"message":"Inserted"})


# 2️⃣ Update Certificate = Yes
@app.route('/generate_certificate', methods=['POST'])
def generate_certificate():

    email = request.json['email']

    query = """
    UPDATE wipetable
    SET Certificategenrated='Yes'
    WHERE email=%s
    """

    cursor.execute(query,(email,))
    db.commit()

    return jsonify({"message":"Updated"})


# 3️⃣ Count Certificate Yes
@app.route('/count_certificate_yes', methods=['POST'])
def count_certificate_yes():

    email = request.json['email']

    query = """
    SELECT COUNT(*) as total
    FROM wipetable
    WHERE email=%s
    AND Certificategenrated='Yes'
    """

    cursor.execute(query,(email,))
    result = cursor.fetchone()

    return jsonify(result)


# 4️⃣ Count Records by Email
@app.route('/count_by_email', methods=['POST'])
def count_by_email():

    email = request.json['email']

    query = """
    SELECT COUNT(*) as total
    FROM wipetable
    WHERE email=%s
    """

    cursor.execute(query,(email,))
    result = cursor.fetchone()

    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5003,debug=True)