
# # ? while tsiklidan foydalanib ro'yhat yaratish
    !
    

# print("Yaqin do'stlaringiz ro'yhatini yuzamiz.")
# ismlar = []
# n = 1
# while True:
#     savol = f"{n}-do'stingizni kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     n += 1
#     if takrorlash != 'ha':
#         break
# print("Do'stlaringiz ro'yhati:")
# for ism in ismlar:
#     print(ism.title())

# print("Do'stlaringizni yoshini saqlaymiz.")
# frends = {}
# sign = True
# while sign:
#     name = input("Do'stingiz ismini kiriting: ")
#     age = input("Endi yoshini kiriting: ")
#     frends[name] = int(age)  # intager orqali lig'atga [kalit so'z] va qiymat

#     answers = input("Yana ma'lumot qo'shasizmi? (ha/yo'q) ")
#     if answers.lower().strip() == "yo'q":
#         sign = False


# for name, age in frends.items():
#     print(f"{name.title()} {age} yoshda.")

# cars = ['lacetti', 'nexia', 'gentra', 'bmw', 'mers', 'nexia']
# car = 'nexia'
# while car in cars:
#     cars.remove('nexia')
# print(cars)

# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop() #* pop() methodi orqali 'talabalar'ni ichidan 1tasini sug'irib olamiz va uni 'talaba' ga joylaymiz
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholan4di.")
#     baholangan_talabalar[talaba] = int(baho)
# for n, b in baholangan_talabalar.items():
#     print(f"{n.title()}ning bahosi: {b}")
# print(baholangan_talabalar) #* {'botir': 5, 'olim': 2, 'husan': 4, 'hasan': 4}

# ! Mashg'ulotlar:
"""
? 1.Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
"""

# buyurtmalar = []
# print("\n🚫Agar buyurtmani tohtatmoqchi bo'lsangiz '-' ni bosing.")
# buyurtma = input("\nNima buyurtma qilasiz?\n>>> ")
# while True:
#     buyurtma = input("\nYana nima buyurtma qilasiz?\n>>> ")
#     if buyurtma != '-' and buyurtma != 'stop':
#         buyurtmalar.append(buyurtma)
#     else:
#         break
# print(f"Buyurtmangiz {buyurtmalar}")
"""
? 1.e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
"""
# mahsulot = {}
# while True:
#     product = input("\nMahsulot nomini kiriting: ")
#     price = input("\nNarxni kiriting: ")
#     mahsulot[product] = price
#     st = int(input("\n🚫Mahsulotlar tugagan bo'lsa '0' hali bor bo'lsa '1' deb yozing: "))
#     if st == 0:
#         break
# print(mahsulot)
