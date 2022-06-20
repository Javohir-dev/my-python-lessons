import unittest
from name import get_full_name


# ? Hozir unittest classidan meros oldi va ichidan TestCase methodini oldi
class NmaeTest(unittest.TestCase):
    def test_full_name(self):
        # ^^ boshi test bilan boshlaninishi shart
        name = get_full_name('alijon', 'valiyev')
        # !tengligini taqqosla degan method
        self.assertEqual(name, 'Alijon Valiyev')

    def test_otasining_ismi(self):
        name = get_full_name('alijon', 'valiyev', 'olimovich')
        self.assertEqual(name, 'Alijon Valiyev Olimovich')


unittest.main()  # tepadagi clasni chaqiradi.
