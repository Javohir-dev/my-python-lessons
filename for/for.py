cars = ['Malibu', 'Captiva', 'BMW', 'Tesla']
for car in cars:
    print(car)
# * yoki qiyinroq pastdagidek yozsa ham bo'ladi.
cars = ['Malibu', 'Captiva', 'BMW', 'Tesla']
counter = 0
while counter < len(cars):
    car = cars[counter]
    print(car)
    counter = counter + 1
# * sanoq.
for number in range(1, 10001):
    print(number)

mehmonlar = ['Ali', 'Vali', 'Eshon', 'Husan', 'Olim']
print("Salom", mehmonlar[0])
for mehmon in mehmonlar:
    print("Salom", mehmon)
    print(mehmon, "Haxshi keldingmi?")

for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon} sizni 22-fevral kuni bolib o'tadiga kechamizga taklif qilamiz.")
    print("Hurmat bilan X.Javohir\n")

sonlar = list(range(1, 11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng.")

sonlar = list(range(11)) # 0 dan 10 ga sonlar chiqadi.
sonlar_kvadrati = [] # bo'sh royxat.
for son in sonlar:
    sonlar_kvadrati.append(son**2) #* uning kv.ni hisoblab, sonlar_kvadratiga joylaydi.

print(sonlar)
print(sonlar_kvadrati)

dostlar = [] # bo'sh royxat.
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5): # n bu yerda 0dan 4gacha qiymaqtlarni oladi.
    dostlar.append(input(f"{n + 1}-do'stingizni ismini kkiriting:\n>>> ")) #* bu yerda {n + 1} 0.1.2.3.4 o'niga 1.2.3.4.5. chiqishi uchun.
print(dostlar)
tanish = []
print("Bugun necha kishi bilan suhbatlashdingiz?>>>")
a = input()
for i in range(0):
    tanish.append(input(f"{i + 1}-suhbatlashgan kishingiz"))
    print(tanish)
i_odam = int(input(f"Bugun nechta odam bilan ko'rishdingiz:>>>"))
isimlar = []
for i in range(i_odam):
    isimlar.append(input(f"{i + 1}-suhbat qilgan odamingiz kim edi:>>> "))
print(isimlar)