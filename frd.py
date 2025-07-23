from my import prof
b=prof("about myself", "Female","Gingee", "25/11/2004")

class Name:
    def __init__(self, name, age , email, number):
        self.user_name = name
        self.user_age = age
        self.user_email = email
        self.user_number = number

    def log(self):
        c = b.pro( )

        return f'My name is: {self.user_name}, My age is:{self.user_age}, My email is:{self.user_email}, My number is:{self.user_number},{c}'

a= Name("raveena",20,"rave@gamil.com",2345678912)


print(a.log())
