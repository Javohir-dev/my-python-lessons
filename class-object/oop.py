class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil


talaba1 = Talaba("Javohir", "Khamidullaev", 2002)
talaba2 = Talaba("Olim", "Khakimov", 2004)
talaba3 = Talaba("Qodirhon", "Alimov", 1994)
talaba4 = Talaba("Doston", "Ubadullaev", 2000)
students = [talaba1, talaba2, talaba3, talaba4]
for student in students:
    print(student.ism)
    print(student.familiya)
    print(student.tyil)


class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil

    def get_name(self):
        return self.ism

    def lastname(self):
        return self.familiya

    def get_age(self, yil):
        return yil - self.tyil

    def tanishtir(self):
        return f"Ismim {self.ism} {self.familiya}, tug'ilgan yilim {self.tyil}.\n"


talaba1 = Talaba("Javohir", "Khamidullaev", 2002)
talaba2 = Talaba("Olim", "Khakimov", 2004)
talaba3 = Talaba("Qodirhon", "Alimov", 1994)
talaba4 = Talaba("Doston", "Ubadullaev", 2000)
students = [talaba1, talaba2, talaba3, talaba4]
for student in students:
    print(student.tanishtir())

print(talaba1.get_name())
print(talaba1.get_age(2022))


#! MASHG'ULOT
class User:
    def __init__(self, name, lastname, username, gmail):
        self.name = name
        self.lastname = lastname
        self.username = username
        self.gmail = gmail

    def get_name(self):
        return self.name

    def get_lsname(self):
        return self.lastname

    def get_username(self):
        return self.username

    def get_mail(self):
        return self.gmail

    def get_info(self):
        return f"Foydalanuvchi: {self.get_username()}, ismi: {self.get_name()} {self.get_lsname()}, email: {self.get_mail()}"


talaba1 = User("Javohir1", "Khamidullaev",
               "javohir.coder", "coderjek@gmail.com")
talaba2 = User("Abdulaziz", "Olimov",
               "abdulaziz.coder", "coderabdu@gmail.com")
talaba3 = User("Shoxruh", "Abdurahmonov",
               "shaxa.dev", "shox4747@gmail.com")
talaba4 = User("Jahongir", "Sadullaev",
               "jahongir.925", "johon925@gmail.com")
students = [talaba1, talaba2, talaba3, talaba4]
for student in students:
    print(student.get_info())
