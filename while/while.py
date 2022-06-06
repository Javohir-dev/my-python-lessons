
# # ! input()
# ism = input("ismingiz nima?\n>>> ")
# savol = f"Salom {ism.title()}, yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh)
# height = input(f"{ism.title()} Bo'yingiz necha metr? ")
# height = float(height)

# # ! while()
# son = 1
# while son <= 5:
#     print(son, end=' ')
#     son += 1  # bu code #? son = son + 1 degani
# print("Dastur tugadi.")

# print("Kiritilgan sonni kvadratini qaytaruvchi dastur.")
# savol = 'istagan son kiriting '
# savol += "( Dasturni toxtatish uchun 'exit' kamandasini yozing) : "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat) ** 2)
# print("\nDastur tugadi.\n")


# print("Kiritilgan sonni kvadratini qaytaruvchi dastur.")
# savol = 'istagan son kiriting '
# savol += "( Dasturni toxtatish uchun 'exit' kamandasini yozing) : "
# qiymat = ''
# ishora = True

# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat) ** 2)
# print("\nDastur tugadi.\n")


# print("Kiritilgan sonni kvadratini qaytaruvchi dastur.")
# savol = 'istagan son kiriting '
# savol += "( Dasturni toxtatish uchun 'exit' kamandasini yozing) : "
# qiymat = ''
# # ? brake while:
# while True: # abadiy tsik   l
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break # tsikl toxtatish
#     else:
#         print(float(qiymat) ** 2)
# print("\nDastur tugadi.\n")

# ? while continue:
# son = 0
# while son <= 10:
#     son += 1
#     if son % 2 != 0: # '!=' o'rniga '==' ni qoysan consolega toq sonlar chiqadi
#         continue
#     elif son % 2 >= 0:
#         print(son)

# # ? break for:
# sonlar = range(1, 11)
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son}ning kvadrati {son ** 2} ga teng")

# # ? continue for:
# sonlar = range(1, 11)
# for son in sonlar:
#     if son == 5:
#         continue # continue yordamida 1qadan tashlab otadi.
#     print(f"{son}ning kvadrati {son ** 2} ga teng")
