from flask import Flask,render_template,redirect, request,url_for

app=Flask(__name__)
@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        username =request.form.get('username')
        return redirect(url_for('show_name', name=username))

    return render_template('index.html')

@app.route('/name/<name>')
def show_name(name : str):
    return f'Hello {name}'

if __name__ == '__main__':
    app.run(debug=True)