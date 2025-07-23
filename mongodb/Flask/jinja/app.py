
from flask import Flask,render_template
app=Flask(__name__)
@app.route('/', methods=['GET'])
def hello():
    a="welcome"


    return render_template('fol.html', val=a)

@app.route('/data', methods=['GET'])
def sample_data():
    user_data={
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "phone": "+91-9876543210",
        "age": 26,
        "city": "Bangalore",
        "skills": ["Python", "Flask", "HTML", "CSS", "JavaScript"],
        "education": {
            "high_school": "St. Mary's High School",
            "undergraduate": "B.Sc. Computer Science - ABC College",
            "postgraduate": "M.Sc. Data Science - XYZ University"
        }
    }
    return render_template('fol.html', data=user_data)


if __name__ == '__main__':
    app.run(debug=True)
