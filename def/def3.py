def bahola(ismlar):
    """Talabani baholaydigan funksiya"""
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosi: ")
        baholar[ism] = int(baho)
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)
"""
! tepadagi funksiya asil 'talabalar' RO'YHATINI ichidan talabalar ismini
! sug'urib oladi shuning uchun pastdagi amalni qollab
! ro'yhatni asl holidak saqlab qolishimiz mumkin.
"""


# def bahola(ismlar):
#     """Talabani baholaydigan funksiya"""
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosi")
#         baholar[ism] = int(baho)
#     return baholar


# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar[:])  # ! [:] orqali ro'yhatdan bir nusxa olamiz
# print(baholar)
# print(talabalar)


# ! mashg'ulot
# def bahola(name):
#     """
#     Bu funksiya talabararni baholarini qo'yish uchun ishlaydi.
#     Yani online jurnalga o'xshash
#     """
#     baholar = {}
#     while name:
#         print("salom")
