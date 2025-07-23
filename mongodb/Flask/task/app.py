from flask import Flask, render_template, request, redirect, url_for
import json, os

app = Flask(__name__)
DATA_FILE = 'data.json'


def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

def save_users(users):
    with open(DATA_FILE, 'w') as file:
        json.dump(users, file, indent=4)


@app.route('/', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = {
            "username": request.form['username'],
            "email": request.form['email'],
            "password": request.form['password']
        }
        users = load_users()
        if any(u['email'] == user['email'] for u in users):
            return "Email already registered!"
        users.append(user)
        save_users(users)
        return redirect(url_for('login'))
    return render_template('Register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        for u in users:
            if u['username'] == username and u['password'] == password:
                return render_template('Dashboard.html', username=u['username'])
        return "Invalid email or password!"
    return render_template('Login.html')

if __name__ == '__main__':
    app.run(debug=True)