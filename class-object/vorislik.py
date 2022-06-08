class Shaxs:
    """Shaxslar haqida ma'lumot"""

    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil


inson = Shaxs("Husan", "Akbarov", "AB9094422", 2001)
print(inson.get_info())
print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda.")


class Talaba(Shaxs):
    """Talaba klassi"""

    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info


# talaba1 = Talaba("Javojir", "Khamidullaev", "AB9094422", 2002, 'N1648542')
# print(talaba1.get_info())


class Manzil:
    """Manzil saqlash uchun class"""

    def __init__(self, uy, kocha, tuman, viloyat):
        """Manzil hususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil


talaba_manzil = Manzil(12, 'Olmazor', "Bog'bon", "Samarqand")
talaba = Talaba("Valijon", "Aliyev", "FA112299",2000, "0000012", talaba_manzil)
print(talaba.manzil.get_manzil())
