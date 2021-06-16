import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

# in order to work, you will have to install the chrome web driver on your local machine. See link down below.
# link: https://chromedriver.chromium.org/downloads
# this code is very similar to the one suggested by Shane Lee, see his video down below.
# link: https://youtu.be/xZxaylG2wWQ

# other file that contains a bunch of methods returning username and password
from credenziali import *


mute_status = False

driver = webdriver.Chrome()
driver.get(Link())
driver.maximize_window()

wait = WebDriverWait(driver, 10)


def login():
    login_btn = driver.find_element_by_xpath("//button[text()='Log in']")
    login_btn.click()
    wait.until(EC.visibility_of_element_located((By.ID, "login-username")))
    # method from file "credenziali.py"
    type_text(Username())
    tab()
    # method from file "credenziali.py"
    type_text(Password())
    times(tab, 3)
    enter()
    time.sleep(1)

def accept_cookies():
    times(tab, 3)
    enter()

def times(fn, times):
    for _ in range(0, times):
        fn()
        time.sleep(1)


def type_text(text):
    actions = ActionChains(driver)
    actions.send_keys(text)
    actions.perform()

def press_key(key):
    type_text(key)

def tab():
    press_key(Keys.TAB)


def enter():
    press_key(Keys.ENTER)


def mute():
    mute_btn = driver.find_element_by_xpath("//button[contains(@class, 'volume-bar__icon')]")
    mute_btn.click()


def unmute():
    mute()


def now_playing_ad():
    now_playing_el = driver.find_elements_by_xpath("//div[contains(@data-testid, 'now-playing-widget')]")
    print("a=" + str(now_playing_el))
    print("b=" + str("".join(el.text for el in now_playing_el).lower()))
    return "advert" in "".join(el.text for el in now_playing_el).lower()


login()
accept_cookies()

while True:
    if now_playing_ad() == True and mute_status == False:
        mute()
        mute_status = True
    elif now_playing_ad() == False and mute_status == True:
        unmute()
        mute_status = False
    else:
        pass