car_0 = {'model':'bmw', 'color':'blue'}
print(car_0['model'])
print(car_0['color'])

en_uz = {'color':'rang', 'car':'mashina', 'apple':'olma', 'home':'uy', 'banana':'banan'}
print(en_uz[input('englizcha so\'zkiriting\n>>> ')])

fruits = {'apple':12000, 'apricot':9500, 'watermelon':25000}
fruit = fruits[input('which fruit? ')]
print(f"narxi: {fruit}")

student = {'name':'xamidullayev javohr', 'age':20, 'year':2002}
# ?  \<<<back slash orqali yandi qator yaratdim.
print(f"{student['name'].title()}, \
{student['year']}-yilda tug'ilgan, \
{student['age']} yoshda")

# * yangi lug'at qo'shish:
student['kurs'] = 3
student['fakultet'] = 'informatika'
student['ism'] = 'javohir'

# * lug'at o'zgartirish:
student['ism'] = 'abduvahob'
print(student) #* Natija:{'name': 'xamidullayev javohr', 'age': 20, 'year': 2002, 'kurs': 3, 'fakultet': 'informatika', 'ism': 'abduvahob'}

#* bo'sh lug'at bilan ishlash
null = {}
null['ism'] = 'javohir'
null['kurs'] = 3
null['yosh'] = 20
print(f"{null['ism'].title()}, {null['kurs']}-kurs, {null['yosh']} yoshda.")

# * Ma'lumotni yangilaymiz.
null['kurs'] = 4
null['yosh'] = 21
print(f"Talabaning ismi {null['ism'].title()}, {null['kurs']}-kursga o'tdi, {null['yosh']} yoshda.")

# * Lug'atda elementni o'chirish:
student = {'name':'xamidullayev javohr', 'age':20, 'year':2002}
del student['age']
print(student)

phones = {
    'ali':'IPhone X',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'javohir':'galaxy note 10+'
}
print(phones)

# * get() metodi
phone = phones.get('husan', 'Bunday ism mavjud emas.')
print(phone) #* Natija: Bunday ism mavjud emas.

phone = phones.get('husan')
print(phone) #* Natija: None
# ! Mashg'ulot:
# ? 1-Mashg'ulot

otam = {
    'ism':'azimjon',
    'yosh':51,
    'yil':1971,
    'kasb':'sotuvchi'}
print(f"\nBu mening otam, ismlari {otam['ism'].title()}, \
{otam['yil']}-yilda tug'ilganlar, \
yoshlari {otam['yosh']} da, ")

onam = {
    'ism':'nargiza',
    'yosh':48,
    'yil':1974,
    'kasb':'uy bekasi'}
print(f"\nBu mening onam, ismlari {onam['ism'].title()}, \
{onam['yil']}-yilda tug'ilganlar, \
yoshlari {onam['yosh']} da, ")

akam = {
    'ism':'jahongir',
    'yosh':28,
    'yil':1994,
    'kasb':'sotuvchi'}
print(f"\nBu mening akam, ismlari {akam['ism'].title()}, \
{akam['yil']}-yilda tug'ilganlar, \
yoshlari {akam['yosh']} da, ")

# ? 2-Mashg'ulot
taomlar = {
    'vali':'osh',
    'ali':'shashlik',
    'husan':'sho\'rva',
    'hasan':'qozonkabop',
    'men':'moshxorda'
}
name = input('Kimning sevimli taomi kerak?>>> ')
print(f"{name.title()}ning sevimli taomi {taomlar[name]}")

# ? 3-Mashg'ulot
keys = {
    'intager':'intager butun son',
    'float':'float o\'nlik sonlar',
    'boolean':'True va False',
    'string':'string matnlar',
    'list':'ro\'yhatlar',
    'tuple':'o\'zgarmaslar'
}
key = input('bitta type yozing\n>>> ')
print(f"{keys[key]}")

# ? 4-Mashg'ulot
types = {
    'intager':'intager so\'zi butun son deb tarjima qilinadi.',
    'float':'float so\'zi o\'nlik son deb tarjima qilinadi.',
    'boolean':'boolean so\'zi True va Falseni anglatadi.',
    'string':'string matn deb tarjima qilinadi.',
    'list':'list so\'zi ro\'yhat deb tarjima qilinadi.',
    'tuple':'tuple so\'zi o\'zgarmas deb tarjima qilinadi.'
}
i = input('bitta type yozing\n>>> ')
print(f"{types[i]}")

# ? 5-Mashg'ulot
types = {
    'intager': 'intager so\'zi butun son deb tarjima qilinadi.',
    'float': 'float so\'zi o\'nlik son deb tarjima qilinadi.',
    'boolean': 'boolean so\'zi True va Falseni anglatadi.',
    'string': 'string matn deb tarjima qilinadi.',
    'list': 'list so\'zi ro\'yhat deb tarjima qilinadi.',
    'tuple': 'tuple so\'zi o\'zgarmas deb tarjima qilinadi.'
}
i = input('bitta type yozing:\n>>> ').lower()
aniq = types.get(i)
if aniq == None:
    print('Bunday qiymat yo\'q.')
else:
    print(types[i])