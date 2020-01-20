from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
from django.urls import reverse
from datetime import datetime, timedelta
import time


class TestCalendarPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("functional_tests/chromedriver.exe")

    def tearDown(self):
        self.browser.close()

    def test_click_redirect_to_listen_music(self):
        redirect_url = self.live_server_url + reverse("music:album-list")
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id("listen-music").click()
        self.assertEqual(
            self.browser.current_url,
            redirect_url
        )

    def test_authentication_profile(self):
        login_url = self.live_server_url + reverse("users:login")
        self.browser.get(login_url)
        login = self.browser.find_element_by_name("username")
        password = self.browser.find_element_by_name("password")
        submit_btn = self.browser.find_element_by_class_name("btn-login")
        login.send_keys("test_selenium")
        password.send_keys("12345678test")
        submit_btn.send_keys(Keys.RETURN)








