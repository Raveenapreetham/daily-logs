from flask import Flask

app= Flask(__name__)

@app.route('/')
def name():
    return ('<h3>Self intro </h3>'
    '<h3>Good morning to all, Thank you for giving me this opportunity</h3>'
    '<h2>My name is <h2 style="color:blue"> Raveena Preetham R</h2>From Villupuram </h2>'
    '<h2><p>I have completed my graduation in <h2 style="color:blue">BSC.Computer Science </h2>at Sanghamam college of arts and science from Annamalai university</p></h2>'
    '<h2>I have completed one month intership on </bold>"FSD"</bold></h2>'
    '<h2>I have completed certification</h2>'
    '<ul>'
    '<li> HTML</li>'
    '<li>CSS</li>'
    '<li>Excel</li>'
    '<li>Basic of python</li></ul>'
    '<center><h2>Thats all about me thanks</h2></center>'
    )



if __name__ == '__main__':
    app.run(
        debug=True,
        port=1000,
        host='localhost'

    )
