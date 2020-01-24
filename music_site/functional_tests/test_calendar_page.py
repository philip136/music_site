from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
from django.urls import reverse
from datetime import datetime, timedelta
from django.test import Client
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile
from calendarApp.models import Calendar
from calendarApp.session_cookie import create_session_cookie
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
import time
import re


class TestCalendarPage(StaticLiveServerTestCase):

    def setUp(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("start-maximized")
        self.chrome_options.add_argument("disable-infobars")
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument('window-size=1366x768')
        self.browser = webdriver.Chrome(chrome_options=self.chrome_options,
                                        executable_path="functional_tests/chromedriver.exe"
                                        )
        self.session_cookie = create_session_cookie(
            username="test1234",
            password="test123456789test"
        )
        self.browser.get(self.live_server_url)
        self.browser.add_cookie(self.session_cookie)
        self.browser.refresh()
        self.user_id = User.objects.get(username="test1234").id

    def tearDown(self):
        self.browser.close()

    @staticmethod
    def clear_text(element):
        length = len(element.get_attribute("value"))
        element.send_keys(length * Keys.BACKSPACE)

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

    def test_create_event_on_calendar_page(self):
        profile = Profile.objects.get(user=User.objects.get(username="test1234"))
        calendar_url = self.live_server_url + reverse("calendar")
        self.browser.get(calendar_url)
        wait(self.browser, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "add_event_for_user"))).click()

        start_date = datetime.now(tz=timezone.utc).astimezone()
        end_date = datetime.now(tz=timezone.utc).astimezone() + timedelta(days=1)

        title = self.browser.find_element_by_css_selector("input#title")
        start_event = self.browser.find_element_by_css_selector("input#start_event")
        self.clear_text(start_event)
        end_event = self.browser.find_element_by_css_selector("input#end_event")
        notes = self.browser.find_element_by_css_selector("input#notes")
        # user id auto setup (value in hidden input)
        submit_btn = self.browser.find_element_by_css_selector("input#submit-event")

        title.send_keys("test")
        start_event.send_keys(datetime.strftime(start_date, "%Y-%m-%d %H:%M"))
        end_event.send_keys(datetime.strftime(end_date, "%Y-%m-%d %H:%M"))
        notes.send_keys("test")
        submit_btn.send_keys(Keys.ENTER)
        time.sleep(2)
        count_events = Calendar.objects.filter(user=profile).count()
        self.assertEqual(1, count_events)

    def test_delete_event_on_calendar_page(self):
        event = Calendar.objects.create(
            title="test",
            start_event=datetime.now(),
            end_event=datetime.now() + timedelta(days=1),
            notes="test",
            user=Profile.objects.get(user=User.objects.get(username="test1234"))
        )
        event.save()
        count = Calendar.objects.filter(user=Profile.objects.get(user=User.objects.get(username="test1234"))).count()
        calendar_url = self.live_server_url + reverse("calendar")
        self.browser.get(calendar_url)
        wait(self.browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.posts"))).click()
        wait(self.browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-dark"))).click()
        after_del = Calendar.objects.filter(
            user=Profile.objects.get(user=User.objects.get(username="test1234"))
        ).count()
        self.assertEqual(count, after_del + 1)

    def test_update_event_on_calendar_page(self):
        event = Calendar.objects.create(
            title="test",
            start_event=datetime.now(tz=timezone.utc).astimezone(),
            end_event=datetime.now(tz=timezone.utc).astimezone() + timedelta(days=1),
            notes="test",
            user=Profile.objects.get(user=User.objects.get(username="test1234"))
        )
        event.save()
        calendar_url = self.live_server_url + reverse("calendar")
        self.browser.get(calendar_url)
        wait(self.browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.posts"))).click()
        wait(self.browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                 "button#event-edit.btn.btn-success"))).click()
        start_date = datetime.now(tz=timezone.utc).astimezone()
        end_date = datetime.now(tz=timezone.utc).astimezone() + timedelta(days=1)
        title = self.browser.find_element_by_css_selector("input#title")
        start_event = self.browser.find_element_by_css_selector("input#start_event")
        end_event = self.browser.find_element_by_css_selector("input#end_event")
        notes = self.browser.find_element_by_css_selector("input#notes")
        # user id auto setup (value in hidden input)
        submit_btn = self.browser.find_element_by_css_selector("input#submit-event-edit")
        title.send_keys("test123")
        start_event.send_keys(datetime.strftime(start_date, "%Y-%m-%d %H:%M"))
        end_event.send_keys(datetime.strftime(end_date, "%Y-%m-%d %H:%M"))
        notes.send_keys("test123")
        submit_btn.send_keys(Keys.ENTER)
        time.sleep(2)
        event = Calendar.objects.filter(user=Profile.objects.get(user=User.objects.get(username="test1234")))[0]
        self.assertEqual(event.title, "testtest123")








