# ? Lug'at binal ishlash.
# * .items()
studen = {
    'name': 'javohir',
    'surname': 'khamidullaev',
    'age': 22,
    'faculty': 'matematika',
    'course': 4
}
print(studen.items())
for key, value in studen.items():
    print(f"Key: {key}")
    print(f"Value: {value}\n")

phones = {
    'ali': 'IPhone X',
    'vali': 'galaxy s9',
    'olim': 'mi 10 pro',
    'javohir': 'galaxy note 10+'
}
for key, value in phones.items():
    print(f"\n{key.title()}ning telefoni {value}")
# * keys()

products = {
    'apple': 15000,
    'pomegranate': 17000,
    'grapes': 25000,
    'fig': 13000,
    'peach': 36000
}
print(products.keys())
print("Products in the store")
for product in products.keys():
    print(product.title())
# * Pastagidek yozsa ham bo'ladi.
print("Products in the store")
for product in products:
    print(product.title())

bozorlik = ['pomegranate', 'grapes', 'bread', 'fish']
print("Bizning do'konimizda.")
for product in products:
    if product in bozorlik:
        print(f"{product.title()} {products[product]} so'm.")

bozorlik = ['pomegranate', 'grapes', 'bread', 'fish']
print("Bizning do'konimizda.")
for item in bozorlik:
    if item not in products:
        print(f"Iltimos, Do'koningizga {item} ham olib keling.")

print("Bizning do'konimizda.")
for product in sorted(products):
    print(product.title())

# * values()
phones = {
    'ali': 'iphone x',
    'vali': 'galaxy s9',
    'olim': 'iphone x',
    'javohir': 'galaxy note 10+',
    'farxod': 'iphone 8 plus',
    'alisher': 'galaxy s21 ultra',
    'sherzod': 'iphone 8 plus',
    'azamat': 'galaxy s21 ultra',
    'bunyod': 'iphone 8 plus'
}
print(phones.values())
for phone in phones.values():
    if phone == 'iphone x':
        print("IPhone X")
    else:
        print(phone.title())

# ? set()
print("Foydalanuvchilarni telefon turlari:")
for tel in set(phones.values()):
    print(tel)

# * set() ham ma'lumot turi 
# ? set() yaratish:
toys = {'ball', 'car', 'lamp', 'ball'}
print(type(toys))