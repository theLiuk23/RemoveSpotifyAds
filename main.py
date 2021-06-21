import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import pyttsx3


# in order to work, you will have to install the chrome web driver on your local machine. See link down below.
# link: https://chromedriver.chromium.org/downloads
# this code is very similar to the one suggested by Shane Lee, see his video down below.
# link: https://youtu.be/xZxaylG2wWQ


# other file that contains a bunch of methods returning username and password
from credenziali import *




mute_status = False

voce = pyttsx3.init()
driver = webdriver.Chrome()
driver.get(Link())
driver.maximize_window()

wait = WebDriverWait(driver, 10)


def close():
    talk("Sto chiudendo il programma")
    exit()


def talk(string):
    voce.say(string)
    print(string)
    voce.runAndWait()


def login():
    try:
        time.sleep(1)
        login_btn = driver.find_element_by_xpath("//button[text()='Accedi']")
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
    except Exception as ex:
        print(ex)
        close()


def accept_cookies():
    try:
        times(tab, 2)
        enter()
    except:
        close()


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
    try:
        mute_btn = driver.find_element_by_xpath("//button[contains(@class, 'volume-bar__icon')]")
        mute_btn.click()
        talk("Ho mutato una pubblicità")
    except:
        talk("Non posso mutare adesso. Goditi la tua pubblicità!")


def unmute():
    try:
        mute_btn = driver.find_element_by_xpath("//button[contains(@class, 'volume-bar__icon')]")
        mute_btn.click()
    except:
        talk("Non posso smutare adesso. Farlo manualmente per favore")


def now_playing_ad():
    now_playing_el = driver.find_elements_by_xpath("//div[contains(@data-testid, 'now-playing-widget')]")
    print("a=" + str(now_playing_el))
    print("b=" + str("".join(el.text for el in now_playing_el).lower()))
    return "advert" in "".join(el.text for el in now_playing_el).lower()

talk("Ho aperto Spotify")
login()
talk("Ho effettuato l'accesso")
accept_cookies()
talk("Ho accettato i cookies")

while True:
    try:
        if now_playing_ad() == True and mute_status == False:
            mute()
            mute_status = True
        elif now_playing_ad() == False and mute_status == True:
            unmute()
            mute_status = False
        else:
            pass
    except:
        close()