def toliq_ism_yasa(ism, familiya):
    """To'liq ism qaytaruvchi funksiya."""
    toliq_ism = f"{ism.title()} {familiya.title()}"
    return toliq_ism


# * Hohlagan paytda hohlagan joyda foydalanish uchun shu yo'ldan foydalandik
talaba = toliq_ism_yasa('olim', 'hakimov')

talaba1 = toliq_ism_yasa('javohir', 'khamidullayev')
talabe2 = toliq_ism_yasa('hasan', 'husanov')
print(f"Darsga kelmagan talabalar: {talaba1} va {talabe2}.")
print(f"{talaba.title()} darsga kechikib keldi.")

# ? ihtiyoriy ma'lumot.
def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
    """To'liq ism qaytaruvchi funksiya"""
    if otasining_ismi:
        toliq_ism = f"{ism} {familiya} {otasining_ismi}"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism.title()


talaba1 = toliq_ism_yasa('javohir', 'khamidullayev')
talabe2 = toliq_ism_yasa('hasan', 'husanov', 'akmalovich')
print(f"Darsga kelmagan talabalar: {talaba1.title()} va {talabe2.title()}.")

def avto_info(kompaniya, model, rang, korobka, yili, narxi=None):
    avto = {
        'kompaniya': kompaniya,
        'model': model,
        'rang': rang,
        'korobka': korobka,
        'yil': yili,
        'narx': narxi}
    return avto


avto1 = avto_info('GM', 'malibu', 'qora', 'avtomat', 2021)
avto2 = avto_info('BMW', 'm5 e39', 'mokri', 'mehanik', 2020, 15000)
avtolar = [avto1, avto2]
print("Online bozordagi avtomobillar: ")
for avto in avtolar:
    if avto['narx']:
        narx = f"{avto['narx']}$"
    else:
        narx = "Noma'lum"
    print(f"{avto['model']} {avto['rang'].upper()}. Narxi: {narx}")


def oraliq(min, max, step=1):
    """
        oraliq(stop) -> oraliq object oraliq(start, stop[, step]) -> oraliq object

    Return an object that produces a sequence of integers from start (inclusive)
    to stop (exclusive) by step. oraliq(i, j) produces i, i+1, i+2, ..., j-1. start
    defaults to 0, and stop is omitted! oraliq(4) produces 0, 1, 2, 3. These are exactly
    the valid indices for a list of 4 elements. When step is given, it specifies the
    increment (or decrement).
    """
    sonlar = []
    while min < max:
        sonlar.append(min)
        min += step
    return sonlar


print(oraliq(0, 100, 10))
# ?
def avto_info(kompaniya, model, rang, korobka, yili, narxi):
    avto = {
        'kompaniya': kompaniya,
        'model': model,
        'rang': rang,
        'korobka': korobka,
        'yil': yili,
        'narx': narxi}
    return avto


print("Saytimizdagi avtolar ro'yhatini shakllantiramioz.")
avtolar = []  # Salondagi avtolar uchun bo'sh ro'yhat.
while True:
    print("\nQuyidagi ma'lumotlarni kiriting:", end='')

    kompaniya = input(" Ishlab chiqaruvchi: ")
    model = input(" Modeli: ")
    rang = input(" Rangi: ")
    korobka = input(" Korobka: ")
    narxi = input(" Narxi: ")
    yili = input(" Yili: ")

    avtolar.append(avto_info(kompaniya, model, rang, korobka, yili, narxi))
    # Dastur davom etishi yoki to'xtashi.
    javob = input("Yana avtomobil qo'shasizmi? (Yes/No): ")
    if javob.strip().lower() == 'no':
        break
print("\nSalonimizdagi avtomobillar:")
for avto in avtolar:
    if avto['narx']:
        narx = avto['narx']
    else:
        narx = "Noma'lum"

print(f"{avto['rang'].title()}, {avto['model'].upper()}, {avto['korobka']}. Narxi:{narx} so'm")

# ! Mashg'ulot:

def mijoz_info(ism, familiya, tyil, tjoy, email="", tel=None):
    """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    mijoz = {
        "ism": ism,
        "familiya": familiya,
        "tyil": tyil,
        "yoshi": 2022 - tyil,
        "tjoy": tjoy,
        "email": email,
        "telefon": tel,
    }
    return mijoz


print("Foydalanuvchi ma'lumotlarini kiriting.")
mijozlar = []  # user ma'lumotlari uchun bo'sh ro'yxat
while True:
    ism = input("Ismingiz: ")
    familiya = input("Familiyangiz: ")
    tyil = int(input("Tug'ilgan yilingiz: "))
    tjoy = input("Tug'ilgan joyingiz: ")
    email = input("Emailingiz: ")
    telefon = input("Telefon raqamingiz: ")

    mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
    javob = input("Dasturni davom ettirasizmi? (ha/yo\'q): ")
    if javob != 'ha':
        break

print("Mijozlar: ")
for mijoz in mijozlar:
    print(
        f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
        f"{mijoz['yoshi']} yoshda, telefon nomeri: {mijoz['telefon']}"
    )
