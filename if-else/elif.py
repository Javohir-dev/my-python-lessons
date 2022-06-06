num = -50
if num < 0:
    print("Manfiy son")
else :
    print("Musbat son")
# 
age = int(input("Yoshingiz nechida? "))
if age <= 4:
    narx = 0
elif age <= 12:
    narx = 5000
elif age <= 18:
    narx = 8000
else :
    narx = 10000

print(f"Sizga kirish {narx} so'm.")
# ? OR operatori:

day = input("bugun nima kun? ").lower()
if day == 'shanba' or day == 'yakshanba':
    print('Bugun dam olish kuni.')
else :
    print("Bubun ish kuni.")

# ? AND operatori:

day = input("bugun nima kun? ").lower()
harorat = float(input("Havo harorati qanday? "))

if day == 'yakshanba' and harorat >= 30:
    print("Chomilgani ketdik.")
elif day == 'yakshanba' and harorat < 30:
    print("Uyda dam olamiz.")
else:
    print("Bugun ish kuni.")

day = input("bugun nima kun? ")
harorat = float(input("Havo harorati qanday? "))

if (day.lower() == 'yakshanba' or day.lower() == 'shanba') and harorat >= 30:
    print("Toqqa goo.")
elif (day.lower() == 'yakshanba' or day.lower() == 'shanba') and harorat < 30:
    print("Uyda dam olamiz.")
else:
    print("Bugun ish kuni.")

narx = 15000
t = True
f = False
if t and f:
    narx = narx + 10000
elif t or f:
    narx = narx + 5000
#
print(f"Sizdan {narx} so'm bo'ldi.")
narx = 12000
choy = True #* yoki 1
salat = False #* yoki 0
non = 1 #* yoki True
kampot = 0 #* yoki False
assarti = False #* yoki 0 ham ishlatsak bo'ladi.
if choy:
    print("Mijoz choy sotib oldi.")
    narx = narx + 3000

if salat:
    print("Mijoz salat sotib oldi.")
    narx = narx + 5000

if non:
    print("Mijoz non sotib oldi.")
    narx = narx + 2000

if kampot:
    print("Mijoz kampot sotib oldi.")
    narx = narx + 1500

if assarti:
    print("Mijoz assarti sotib oldi.")
    narx = narx + 18000

print(f"Jami {narx}")

# ? IN operatori

menu = ['osh','qozonkabop', 'shashlik', 'norin', 'somsa']
print('somsa' in menu)

menu = ['osh','qozonkabop', 'shashlik', 'norin', 'somsa']
ovqat = input('Nima buyurtma qilasiz?\n>>> ')
if ovqat.lower() in menu:
    print("Buyurtma qabul qilindi.")
else:
    print("Uzur bizda bu taom yo'q.")

num = [12, 23, 34, 45, 56]
search = int(input('>>> '))
if search in num:
    print("ha")
else :
    print("yo'q")

# ? NOT IN operatori

menu = ['osh','qozonkabop', 'shashlik', 'norin', 'somsa']
ovqat = input('Nima buyurtma qilasiz?\n>>> ')
if ovqat.lower() not in menu:
    print(f"Uzur bizda {ovqat} yo'q.")
else:
    print("Buyurtma qabul qilindi.")
son = float(input("Birorta son kiriting: "))
if son:
    if (son % 2) == 0 :
        print(f"{son} juft son.")
    elif (son % 2) >= 1 :
        print(f"{son} toq son.")

menu = ['osh','qozonkabop', 'shashlik', 'norin', 'somsa']
buyurtma = []
buyurtma.append(input("Nima buyurasiz?\n>>> "))
if buyurtma:
    for taom in buyurtma:
        if taom in menu:
            print(f"    {taom} bor.")
        else: print(f"Kechirasiz menuda {taom} yo'q.")
else: print("Buyurtma qabul qilindi.")
print(f"Hozir {buyurtma} keladi.")


# ! Mustaqil ishlar.
# ? juft va toq son
num = int(input("Juft son kiriting: "))
if num % 2:
    print(f"{num} juft son emas.")
else: print("Raxmat!")
# ? Yoshiga qarab narx.
age = int(input("Yoshingiz nechida?\n>>> "))
if age <= 4 or age >= 60 :
    print("chipta bepul")
elif age <= 18 :
    print("10000 so'm")
elif age > 18 :
    print("20000 so'm")
else: print("Noto'g'ri ma'lumot kirittingiz.")
# ? Katta va kichik.
print("ikki hil son kiriting.")
a = float(input("\nbirinchi sonni kiriting: "))
b = float(input("\nikkinchi sonni kiriting: "))
if a < b :
    print(f"{a} < {b}")
elif a > b :
    print(f"{a} > {b}")
elif a == b:
    print("Sonlar teng.")
# ? Dokonda bor yoki yoqligini ko'rsatish
mahsulotlar = ['anor', 'uzum', 'olma', 'nok', 'tarvuz']
savat = []
numbers = list(range(1 , 6))
for number in numbers:
    savat.append(input(f"\nSavatga {number}-mahsulotni qo'shing: "))
print("\nDo'konimizda:")
for meva in savat:
    if meva in mahsulotlar:
        print(f"{meva} bor")
    else: print(f"{meva} yo'q")
# ? do'konda yo'g'ini chiqarish.
mahsulotlar = ['anor', 'uzum', 'olma', 'nok', 'tarvuz']
savat = []
numbers = list(range(1 , 6))
for number in numbers:
    savat.append(input(f"\nSavatga {number}-mahsulotni qo'shing: "))
print("\nDo'konda quyidagi maxsulotlar yo'q:")
for mahsulot in savat:
    if mahsulot not in mahsulotlar:
        print(mahsulot)
# ? Login kiritish.
login = ['javohir.coder', 'azizcik77', 'javohir77', 'kotta.bolla', 'abbos_98', 'massa_38']
search = input("\nIltimos login kiriting:\n>>> ").lower()
if len(search) >= 6:
    if search not in login:
        print("Xush kelibsiz!")
    elif search in login:
        print('bu login band, iltimos boshqa login tanlang.')
else:
    print('Login 6ta belgidan ko\'p bo\'lishi kerak.')
# ? butun son
num = int(input("butun son kiriting: "))
for i in range(2,11):
    if not num % i:
        print(f"{num} soni {i}ga qoldiqsiz bo'linadi.")