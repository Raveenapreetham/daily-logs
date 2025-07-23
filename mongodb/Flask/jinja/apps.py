from flask import Flask,render_template

app=Flask(__name__)
@app.route('/', methods=['GET'])
def hello():
    a="welcome"


    return render_template('fol.html', val=a)

@app.route('/data', methods=['GET'])
def sample_data():
    user_data={

    "user1": {
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
    },
    "user2": {
        "name": "Bob Smith",
        "email": "bob@example.com",
        "phone": "+91-9876501234",
        "age": 28,
        "city": "Chennai",
        "skills": ["Java", "Spring", "Hibernate", "SQL"],
        "education": {
            "high_school": "Greenwood High",
            "undergraduate": "B.E. IT - LMN Institute",
            "postgraduate": "M.Tech Software Engg - PQR University"
        }
    },
    "user3": {
        "name": "Charlie Lee",
        "email": "charlie@example.com",
        "phone": "+91-9876001122",
        "age": 24,
        "city": "Hyderabad",
        "skills": ["JavaScript", "React", "Node.js", "MongoDB"],
        "education": {
            "high_school": "DAV Public School",
            "undergraduate": "B.Sc. Information Tech - KLM College",
            "postgraduate": "M.Sc. Full Stack - UVW University"
        }
    },
    "user4": {
        "name": "Diana Prince",
        "email": "diana@example.com",
        "phone": "+91-9876123456",
        "age": 27,
        "city": "Delhi",
        "skills": ["Python", "Django", "Bootstrap", "SQLAlchemy"],
        "education": {
            "high_school": "Sunshine Academy",
            "undergraduate": "BCA - DEF College",
            "postgraduate": "MCA - JKL University"
        }
    },
    "user5": {
        "name": "Ethan Hunt",
        "email": "ethan@example.com",
        "phone": "+91-9876234567",
        "age": 30,
        "city": "Mumbai",
        "skills": ["Go", "Docker", "Kubernetes", "PostgreSQL"],
        "education": {
            "high_school": "National High",
            "undergraduate": "B.Tech CSE - TUV Institute",
            "postgraduate": "M.Tech DevOps - QRS University"
        }
    },
    "user6": {
        "name": "Fiona Glenanne",
        "email": "fiona@example.com",
        "phone": "+91-9876345678",
        "age": 25,
        "city": "Pune",
        "skills": ["Ruby", "Rails", "Tailwind CSS", "GraphQL"],
        "education": {
            "high_school": "Hilltop School",
            "undergraduate": "B.Sc. Computer Apps - MNO College",
            "postgraduate": "M.Sc. Software Dev - STU University"
        }
    },
    "user7": {
        "name": "George Mason",
        "email": "george@example.com",
        "phone": "+91-9876456789",
        "age": 29,
        "city": "Ahmedabad",
        "skills": ["PHP", "Laravel", "MySQL", "jQuery"],
        "education": {
            "high_school": "City Central",
            "undergraduate": "BCA - XYZ College",
            "postgraduate": "MCA - OPQ University"
        }
    },
    "user8": {
        "name": "Hannah Wells",
        "email": "hannah@example.com",
        "phone": "+91-9876567890",
        "age": 31,
        "city": "Kolkata",
        "skills": ["C#", ".NET Core", "Azure", "SQL Server"],
        "education": {
            "high_school": "Crescent High",
            "undergraduate": "B.Sc. Software Systems - ABC Institute",
            "postgraduate": "M.Sc. Cloud Computing - LMN University"
        }
    },
    "user9": {
        "name": "Ian Gallagher",
        "email": "ian@example.com",
        "phone": "+91-9876678901",
        "age": 23,
        "city": "Coimbatore",
        "skills": ["Flutter", "Dart", "Firebase", "Figma"],
        "education": {
            "high_school": "Modern Public School",
            "undergraduate": "B.Sc. Mobile Dev - KLM College",
            "postgraduate": "M.Sc. App Dev - UVW University"
        }
    },
    "user10": {
        "name": "Jane Doe",
        "email": "jane@example.com",
        "phone": "+91-9876789012",
        "age": 27,
        "city": "Trivandrum",
        "skills": ["Swift", "iOS", "Xcode", "UI/UX"],
        "education": {
            "high_school": "City Girls High",
            "undergraduate": "B.E. Electronics - DEF Institute",
            "postgraduate": "M.Tech. Embedded Systems - RST University"
        }
    }
}

    return render_template('fol.html', data=user_data)


if __name__ == '__main__':
    app.run(debug=True)