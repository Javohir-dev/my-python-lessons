
cars = ['mers', 'bmw', 'audi', 'kia', 'volvo']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else :
        print(car.title())

ism = input('Ismingiz nima?\n>>> ')
if ism.lower() != 'javohir':
    print(f'Kechirasiz  {ism.title()} biz Javohirni kutyapmiz.')
else:
    print('Salom, Javohir')

javob = float(input("12 x 6 nechiga teng?\n>>> "))
if javob != 12 * 6:
    print('Javob xato!')
else :
    print('qoil')

yosh = int(input("Yoshingizni kiriting:\n>>> "))
if yosh >= 18:
    print('Xush kelibsiz 😁')
else :
    print("18 yoshga to'lmaganlar kirish taqiqlanadi!")

login = input("Yangi login tanlang: ")
if len(login) <= 5:
    print("login 5ta harfdan ko'proq bo'ishi shart!")

yil = int(input("Tug'ilgan yilingizni kiriting: "))
if 2022 - yil < 18:
    print(f"Sizni yoshingiz {2022 - yil} ekan.")
    print("Kirsh mumkin emas!")
else :
    print("Xush kelibsiz 😁")

yosh = int(input("Yoshingiz nechida? >>> "))
if yosh > 65: print("siz COVIT-19 risk guruhida ekansiz.")

x, y = 25, 50
print("x > y") if x > y else print("x < y")