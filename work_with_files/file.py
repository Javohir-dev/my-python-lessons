# Bu usul ham ishlaydi lekn tavsiya etilmaydi
# fayl = open('pi.txt')
# PI = fayl.read()
# print(PI)
# fayl.close()

# ? eng avzal yo'li shu with bilanfileni oqib bo'lin yopib qoyadi
# with open('pi.txt') as fayl:
#     pi = fayl.read()

# print(pi)

# pi = pi.rstrip() # o'ng qatordagi bo'sh joylarni olib tashlaydi
# pi = pi.replace('\n', '') # '\n' ni topib ''ga almashtirayapti
# pi = float(pi) # type()ni str dan floatga o'zgartirayapti

# print(pi)

# filename = 'data/talaba.txt'

# with open(filename) as file:
#     for line in file:
#         print(line)

# # bu amal har bir qatorni alohida element qilib ro'yxatga joylaydi
# with open(filename) as file:
#     talabalar = file.readlines()

# # print(talabalar)

# talabalar = [talaba.rstrip() for talaba in talabalar]

# print(talabalar)

# # ! filega yozish
# filenomi = 'new_file.txt'
# ism = 'Olimjon Hasanov'
# tyil = 2002
# # ! 'w' << bu file nima maqsadda ochilayotganini bildiradi. 'w' bu write yani yozmoq
# # ! 'w' aslida yangi file uchun moljallangan, yani biz 'w' ni ishlatsak file ichini tozalab tashlaydi.
# # ! agar 'new_file.txt' degan file bo'lmasa yangi file yaratadi.
# with open(filenomi, 'w') as file:
#     file.write(ism + '\n')
#     file.write(str(tyil) + '\n')

# faylnomi = 'new_file.txt'
# # ! 'a' bu belgi append yani qoshishni bildiradi
# # ! file ichidagi matnlardan kegin yoziladi.
# # ! agar 'new_file.txt' bunday file yoq bolsa yaratadi.
# with open(faylnomi, 'a') as fayl:
#     fayl.write("Alijon Valiyev\n")
#     fayl.write("2000")
