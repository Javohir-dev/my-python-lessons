from uuid import uuid4


class Avto:
    """Avtomabil classi"""

    def __init__(self, make, model, rang, yil, narh, km=0):
        """Avtomabilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self, km):
        """Mashinani km ga yana km qoshish"""
        if km >= 0:
            self.__km += km
        else:
            print("Mashinaning km ni kamaytirib bo'lmaydi.")


avto1 = Avto("GM", "Malibu", "Qora", 2021, 35000, 1000)
# print(avto1.get_id(), avto1.get_km())


class Avto2:
    """Avtomobil klassi"""
    __num_avto = 0

    def __init__(self, make, model, rang, yil, narh, km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto2.__num_avto += 1

    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self, km):
        """Mashinani km ga yana km qoshish"""
        if km >= 0:
            self.__km += km
        else:
            print("Mashinaning km ni kamaytirib bo'lmaydi.")


avto1 = Avto2("GM", "Malibu", "Qora", 2020, 40000)
avto2 = Avto2("GM", "Lacetti", "Oq", 2020, 20000)
avto3 = Avto2("Toyota", 'Carolla', "Silver", 2018, 45000)
print(Avto2.get_num_avto())
