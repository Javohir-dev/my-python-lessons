# car0 = {
#     "model": "lacetti",
#     "rang": "oq",
#     "yill": "2018",
#     "narx": 10000,
#     "km": 50000,
#     "karobka": "avtomat",
# }
# car1 = {
#     "model": "nexia 3",
#     "rang": "chocco",
#     "yill": "2016",
#     "narx": 12000,
#     "km": 55000,
#     "karobka": "mexanika",
# }
# car2 = {
#     "model": "elantra",
#     "rang": "qora",
#     "yill": "2022",
#     "narx": 34600,
#     "km": 50,
#     "karobka": "avtomat",
# }
# car = car1
# print(
#     f"{car['model'].title()}, "
#     f"{car['rang']} rangda, "
#     f"{car['yill']}-yil, {car['narx']}$"
# )
# cars = [car0, car1, car2]
# for car in cars:
#     print(f"\n{car['model'].title()}, "
#     f"\n{car['rang']} rangda, "
#     f"\n{car['yill']}-yil, {car['narx']}$" )


# print(cars[0]) #* Natija: {'model': 'lacetti', 'rang': 'oq', 'yill': '2018', 'narx': 10000, 'km': 50000, 'karobka': 'avtomat'}
# print(cars[1]['model']) #* Natija: nexia 3

# malibus = []
# for n in range(10):
#     new_car = {
#         "model": "malibu",
#         "rang": None,
#         "yill": "2022",
#         "narx": None,
#         "km": 0,
#         "karobka": "avtomat",
#     }
#     malibus.append(new_car)

# # print(malibus)
# for malibu in malibus[:3]:
#     malibu["rang"] = "qizil"

# for malibu in malibus[3:6]:
#     malibu["rang"] = "qora"

# for malibu in malibus[6:]:
#     malibu["rang"] = "oq"
#     malibu["karobka"] = "mexanika"

# for color in malibus:
#     print(color)

# for malibu in malibus:
#     if malibu["karobka"] == "avtomat":
#         malibu["narx"] = 40000
#     else:
#         malibu["narx"] = 35000


# for malibu in malibus:
#     print(malibu)

# coders = {
#     'ali':['python', 'c++'],
#     'vali':['html', 'css', 'js'],
#     'hasan':['php', 'mysql'],
#     'husan':['python', 'php'],
#     'olim':['c', 'c++', 'c#']
# }

# for ism, tillar in coders.items():
#     print(f"\n{ism.title()} biladigan tillar:")
#     for til in tillar:
#         print(til.upper())

# ? and = ''
# for ism, tillar in coders.items():
#     print(f"\n{ism.title()} biladigan tillar:")
#     for til in tillar:
#         print(f"{til.upper()}", end = ' ')

hamkasblar = {
    'ali': {'familiya': 'valiyev',
            'tyili': 1995,
            'malumoti': 'oliy',
            'tillar': ['python', 'c++']
            },
    'vali': {'familiya': 'aliyev',
            'tyili': 2001,
            'malumoti': 'o\'rta',
            'tillar': ['html', 'css', 'js']
            },
    'hasan': {'familiya': 'olimov',
            'tyili': 2000,
            'malumoti': 'oliy',
            'tillar': ['python', 'php']
            },
}

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}. "
        f"{info['tyili']}-yilda tug'ilgan.\n"
        f"Ma'lumoti: {info['malumoti']}. \n"
        "Quyidagi tillarni biladi:")
    for til in info['tillar']:
        print(til.upper())