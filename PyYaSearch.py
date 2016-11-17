import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        assert "No results found." not in driver.page_source
        elem.send_keys(Keys.RETURN)

    def test_search_in_ya_ru(self):
        driver = self.driver
        driver.get("http://www.ya.ru")
        self.assertIn("Яндекс", driver.title)
        elem = driver.find_element_by_name("text")
        elem.send_keys("yandex")
        assert "No results found." not in driver.page_source
        elem.send_keys(Keys.RETURN)

    #def tearDown(self):
        #self.driver.close()

if __name__ == "__main__":
    unittest.main()


#I am in master branch
#I am in test_branch

print('Hohohohoho')