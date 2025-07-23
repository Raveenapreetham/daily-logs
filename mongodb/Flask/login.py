from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)


user_data = 'users.json'

def load_user():
    if not os.path.exists(user_data):
        return []
    with open(user_data, 'r') as f:
        return json.load(f)

def save_user(user):
    users = load_user()
    users.append(user)
    with open(user_data, 'w') as f:
        json.dump(users, f, indent=1)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register_user', methods=['POST'])
def register_user():
    username = request.form['username']
    password = request.form['password']

    if not username or not password:

        return redirect(url_for('register'))

    user = {'username': username, 'password': password}

    return redirect(url_for('home'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    users = load_user()
    for user in users:
        if user['username'] == username and user['password'] == password:
            return redirect(url_for('dashboard', name=username))

    # flash("")
    return redirect(url_for('home'))

@app.route('/dashboard/<name>')
def dashboard(name):
    return render_template('dashboard.html', username=name)

if __name__ == '__main__':
    app.run(debug=True)