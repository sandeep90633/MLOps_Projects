# Put and Delete - HTTP verbs
# Workinng with APIs - Json

from flask import Flask, request, jsonify
import psycopg2

# DB Connection Function
def get_db_connection():
    conn = psycopg2.connect(
        dbname="sql_practice",
        user="postgres",
        password="Dinu@123",
        host="127.0.0.1",
        port="5433"
    )
    return conn

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome!"

# To see all the users
@app.route("/items", methods=['GET'])
def get_all_users():
    conn = get_db_connection()
    cur = conn.cursor()

    # Fetch all users
    cur.execute("SELECT id, username FROM users;")
    rows = cur.fetchall()

    # Convert to list of dictionaries
    users = []
    for row in rows:
        users.append({
            'id': row[0],
            'username': row[1]
        })

    cur.close()
    conn.close()

    return jsonify(users)

# To add users into the db
@app.route("/items", methods = ['POST'])
def add_users():
    if not request.json or not 'username' in request.json:
        return jsonify({"error":"item not found"})
    
    username= request.json['username']
    password= request.json['password']
    
    conn = get_db_connection()
    cur = conn.cursor()

    try:
        # Fetch all users
        cur.execute("SELECT id FROM users ORDER BY id DESC LIMIT 1;")
        result = cur.fetchone()
        new_id = result[0] +1 if result else 1
        
        cur.execute(
            "INSERT INTO users (id, username, password) VALUES (%s, %s, %s);",
            (new_id, username, password)
        )
        conn.commit()
        
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    
    finally:
        cur.close()
        conn.close()

    return jsonify({
        "message": "User added successfully",
        "user": {
            "id": new_id,
            "username": username
        }
    }), 201    
    
@app.route("/items/<int:id>", methods=['PUT'])
def update_user(id):
    if not request.json or not 'username' in request.json or not 'password' in request.json:
        return jsonify({"error":"item not found"})
    
    username= request.json['username']
    password= request.json['password']
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        cur.execute("UPDATE users SET username= %s, password= %s WHERE id=%s;", (username, password, id))
        conn.commit()
        
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    
    finally:
        cur.close()
        conn.close()
        
    return jsonify({
        "message": "User data updated successfully",
        "user": {
            "id": id,
            "username": username
        }
    }), 201
    
@app.route("/items/<int:id>", methods=['DELETE'])
def delete_user(id):
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        cur.execute("DELETE FROM users WHERE id= %s", (id,))
        conn.commit()
    
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    
    finally:
        cur.close()
        conn.close()
    
    return jsonify({
        "message": "User data deleted successfully",
        "user": {
            "id": id
        }
    }), 201
    
if __name__ == "__main__":
    app.run(debug=True)
    