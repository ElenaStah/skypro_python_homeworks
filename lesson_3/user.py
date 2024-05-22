
class User:

    def __init__(self, first_name, last_name):
        print("Mое имя ", first_name)
        self.userfirst_name = first_name
        self.userlast_name = last_name


    def sayLastName(self):
        print("Моя фамилия", self.userlast_name)

    def sayFullName(self):
        print("Меня зовут ", self.userfirst_name, self.userlast_name)


