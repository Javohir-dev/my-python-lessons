
# ! def()
def salom_ber():
    """Bu funksiya user bilan salomlashadi."""
    print("Assalomu Aleykum.")


salom_ber()


def kutvol(name):  # * (name) bu parametr deyiladi.
    """Mehmon kutadigan funksiya"""
    print(f"Assalomu aleykum {name.title()}, hush kelibsiz.")


kutvol('javohir')  # * 'javohir' endi argument deb ataladi.
kutvol('shahzod')


def funsiya(name):
    """Bu yerda funsiya haqida ma'lumotlar batafsil yoziladi."""
    print(name)


# * Natija: Bu yerda funsiya haqida ma'lumotlar batafsil yoziladi.
print(funsiya.__doc__)


def toliq_ism(name, surname):
    """
    Ikkta parametr qabul qiladigan funsiya.
    """
    print(f"Foydalanuvchi ismi {name.title()}\n"
        f"Foydalanuvchi familiyasi {surname.title()}")


toliq_ism('olim', 'hakimov')
# ? Hatolarni oldin olish uchun bunday yozsa ham bo'adi:


def malumot(age, name):
    """
    Bu yerda parametrlarga bira to'la qiymat berdik.
    """
    print(f"yoshingiz {age}, Ismingiz {name.title()}")


malumot(name='javohir', age=22)


def yosh_hisobla(tyil, joriy_yil=2022):
    """yoshni hisoblaydigan funsiya."""
    print(f"Siz {joriy_yil - tyil} yoshdasiz.")


yosh_hisobla(1994, 2020)  # * Natija: Siz 26 yoshdasiz.
# ? yoki
# * joriy_yil tepada qiymat berib ketgani uchun funksiya ishlaydi.
yosh_hisobla(1990)  # * Natija: Siz 26 yoshdasiz.
# ! Mashg'ulot:


def hisobla():
    """
    'x'ning 'y'-darajasini aniqlab beradigan funksiya.
    """
    x = int(input("butun son kiriting: "))
    y = int(input("butun son kiriting: "))
    print(f"{x} ning {y}-darajasi {x ** y} ga teng.")


hisobla()


def number(num):
    """
    Qoldiqsiz bo'linadigan sonni
    aniqlovchi funksiya.
    """
    for n in range(2, 11):
        if not num % n:
            print(f"{num} {n} ga qoldiqsiz bo'linar ekan.")
        else:
            continue


number(int(input("Son kiriting: ")))
