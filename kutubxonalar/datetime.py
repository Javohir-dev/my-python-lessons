import datetime as dt

hozir = dt.datetime.now()
print(hozir)  # Hozirgi vaqtni consolga chiqaradi
print(hozir.hour)
# soat
print(hozir.minute)
# daqiqa
print(hozir.second)
# soniya

bugun = dt.date.today()
print(f"Bugun sana: {bugun}")
# NATIJA: Bugun sana: 2022-06-27
ertaga = dt.date(2022, 6, 28)
print(f"Ertangi sana: {ertaga}")
# NATIJA: 2022-07-28
hozir = dt.datetime.now()
VaqtHozir = hozir.time()
print(f"Hozir soat: {VaqtHozir}")
# ^^ hozirgi soatni ajratib oladi
keyingiVaqt = dt.time(23, 59, 00)
print(keyingiVaqt)
# sanalar orasidagi vaqt
bugun = dt.date.today()
ramazon = dt.date(2022, 10, 13)
farq = ramazon - bugun
print(farq)
# ramazondan bugunni ayirdik
print(f"Ramazonga `{farq.days}` qoldi.")
hozir = dt.datetime.now()
futbol = dt.datetime(2022, 7, 10, 23, 45, 00)
farq = futbol - hozir
print(farq)
soniyalar = farq.seconds
minutlar = int(soniyalar/60)
soatlar = int(minutlar/60)
print(f"futbol boshlanishiga {farq.days} kunu {soatlar} soat qoldi.")

# ! MASHQ
# ? Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani konsolga chiqaring
bugun = dt.date.today()
kun1 = dt.date(2022, 10, 1)
kun2 = dt.date(2022, 11, 1)
kun3 = dt.date(2022, 12, 1)
kun4 = dt.date(2022, 9, 1)
kun5 = dt.date(2022, 7, 1)
kunlar = [kun1, kun2, kun3, kun4, kun5]
for kun in kunlar:
    farq = kun - bugun
    print(farq)

# ? Ramazon va qurbon hayitigacha qolgan kunlarni konsolga chiqaring
bugun = dt.date.today()
ramazon = dt.date(2022, 8, 14)
hayt = dt.date(2022, 9, 13)
farqlar = [ramazon, hayt]
for n in farqlar:
    farq = n - bugun
    print(farq)

# ? Tug'ilgan kuningizdan bugungi sanagacha qancha yil, oy, kun o'tganini qaytaruvchi funksiya yozing


def tkun(tyil):
    bugun = dt.datetime.now()
    farq = bugun - tyil
    return farq


print(tkun(dt.datetime(2002, 2, 22)))
