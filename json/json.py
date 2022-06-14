import json

x = 10
x_json = json.dumps(x)

y = 5.5
y_json = json.dumps(y)

m = True
m_json = json.dumps(m)

# ism = "anvar"
# ism_json = json.dumps(ism)
# familiya_json = json.dumps('narzullaev')

sonlar = (12, 45, 23, 67)
sonlar_json = json.dumps(sonlar)


bemor = {
    "ism": "Alijon Valiyev",
    "yosh": 30,
    "oila": True,
    "farzandlar": ("Ahmad", "Bonu"),
    "allergiya": None,
    "dorilar": [
        {"nomi": "Analgin", "miqdori": 0.5},
        {"nomi": "Panadol", "miqdori": 1.2},
    ],
}
# ? jsonga ma'lumot kiritish
bemor_json = json.dumps(bemor, indent=2)
print(bemor_json)

# ? filega saqlash uchun endi `dumps` emas `dump` dan foydalanamiz
with open("bemor.json", "w") as f:
    json.dump(bemor, f)

# ? jsondan pythonga olish
bemor2 = json.loads(bemor_json)
