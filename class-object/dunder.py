class Avto:
    """Avtomobil klassi"""
    __num_avto = 0

    def __init__(self, make, model, rang, yil, narh, km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1

    def __str__(self):
        return f"Avto: {self.make} {self.model}"

    def __repr__(self):
        """Ko'proq tavsiya qilinadi chunki
        bu methodko'proq funksiyalar bilan ham ishlaydi"""
        return f"Avto: {self.make} {self.model}"

    def __eq__(self, y):
        """
        Tengligini solishtiruvchi methon
        print(x == y)
        yordamida ishlaydi
        """
        return self.narh == y.narh

    def __lt__(self, y):
        """
        Kichikligini solishtiruvchi methon
        print(x < y)
        yordamida ishlaydi
        """
        return self.narh < y.narh

    def __le__(self, y):
        """
        Kichik yoki teng solishtiruvchi methon
        print(x <= y)
        yordamida ishlaydi
        """
        return self.narh <= y.narh


avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
avto2 = Avto("GM", "Malibu", "Qora", 2020, 20000)
# print(avto1 <= avto2)


class AvtoSalom:
    """Avtosalomm classi"""

    def __init__(self, name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni."

    def __getitem__(self, index):
        """
        Endi bemalol royxat ichidan index
        orqali chaqirsak ham bo'ladi.
        print(salon1[0])
        ! AGAR barcha elementlarni ko'rmoqchi bolsak >>> print(salon1[:])
        shu yo'ldan foydalanamiz
        """
        return self.avtolar[index]

    def __getitem__(self, index, qiymat):
        """
        Endi bemalol royxat ichidagi elementlarni 
        boshqasi bilan index orqali almashtirishimiz ham mumkin.
        print(salon1[0]) = Avto("BMW", "M5 e39", "Qora", 2020, 400000) 
        shu yo'ldan foydalanamiz
        """
        self.avtolar[index] = qiymat

    def add_avto(self, *qiymat):
        for avto in qiymat:
            if isinstance(avto, Avto):
                self.avtolar.append(avto)
            else:
                print("Avto kiriting")


salon1 = AvtoSalom("MaxAvto")

avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
avto2 = Avto("GM", "Lacetti", "Oq", 2020, 20000)
avto3 = Avto("Toyota", 'Carolla', "Silver", 2018, 45000)
salon1.add_avto(avto1, avto2, avto3)
# avto4 = Avto("Mazda", "6", 'Qizil', 2015, 35000)
# avto5 = Avto("Volkswagen", "Polo", 'Qora', 2015, 30000)
# avto6 = Avto("Honda", "Accord", "Oq", 2017, 42000)

print(salon1[0])