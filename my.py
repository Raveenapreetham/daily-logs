class prof:
    def __init__(self,about, gender, place, dob):
        self.about=about
        self.user_gender = gender
        self.user_place = place
        self.user_dob = dob

    def pro(self):
        return f' My about is:{self.about}, Gender:{self.user_gender}, Place:{self.user_place}, Dob:{self.user_dob}'
