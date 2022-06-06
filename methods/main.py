mevalar = ["olma", "o'rik", "anor", "gilos"] #* mevalar ro'yxati str ko'rinishida.
narxlar = [12000, 18000, 20000, 22000, 25000, 36000, -25, 63.2] #* narxlar ro'yxati int korinishida.
sonlar = ["bir", "ikki", 3, 4, 5] #* int va str aqralsh ro'yxat.
print(type(sonlar))
ismlar = [] #* bo'sh royxat.

print(mevalar[0] + " " + mevalar[-1])
print(mevalar[0].upper(), '\t', mevalar[2]) #* tartib raqam 0dan boshlanadi shuning uchun elementlarni chaqirayotganda 0,1,2,3 deb chaqiramiz.
print(mevalar[-1]) #* biz elementlarni minus sonlar orqali ham chaqirishimiz mumkin yani teskarisiga:(-1)(-2)(-3)(-4)bu tartibda
print(narxlar[0] + narxlar[1]) #* Natija: 30000 | narxlar o'zgaruvchani ichidagi elementlar type: integer bo'gani uchun (+ - * /) amallarini ishlatsak bo'ladi
mevalar[0] = "nok" #* endi mevalar o'zgaruvchanidagi olma elementi nokga o'zgardi.
print(mevalar) #* Natija: ['nok', "o'rik", 'anor', 'gilos']
print(mevalar[0] == "nok") #* True

# todo  .append() Ro'yhat ichiga element qo'shish.
# todo  .append() metodi faqat ro'yxatni ohiriga element qo'shadi.

mevalar.append("nok") #* mevalar Ro'yxatiga yangi nok degan element qoshildi.
print(mevalar)
# Agar aniq bir joyga element qo'shmoqchi bolsak #! .insert(index, object) dan foydalanamiz
mevalar.insert(0, "banan")
print(mevalar) #* Natija ['banan', 'olma', "o'rik", 'anor', 'gilos', 'nok']
# * Shu tarzda istagan joyimizga element qo'shishimiz mumkin, .insert() yordamida.
# todo -del- yordamida elementlarni o'chirish.
del mevalar[0] #* banan elemanti -del- buyrug'i orqali o'chirildi.
print(mevalar) #* Natija: ['olma', "o'rik", 'anor', 'gilos', 'nok']
cars = [] #* Bo'sh Ro'yxat
cars.append("Lacetti")  #* yangi qiymat qo'shish
cars.append("Spark")    #* yangi qiymat qo'shish
cars.append("Malibu")   #* yangi qiymat qo'shish
cars.append("Tracker")  #* yangi qiymat qo'shish
print(cars)  #* Natija: ['Lacetti', 'Spark', 'Malibu', 'Tracker']

del cars[0] #* Lacetti elemanti o'chirildi -del- buyrug'i orqali
print(cars) #* Natija: ['Spark', 'Malibu', 'Tracker']

cars.insert(0, "Gentra") #* Ro'yxat boshiga Gentra
print(cars) #* Natija: ['Gentra', 'Spark', 'Malibu', 'Tracker']
del cars[1]#* endi Sparkni o'chirdik.

print(cars)#* Natija: ['Gentra', 'Malibu', 'Tracker']
# todo .remove()
cars.remove("Malibu")   # todo .remove() yordamida elementni nomini yozgan holda o'chirishimiz mumkin.
print(cars) #* Natija: ['Gentra', 'Tracker']

hayvonlar = ["it", "mushuk", "sigir", "qo'y", "mushuk"]
hayvonlar.remove("mushuk") #* .remove() methodi bir hil so'zlar ko'p bo'lsa faqat birinchi uchraganini o'chiradi.
print(hayvonlar) #* Natija: ['it', 'sigir', "qo'y", 'mushuk'] >>> Birinchi mushuk o'chib ketti.
# todo .pop() orqali istagan elementini sug'urib olsak bo'ladi.
bozorlik = ["yog'", "un", "piyoz", "banan", "go'sht"] #* Ro'yxat yaratildi
print(bozorlik) #* Natija: ["yog'", 'un', 'piyoz', 'banan', 'gosht']
mahsulot = bozorlik.pop(1) #* mahsulot degan yangi o'zgaruvchi ichiga .pop() methodi orqali 2chi elementini sug'urib oldik.
print(mahsulot) #* Natija: un.
print(bozorlik) #* Natija: ["yog'", 'piyoz', 'banan', 'gosht'] >>> endi ro'yxatda un yo'q.
i = [12, 2, 4, 45, 60]
h = i.pop(2)
print(h)
print(i)
# ? Masalan kichik bir dastur:
bozorlik = ["yog'", "un", "piyoz", "banan", "gosht"]
mahsulot = bozorlik.pop(2)
print("Men", mahsulot, "sotib oldim.")
print("Yana", bozorlik, "larni sotib olishim kerak.")
# *shu kabi dasturlarda ishlatsak bo'ladi.
#
# ?  .append() methodi orqali ro'yhat ichiga element qo'shish.
# ! Masalan: o'zgaruvchan.append("nok") #* o'zgaruvchan Ro'yxatiga yangi nok degan element qoshildi.
# //
# ?  .insert(index, object) methodi orqali aniq bir joyga element qo'shishimiz mumkin.
# ! Masalan: o'zgaruvchan.index(0, "banan") #* o'zgaruvchan Ro'yxatiga yangi banan degan element boshiga qo'shildi.
# //
# todo -del- yordamida elementlarni o'chirish.
# ! Masalan: del o'zgaruvchan[0] #* -del- buyrug'i orqali birinchi elemanti o'chirildi.
# //
# ? .remove() methodi orqali elementni nomini yozgan holda o'chirishimiz mumkin.
# ! Masalan: o'zgaruvchan.remove("element") #* .remove() yordamida elementni nomini yozgan holda o'chirishimiz mumkin.
# //
# ? .pop()  methodi orqali biron elementni ro'yxatdan sug'urib olishimiz mumkin.
# ! Masalan: o'zgaruvchan = o'zgaruvchan2.pop(1) #* mahsulot degan yangi o'zgaruvchi ichiga .pop() methodi orqali 2chi elementini sug'urib oldik.
# * Agar o'zgaruvchan.pop() deb bo'sh qoldirsak Ro'yxat oxiridagi elementni sug'urib oladi.
# //
# ? a[0] = a[0] + 1 #* o'zgaruvchan type integer bolsa shu amal orqali qiymatga 1 qo'shdik.
# ! Masalan: o'zgaruvchan[0] = o'zgaruvchan[0] + 2000 #* o'zgaruvchanning qiymatiga  2000 qo'shildi.