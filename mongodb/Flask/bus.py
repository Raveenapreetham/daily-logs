from flask import Flask,render_template,redirect, request,url_for

app=Flask(__name__)
@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        username =request.form.get('username,password,confirm_password,gender')
        return redirect(url_for('show_name',name= username,password=password,confirm_password=confirm_password,gender=gender))
    return render_template('login.html')

@app.route('/name/<name>')
def show_name(name, password, confirm_password,gender):
    return f'Name:{name}, Password:{password}, Confirm_password:{confirm_password}, Gender:{gender}'

if __name__ == '__main__':
    