# import avto_info_mod
# # ? yoki
# import avto_info_mod as aim
# avto1 = aim.avto_info('GM', 'Malibu', 'Qora', 'Avtomad', 2020, 40000)
# aim.info_print(avto1)


# # * bunday MODULNI emas modul ichidagi kerakli funksiyalarni ko'chirib olsak to'riroq bo'ladi.

# from avto_info_mod import avto_info, info_print

# avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomad', 2020, 40000)
# info_print(avto1)

# # * Alohida chaqirgan funksiyaga ham qisqa nom berishimiz mumkin

# from avto_info_mod import avto_info as ainfo, info_print as iprint

# avto1 = ainfo('GM', 'Malibu', 'Qora', 'Avtomad', 2020, 40000)
# iprint(avto1)

# # * MODULDAGI barcha funsiyalarni ham chaqirish imkoniyati bor.
# # ! Lekin bunday qilish tavsiya etilmaydi, chunki MODni ichidagi funksiya o'zgaruvchi
# # ! va boshqa narsalarni ham import qilib oladi
# # ! va bu file ichidagilar bilan aralash bolib ketadi.

from avto_info_mod import *
avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomad', 2020, 40000)
info_print(avto1)