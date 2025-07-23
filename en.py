#public access modifiers

class Parent:
    def __init__(self,Name,age):
        self.Name = Name
        self.age = age


class child(Parent):
    def info(self):
        return self.Name,self.age

    a = Parent("Ravi",29)
    print(a.age)
    print(a.Name)

#####################################################################

#protected access modifiers

class Parent:
    def __init__(self, Name):
        self._Name = Name

class Child(Parent):
    def __init__(self, Name, age):
        super().__init__(Name)
        self._age = age

    def info(self):
        print(f"Name: {self._Name}, Age: {self._age}")


a = Child("Raveena", 30)
a.info()

#####################################################################################

#private access modifiers


class Parent:
    def __init__(self, Name):
        self.__Name = Name

class Child(Parent):
    def __init__(self, Name, age):
        super().__init__(Name)
        self.__age = age

    def info(self):
        print(f"Name: {self.__Name}, Age: {self.__age}")


a = Child("Raveena", 30)
a.info()



