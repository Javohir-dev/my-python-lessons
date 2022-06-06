
# ! Dars linki in YouTube
# ? https://youtu.be/uzNp5XNOZ_I
# * https://python.sariq.dev/function/22-flexible-functions

# TODO: *args

def summa(*sonlar):
    """ Kiritilgan sonlar yig'indisini hisoblaydigan funsiya """
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi


print(summa(1, 2, 3))
print(summa(1, 2, 3, 4))
print(summa(1, 2, 3, 4, 5))

# ikkala funsiya ham bir hil vazifani bajaradi


def summa(*sonlar):
    """ Kiritilgan sonlar yig'indisini hisoblaydigan funsiya """
    return sum(sonlar)


print(summa())
print(summa(1, 2, 3))
print(summa(1, 2, 3, 4))
print(summa(1, 2, 3, 4, 5))


def summa(x, y, *sonlar):
    """ Kiritilgan sonlar yig'indisini hisoblaydigan funsiya """
    return x + y + sum(sonlar)


print(summa(1, 2))
print(summa(1, 2, 3))
print(summa(1, 2, 3, 4))

# TODO: **kwargs -> keywords


def avto_info(kompaniya, model, **malumotlar):
    """ Avtomabillarni ma'lumotlarni lug'at ko'rinishida saqlaydigan funksiya """
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar


avto1 = avto_info('GM', 'Malibu', rangi='qora', yili=2022)
print(avto1)

avto2 = avto_info('Kia', 'K5', rangi='qizil', narxi=35000, yili=2020)
print(avto2)

# ! AMALIYOT


def hisobla(*sonlar):
    """ Kiritilgan sonlar ko'paymasini hisoblaydigan funsiya """
    kopayma = 1
    for son in sonlar:
        kopayma *= son

    return kopayma


print(hisobla(4, 5, 6))


def malumotlar(ism, familiya, **talabalar):
    """ Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya """
    talabalar['ism'] = ism
    talabalar['familiya'] = familiya
    return talabalar


talaba1 = malumotlar("Javohir", "Khamidullaev")
talaba2 = malumotlar("Azam", "Hakimov", yili=1994, soha='IT')
print(talaba1, '\n', talaba2)
