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

filename = 'data/talaba.txt'

with open(filename) as file:
    for line in file:
        print(line)

# bu amal har bir qatorni alohida element qilib ro'yxatga joylaydi
with open(filename) as file:
    talabalar = file.readlines()

#print(talabalar)
