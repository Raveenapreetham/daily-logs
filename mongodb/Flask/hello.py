from flask import Flask, render_template,request

app=Flask(__name__)
@app.route('/')
@app.route('/hello')

def yashika():
    return (render_template("welcome.html"))



if __name__=='__main__':
    app.run(debug=True)
