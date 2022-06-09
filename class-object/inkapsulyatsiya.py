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


avto1 = Avto("GM", "Malibu", "Qora", 2021, 35000, 100000)
print(avto1.get_id(), avto1.get_km())
