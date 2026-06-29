from flask import Flask, request
import sqlite3
import subprocess
import os

app = Flask(__name__)

# Vuln 1: Hardcoded secret (you'll see Gitleaks catch this)
SECRET_KEY = "supersecret123"
DB_PATH = "users.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    conn.execute("INSERT OR IGNORE INTO users VALUES (1, 'admin', 'admin123')")
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return "DevSecOps Lab — vulnerable app running"

# Vuln 2: SQL injection
@app.route("/user")
def get_user():
    username = request.args.get("username", "")
    conn = sqlite3.connect(DB_PATH)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor = conn.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return str(rows)

# Vuln 3: Command injection
@app.route("/ping")
def ping():
    host = request.args.get("host", "localhost")
    output = subprocess.check_output(f"ping -c 1 {host}", shell=True)
    return output

# Vuln 4: Path traversal
@app.route("/file")
def read_file():
    filename = request.args.get("name", "")
    with open(os.path.join("/tmp", filename)) as f:
        return f.read()

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
