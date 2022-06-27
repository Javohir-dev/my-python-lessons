import math

PI = math.pi
print(f"PI ning qiymati {PI}")
E = math.e
print(f"E ning qiymati {E}")

# Trigonometriya
math.sin(math.pi/2)
math.cos(0)
math.tan(PI)

# radianlar va burchaklar o'rtasida konvertasiya
print(math.degrees(math.pi/2))
print(math.radians(90))

# logarifmlar
# natural logarifmlar
math.log(5)
# 10 asosli logarifmlar
math.log10(100)

# sonlarni yaxlitlash
x = 4.6
print(math.ceil(x))
# tepaga butun songa yaqinlashtiradi
print(math.floor(x))
# pastki butun songa yaqinlashtiradi

# kvartal ildiz
x = 81
ildiz = math.sqrt(x)
print(f"{x} ning ildizi {ildiz} ga teng.")

# Darajaga oshirish
math.pow(x, 3)  # kubi
math.pow(x, 5)  # 5 - darajasi
math.pow(x, 1/3)  # kub ildizi

