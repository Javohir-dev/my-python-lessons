from turtle import circle
import unittest
from circle import getArea, getPerimeter


# ? Hozir unittest classidan meros oldi va ichidan TestCase methodini oldi
class CircleTest(unittest.TestCase):
    def test_area(self):
        # ! assertAlmostEqual nuqtadan kegin 7ta son aniqlikkacha tekchiradi
        self.assertAlmostEqual(getArea(5), 78.53975, 3)
        self.assertAlmostEqual(getArea(10), 314.159)
        # nuqtadan kegin ,3 hona tekshir

    def test_peremetr(self):
        self.assertAlmostEqual(getPerimeter(10), 62.8318)
        self.assertAlmostEqual(getPerimeter(4), 25.13272)
        # * assertAlmostEqual sozi deyarli teng bo'sa Ok chiqadi asosan matematik masalalarda ishlatiladi.


unittest.main()

# ! qolgan `assertAlmostEqual`ga o'xshash methodlar uchun havola https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa1NXNFBwUUFrOS12OFRVMGJHdHlfejFuYzhSd3xBQ3Jtc0trakgzd1k2a2VjVDBqVWVLaHQxVG9raVJINnJtTGU4SElvQzE0ZThfVEJxblNaN2lCVk5HLXh0YTljUGFTUFI3bjJyX1lCTmFFVVl0MHlOUXdOMF9oWDJhdmtsZ1lsZXBqLUZ5a1pobjZsQVM4eGgzYw&q=https%3A%2F%2Fpython.sariq.dev%2Ftesting%2F36-function-test&v=GgAs_VhWucY
