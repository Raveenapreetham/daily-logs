class parent:
    def __init__(self,name):
        self.username=name
class child(parent):
    def __init__(self,dep):
        super().__init__(self,name)
        self.user_dep=dep
    def info(self):
        return f'My name is:{self.username}, My dept is:{self.user_dep}'
obj=public('raveena')
print(obj.info())