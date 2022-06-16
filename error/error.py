# # ! try:1 except:0
# # ! xatolar bilan ishlash
# yosh = input("Yoshingizni kiriting: ")
# try:
#     """Agar xato chiqmasa"""
#     yosh = int(yosh)
#     print(f"Siz {2022 - yosh}-yilda tug'ilgansiz")
# except:
#     """Agar xato chiqqanda"""
#     print("\n!Siz butun son kiritmadingiz\n")

# #! dastur toxtab qolmasligi uchun

# while True:
#     """Lekin bunday qilish to'g'ri emas"""
#     yosh = input("Yoshingizni kiriting: ")
#     try:
#         yosh = int(yosh)
#         print(f"Siz {2022 - yosh}-yilda tug'ilgansiz")
#         break
#     except:
#         print("siz butun son kiritmadingiz")

# print("Dastur davom etayapti")
# print("Dastur tugadi")

# while True:
#     """Aslida ana shunday else: bilan yozish kerak"""
#     yosh = input("Yoshingizni kiriting: ")
#     try:
#         """Agar xato chiqmasa"""
#         yosh = int(yosh)
#     except ValueError:  # ? yani Qiymat xatosi
#         """Agar xato chiqqanda"""
#         print("siz butun son kiritmadingiz")
#     else:
#         print(f"Siz {2022 - yosh}-yilda tug'ilgansiz")
#         break

# # ! ZeroDivisionError
# x, y, = 5, 10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print(f"{y}ni 0ga bo'lish mumkin emas.")

# # ! IndexError
# mevalar = ["olma", "anor", "anjir", "uzum"]
# try:
#     print(mevalar[7])
# except IndexError:
#     print(f"Royxatda {len(mevalar)} ta meva bor xolos.")

# # ! KeyError
# user = {"username": "javohir.coder",
#         "status": "admin",
#         "email": "coderjek@gmail.com",
#         "phone": "+998885394422"}

# key = 'tel'
# try:
#     print(f"Foydalanuvchi: {user[key]}")
# except KeyError:
#     print(f"{key} bunday kalitv mavjud emas!")


# # ! FileNotFoundError
# import json
# filename = "data.txt"  # bunday file mavjud emas
# try:
#     with open(filename) as f:
#         text = f.read()
# except FileNotFoundError:
#     print("Bunday file mavjud emas!")

# # ! MISOL UCHUN:
# import json
# files = ['talaba1.json', 'talaba2.json', 'talaba3.json', 'talaba4.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)
#     except FileNotFoundError:
#         # print("xato")
#         """agar ^^ chiqishi kerak bolmasa pass yozish kerak"""
#         pass
#     else:
#         print(talaba['ism'])
#         # file ustida turli amallar

# # ! Biz exceptlardan birnechta yozishimiz mumkin
# while True:
#     n = input("Butun son kiriting: ")
#     try:
#         n = int(n)
#         x = 20 / n
#     except ValueError:  # agar user butun son kiritmasa
#         print("Butun son kiritmadingiz!")
#     except ZeroDivisionError:  # agar foydalanuvchi 0 kiritsa
#         print("0 ga bo'lish mumkin emas!")
#     else:
#         print(f"x={x}")
#         break


# ! Bu tsikl da hatoni ko'rsatmasdan oldini olayapmiz
while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():  # .isdigit() methodi yosh aslida raqamlardan iboratmi shuni tekshirib beradi
        """
        '20'.isdigit()
        * >>> True
        '20.1'.isdigit()
        ! >>> False
        """
        yosh = int(yosh)
        break
    else:
        print("Siz butun son kiritmadingiz!")
print(f"Siz {2022 - yosh}-yilda tug'ilgansiz")
