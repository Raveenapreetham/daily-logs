from flask import Flask,render_template,request,flash,redirect,url_for,session,jsonify
from datetime import datetime
from business import collection
from utils import login_required
app=Flask(__name__)
app.secret_key='dreams'

@app.route('/register',methods=['GET'])
def register_get():
    return render_template('register.html')

@app.route('/register',methods=['POST'])
def register_post():
    username=request.values.get("name")
    password=request.values.get("password")
    confirmPassword=request.values.get("confirmPassword")

    if password != confirmPassword:
        flash('password mismatch', 'success')
        return render_template('register.html')

    user_dict ={
    "name":username,
     "password":password,
     "created_at":datetime.now()
     }
    if user_dict["name"]:
        collection.insert_one(user_dict)

        flash("user register successfully","success")
        return redirect(url_for('login_get'))

    flash("user register failed","error")
    return render_template('register.html')

@app.route('/login',methods=['GET'])
def login_get():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    try:
        name=request.values.get("name")
        password=request.values.get("password")
        user=collection.find_one({"name":name})
        if not user:
            flash('user not found','error')
            return redirect(url_for('register_get'))
        if user['password'] == password:
            session['name']=name
            session['logged_in']=True
            session['logged_at']=datetime.now()
            flash('login successful','success')
            return redirect(url_for('home'))

        flash('incorrect password','error')
        return render_template('login.html')
    except Exception:
        flash('login failed, try again later','error')
        return render_template('login.html')
@app.route('/sed')
def session_data():
    return jsonify(session)

@app.route('/user')
@login_required
def show_user():
    username = session.get('name')
    return f'<h1>hello {username}</h1><br><h1>last login :{session.get('logged_at')}'
app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login_get'))



@app.route('/home')
@login_required
def home():
    return "hello everyone"

if __name__ =='__main__':
    app.run(debug=True)