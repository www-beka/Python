# def my_function():
#     return 2 + 2

# assert my_function() == 5


# import unittest
# from typing import Union
# from typing import assert_never

# def handle_value(value: Union[int, str, float]):
#     if isinstance(value, int):
#         print('Handling value of type int')
#     elif isinstance(value, str):
#         print('Handling value of type str')
#     elif isinstance(value, float):
#         print('Handling value of type float')
#     else:
#         assert_never(value)

# handle_value(12)

# class Test(unittest.TestCase):

#     def setUp(self):
#         self.variable = 1
#     def tearDown(self):
#         self.variable = None

#     def test_2(self):
#         self.assertNotEqual(1,2)
    
#     def test_3(self):
#         self.assertTrue(True)
    
#     def test_4(self):
#         self.assertFalse(False)
    
#     def test_5(self):
#         self.assertIs(1, 1)

#     def test_6(self):
#         self.assertIsNone(None)
    
#     def test_7(self):
#         self.assertIn(1, [1,2,3])
    
#     def test_8(self):
#         self.assertIsInstance(1, int)


import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PATH = 'C:\\Users\\user\\Desktop\\ALL\\Full-stack\\Back-end\\Python\\Python\\Retake_py\\Lessons\\chromedriver.exe'

HALF_SECOND = 0.5



class Fullstack(unittest.TestCase):
    def setUp(self) -> None:
        options = Options()
        self.driver = webdriver.Chrome(service=Service(PATH), options=options)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()
        print(f'Ending test for {self.driver}')
    
    def test_login_to_facebook(self):
        self.driver.get("https://www.facebook.com/")
        print("Getting url...")
        btn_register = self.driver.find_element(By.LINK_TEXT, 'Создать новый аккаунт') 
        btn_register.click()
        time.sleep(HALF_SECOND*2)
        
        firstname = self.driver.find_element(By.NAME, "firstname")
        lastname = self.driver.find_element(By.NAME, "lastname")
        email = self.driver.find_element(By.NAME, "reg_email__")
        password = self.driver.find_element(By.NAME, "reg_passwd__")
        submit = self.driver.find_element(By.NAME, "websubmit")
        # sex = self.driver.find_element(By.LINK_TEXT, "Мужчина")

        write_firstname = 'Bekzod'
        write_lastname = 'Bekmuradov'
        write_email = 'example@example.com'
        write_password = '3132131231312'

        firstname.send_keys(write_firstname)
        time.sleep(HALF_SECOND*2)
        lastname.send_keys(write_lastname)
        time.sleep(HALF_SECOND*2)
        email.send_keys(write_email)
        time.sleep(HALF_SECOND*2)
        password.send_keys(write_password)
        time.sleep(HALF_SECOND*2)
        submit.click()
        time.sleep(HALF_SECOND*3)
        assert "Введите " in self.driver.page_source

        # emali_url = self.driver.find_element(By.ID, "email")
        # pass_url = self.driver.find_element(By.ID, "pass")
        # btn_login = self.driver.find_element(By.ID, 'loginbutton')
        # time.sleep(HALF_SECOND*5)
        # text_email = 'email@example.com'
        # text_password = 'password@example.com'

        # emali_url.send_keys(text_email)
        # pass_url.send_keys(text_password)

        # btn_login.click()
        # time.sleep(HALF_SECOND*5)

        #! birthday_year = self.driver.find_element(By.XPATH, 'input[value=birthday_year]')

        
        
    
    # def test_wikipedia(self):
    #     self.driver.get("https://www.wikipedia.org/")
    #     print("Getting url...")
    #     slogan = self.driver.find_element(By.CLASS_NAME, "localized-slogan")
    #     print(slogan)
    #     print("ID: -> ", slogan.get_property("id"))
    #     print("link.text: -> ", slogan.text)

    #     text_to_write = "FullStack programming"
    #     search_input = self.driver.find_element(By.ID, "searchInput")
    #     search_input.send_keys(text_to_write)
    #     time.sleep(HALF_SECOND)
    #     btn = self.driver.find_element(By.CLASS_NAME, "svg-search-icon")
    #     btn.click()
    #     time.sleep(HALF_SECOND*2)
    #     expected_heading = self.driver.find_element(By.ID, "firstHeading")
    #     assert expected_heading.text == "Search results"
    #     assert "Search results" in self.driver.page_source