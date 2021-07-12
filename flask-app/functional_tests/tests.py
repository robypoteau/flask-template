from selenium import webdriver
import unittest


class ExampleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.FirefoxOptions()
        options.add_argument('headless')
        try:
            cls.browser = webdriver.Firefox(options=options)
        except Exception as e:
            e

    def test_title(self):
        browser = self.__class__.browser
        if browser:
            browser.get('http://localhost:5000')
            assert 'Bare Bootstrap Template' in browser.title

    @classmethod
    def tearDownClass(cls):
        if cls.browser:
            cls.browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
