import time

from django.test import LiveServerTestCase
from selenium import webdriver


class EmployerTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome()
        super(EmployerTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(EmployerTestCase, self).tearDown()

    def test_login_admin(self):
        try:
            selenium = self.selenium
            selenium.get('http://127.0.0.1:8000/accounts/login/')

            input_email = selenium.find_element_by_id('id_username')
            input_email.send_keys('arthur-admin@gmail.com')

            input_password = selenium.find_element_by_id('id_password')
            input_password.send_keys('arthur-admin-password')

            login_click = selenium.find_element_by_id('submit-id-sign_in')
            login_click.click()

            find_admin = selenium.find_element_by_xpath('//li[contains(text(), "admin")]')
            assert find_admin != True
        finally:
            selenium.quit()

    def test_employer(self):
        try:
            selenium = self.selenium
            selenium.get('http://127.0.0.1:8000/employer/')
            find_link = selenium.find_element_by_class_name('container-fluid a')
            find_link.click()
            find_text = selenium.find_element_by_tag_name('h2')
            assert "Please Log In" != find_text
            time.sleep(5)
        finally:
            selenium.quit()





