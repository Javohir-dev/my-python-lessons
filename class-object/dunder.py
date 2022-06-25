# dars linki: https://www.youtube.com/watch?v=KOKEsau2uaU&t=0s
# ? 1-qism

# dars linki: https://youtu.be/ltTOXJJiPRk
# ? 2-qism

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
        bu method ko'proq funksiyalar bilan ham ishlaydi"""
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


class AvtoSalon:
    """Avtosalonm classi"""

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

    def __setitem__(self, index, qiymat):
        """
        Endi bemalol royxat ichidagi elementlarni 
        boshqasi bilan index orqali almashtirishimiz ham mumkin.
        print(salon1[0]) = Avto("BMW", "M5 e39", "Qora", 2020, 400000) 
        shu yo'ldan foydalanamiz
        """
        self.avtolar[index] = qiymat

    def __call__(self, *qiymat):
        if qiymat:
            for avto in qiymat:
                self.add_avto(avto)
        else:
            return [avto for avto in self.avtolar]

    def __add__(self, y):
        """
        Ikkala salon nomi va mashinalarni
        bir biriga qoshiadigan method
        """
        if isinstance(y, AvtoSalon):
            yangi_salon = AvtoSalon(f"{self.name} {y.name}")
            yangi_salon.avtolar = self.avtolar + y.avtolar
            return yangi_salon
        elif isinstance(y, Avto):
            """agar user avto kiritsa yani salon1 + avto4 
            salon1 ga yangi mashina qoshiladi"""
            self.add_avto(y)

    def add_avto(self, *qiymat):
        for avto in qiymat:
            if isinstance(avto, Avto):
                self.avtolar.append(avto)
            else:
                print("Avto kiriting")


# ? Bu bilan yangi salon yaratib unga nom berayapmiz.
salon1 = AvtoSalon("MaxAvto")

# ? Yangi salon yaratildi
salon2 = AvtoSalon("Avto Lider")

avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
avto2 = Avto("GM", "Lacetti", "Oq", 2020, 20000)
avto3 = Avto("Toyota", 'Carolla', "Silver", 2018, 45000)
salon1.add_avto(avto1, avto2, avto3)

avto4 = Avto("Mazda", "6", 'Qizil', 2015, 35000)
avto5 = Avto("Volkswagen", "Polo", 'Qora', 2015, 30000)
avto6 = Avto("Honda", "Accord", "Oq", 2017, 42000)
salon2(avto4, avto5, avto6)


salon3 = salon1 + salon2
# print(f"\n{salon3()}\n")
salon1 + avto4  # orqali yangi mashina qoshayapmiz
print(salon1())
