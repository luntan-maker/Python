import selenium as sel
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class Cookie_interface:
    def __init__(self):
        self.get_cookie_driver()
        self.wait_for_loader()
        self.get_the_cookie()
#         self.click_cookie_and_update()
    def get_cookie_driver(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwj4vZWAibjqAhWToFsKHY--AZ8QFjAAegQIARAC&url=https%3A%2F%2Forteil.dashnet.org%2Fcookieclicker%2F&usg=AOvVaw3UTcOEzFj4fmnJ6O5GKFnm")
    def wait_for_loader(self):
        wait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH,"//div[@id='loader']")))
    def get_the_cookie(self):
        self.the_Cookie = wait(self.driver, 5).until(EC.element_to_be_clickable((By.ID,"bigCookie")))
    def cookie_counter(self):
        cookie_number = self.driver.find_element_by_id("cookies")
        self.cookie_count = int(cookie_number.text.split(" cookie")[0])
    def click_cookie_and_update(self):
        self.the_Cookie.click()
        self.cookie_counter()
        
