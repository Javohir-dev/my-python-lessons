cars = ["bmw", "mercedes benz", "audi", "volvo", "tayota"] #* Ro'yxat yaratildi.
cars.sort()#* cars.sort() orqali ro'yxat ichidagi elementlarni alifbo tartibida taxladik.
print(cars) #* Natija: ['audi', 'bmw', 'mercedes benz', 'tayota', 'volvo']

cars = ["bmw", "mercedes benz", "audi", "volvo", "tayota"] #* Ro'yxat yaratildi.
cars.sort(reverse = True) #* .sort() mathodi ichiga --reverse-- argumentini kiritish orqali teskari taxlashimiz mumkin.
print(cars) #* Natija: ['volvo', 'tayota', 'mercedes benz', 'bmw', 'audi']

# todo >>> Agar ro'yxatga tegmagan holda o'zgartirish talab qilinsa sorted() funsiyasidan foydalanamiz.
mevalar = ['olma', 'banan', 'anor', 'shaftoli', 'gilos'] #* Ro'yxat yaratildi.
print(sorted(mevalar)) #* Natija: ['anor', 'banan', 'gilos', 'olma', 'shaftoli']
print(mevalar) #* Natija: ['olma', 'banan', 'anor', 'shaftoli', 'gilos']
# todo >>> sorted() ichida --reverse-- dan foydalansak ham bo'ladi.
print(sorted(mevalar, reverse=True)) #* Natija: ['shaftoli', 'olma', 'gilos', 'banan', 'anor']
# SONLAR:
sonlar = [12, 45, 23, 56, 998, 1, 0, -5, -7.2] #* Ro'yxat yaratildi.
print(sorted(sonlar)) #* Natija: [-7.2, -5, 0, 1, 12, 23, 45, 56, 998]
mevalar = ['olma', 'banan', 'anor', 'shaftoli', 'gilos'] #* Ro'yxat yaratildi.
mevalar.reverse() #* .reverse() orqali ro'yxatni teskari tarzda taxladik.
print(mevalar) #* Natija: ['gilos', 'shaftoli', 'anor', 'banan', 'olma']

mevalar = ['olma', 'banan', 'anor', 'shaftoli', 'gilos'] #* Ro'yxat yaratildi.
print(len(mevalar)) #* Natija: 5

numbers = [] #* Bo'sh ro'yxat yaratildi.
print(numbers) #* Natija: []
numbers = list(range(0,10))
print(numbers) #* Natija: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

toq_sonlar = list(range(1, 20, 2))
print(toq_sonlar) #* Natija: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

juft_sonlar = list(range(0, 20, 2))
print(juft_sonlar) #* Natija: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

sanash = list(range(0, 101, 10))
print(sanash) #* Natija: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

max_qiymat = max(toq_sonlar)
print(max_qiymat) #* Natija: 19

narxlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
print(narxlar) #* Natija:[12000, 22500, 23456, 9800, 5600, 9934, 32874]
print(max(narxlar)) #* Natija: 32874 yani eng katta qiymat
print(min(narxlar)) #* Natija: 5600 yani eng kichik qiymat
print(sum(narxlar)) #* Natija: 116164 yani o'zgaruvchan ichidagi barcha qiymatlar yig'indisini chiqarib beradi.
print(narxlar[0:3]) #* Natija: [12000, 22500, 23456]

mevalar = ['olma', 'banan', 'anor', 'shaftoli', 'gilos'] #* Ro'yxat yaratildi.
# endi undan nusha olamiz
my_fruits = mevalar[:] #* qiymat tartib raqamini bermasdan mevalar ro'yxatidan nusxa oldik.
my_fruits.remove('olma') # 'olmani o'chirdik.
print(my_fruits) #* Natija: ['banan', 'anor', 'shaftoli', 'gilos']
print(mevalar) #* Natija: ['olma', 'banan', 'anor', 'shaftoli', 'gilos']

toys = ('car', 'bus', 'moto', 'snake', 'lizard', 'dino')
print(toys) #* Natija: ('car', 'bus', 'moto', 'snake', 'lizard', 'dino')
toys = list(toys)
print(toys)
# //
# todo>>>  --a.sort()-- va a.sort(reverse=True)
# //
# ? --.sort()-- orqali ro'yxat ichidagi elementlarni alifbo tartibida taxlash mumkin.
# * --.sort()-- taxlayotganda avval katta harflarni keyin kichik harflarni taxlardi. a.sort() Natija: ['D', 'a', 'b']>>> shunday
# ! Masalan: o'zgaruvchan.sort() Natija: ['a', 'b', 'd']
# //
# ? .sort() mathodi ichiga --reverse-- argumentini kiritish orqali teskari taxlashimiz mumkin.
# * reverse => teskarisiga.
# ! Masalan: o'zgaruvchan.sort(reverse=True) Natija: ['d', 'b', 'a']
# //
# todo>>> print(sorted(a)) , print(sorted(a, reverse=True))
# //
# ? Agar ro'yxatga tegmagan holda o'zgartirish talab qilinsa sorted() funsiyasidan foydalanamiz.
# * sorted() funksiyasidan foydalanganimizda asosiy ro'yxat o'zgarmaydi shunchaki tartiblab ko'rsatadi.
# * --reverse-- ni ham ishlatsak bo'ladi.
# ! Masalan: print(sorted(a, reverse=True)) Natija: ['d', 'b', 'a']
# //
# ! ro'yxatni tartiplamagan holda teskari tarzda taxlash.
# * a.reverse() bu holda royhat alifbo tarzida tartiplanmaydi.
# ? a.reverse() dan foydalanib shunchaki teskari taxlashimiz mumkin.
# //
# todo>>> .len() va range()
# //
# ? len(a) funksiyasi orqali ro'yxatda nechta element borligini aniqlasa bo'ladi.
# * a = ['a', 'd', 'b', 'f', 'y'] Ro'yxat yaratildi.
# ! Masalan: print(len(a)) Natija: 5
# //
# ? o'zgaruvchan = list(range(0,10)) orqali o'zgaruvchan ichiga 0dan 10gacha bo'gan sonlarni kirittik.
# * range() dan foydalanganimizda a = list(range(0,10)) .0dan 10gacha sonlar chiqadi 10ning o'zi chiqmaydi.
# ! Masalan: o'zgaruvchan = list(range(0,10)) Natija: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# //
# ? list(range(1,2,3)) 1 = boshlang'ich qiymat| 2 = oxirgi qiymat| 3 = qadmalar.
# * Birinchi sanoq nechidan boshlanishi kerakligi, Ikkinchinechigacha bo'lishi va Uchinchisi qadamlarni bildirgan holda funsiya ishlaydi.
# ! Masalan: sanash = list(range(0, 101, 10)) Natija: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# //
# todo>>> max(), min() va sum()
# //
# ? max() funsiyasi orqali biz ro'yxatda bor sonlarning eng kattasini aniqlashimuz mumkin.
# * "a" o'zgaruvchaniga "b" o'zgaruvchanining ichidagi eng katta qiymatni saqlaydik.
# ! Masalan: a = max(b) Natija: 99
# ==
# ? min() funsiyasi orqali biz ro'yxatda bor sonlarning eng kichkinasini aniqlashimuz mumkin.
# * "a" o'zgaruvchaniga "b" o'zgaruvchanining ichidagi eng kichik qiymatni saqlaydik.
# ! Masalan: a = min(b) Natija: 1
# //
# ? sum() funksiyasi o'zgaruvchan ichidagi barcha qiymatlar yig'indisini chiqarib beradi.
# ! Masalan: print(sum(a)) Natija: 1648542
# //
# todo>>> qiymatlarni ajratish
# ? qiymatlar ichidan ajratib olish
# * bu ham 0-1-2-chiymatlarni chiqarib beradi "3" chiqmaydi.
# * Agar print(:3) desak yozilmagan son o'rniga eng boshi yaniy 0-qiymatni beradi.
# * Agar print(1:) desak yozilmagan son o'rniga eng oxirgi qiymatni beradi.
# ! Masalan: print(a[0:3]) Natija: [0-qiymat, 1-qiymat, 2-qiymat]
# //
# todo>>> Ro'yxatdan nusha olish.
# ? a = b[:] ikki nuqta qoyamiz holos nusha kochirildi.
# * a = b nusha olindi <<< BU XATO "EROR"
# ! mevalar = ['olma', 'banan', 'anor', 'shaftoli', 'gilos'] >>> Ro'yxat yaratildi.
# ! endi undan nusha olamiz
# ! my_fruits = mevalar[:] >>> qiymat tartib raqamini bermasdan mevalar ro'yxatidan nusxa oldik.
# ! my_fruits.remove('olma') >>> 'olmani o'chirdik.
# ! print(my_fruits) >>> Natija: ['banan', 'anor', 'shaftoli', 'gilos']
# //
# todo>>> TUPLE lar yani o'zgarmas ro'yhatlar.
# ? TUPLE bu o'zgarmas ro'yxat bu oddiy ro'yhat bilan bir hil ishlaydi faqat qiymatlarni o'zgartirib bo'lmaydi.
# * Faqat a = list(a) orqali uni typeini listga o'zgartirib olsak kegin uni ustida o'chirish, qo'shish, o'zgartirish amallarini bajarsak boladi.
# ! Maslan: a = ('car', 'bus', 'moto', 'snake', 'lizard', 'dino') tuple yaratildi.