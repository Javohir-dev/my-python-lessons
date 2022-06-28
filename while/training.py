
# ! 01
print("\n🚫Agar dasturni tohtatmoqchi bo'sangiz 'stop' deb yozing.")
search = "Qaysi kitoblarni o'qigansiz?\n>>>"
books = []

while True:
    get = input(search)
    get = get.strip()
    if get == 'stop':
        print("Dastur tugadi.")
        break
    elif get != 'stop':
        books.append(get)

print(f"\nSizning manabu {len(books)}ta kitob o'qigan ekansiz.")
num = len(books)

if num >= 2:
    for book in books:
        print(f"\n{book.title()}")

# ! 02
enter = 'yoshingizni kiriting chipta narxini aytaman:\n>>>'
k = "sizga kirish"
summa = 0

while True:
    age = input(enter)
    age = age.strip()
    if age:
        age = age.lower()
        if age == 'exit' or age == 'quit':
            break
        elif age != 'exit' or age != 'quit':
            yosh = int(age)
            if yosh <= 7:
                print(f"{k} 2000 so'm")
                summa += 2000

            elif yosh > 7 and yosh <= 18:
                print(f"{k} 3000 so'm")
                summa += 3000

            elif yosh <= 65:
                print(f"{k} 10000 so'm")
                summa += 10000

            elif yosh > 65:
                print(f"{k} bepul")
    else:
        print("\n🚫Xabarni bo'sh jo'natmang.\n")

print(f"Sizdan {summa} so'm bo'ldi.")
# ! 03
savol = "\nKiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "\nMusbat son kiriting"
savol += "(🚫Dasturni to'xtatish uchun 'exit' deb yozing):\n>>>"


while True:
    qiymat = input(savol)
    if qiymat and qiymat != 'exit':
        ildiz = float(qiymat) ** 0.5
        if ildiz <= 0:
            continue
        elif ildiz > 0:
            print(f"{qiymat}ning ildizi {ildiz}ga teng.")
    elif qiymat == 'exit':
        break
    else:
        print("Notog'ri malumot kiritdingiz.")

