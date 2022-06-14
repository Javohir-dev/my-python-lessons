import pickle

# ? faylga o'zgaruvchan object, funksiya, va hokazolar

talaba1 = {'ism': 'hasan', 'familiya': 'husanov', 'tyil': 2003, 'kurs': 2}
talaba2 = {'ism': 'alijon', 'familiya': 'valiyev', 'tyil': 2004, 'kurs': 1}


# ! lekin bunday qilish tavsiya qilinmaydi, aslida har bir o'zgaruvchi yoki object uchun alohida file yaratiladi uchun
with open('info', 'wb') as file:
    pickle.dump(talaba1, file)
    pickle.dump(talaba1, file)


# ! info faylini o'qish uchun kichik bir dastur

with open('info', 'rb') as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)
    
print(talaba1)
print(talaba2)
