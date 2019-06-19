import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException

browser = webdriver.Chrome("chromedriver.exe")
browser.get('https://m.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier=10156570369232217') # mobile facebook like screen, you can change and use here

browser.maximize_window()

kullanici_adi= 'FACEBOOK USERNAME'
parola = 'FACEBOOK PASSWORD'
time.sleep(5)

browser.find_element_by_xpath('//*[@id="m_login_email"]').send_keys(kullanici_adi)
browser.find_element_by_xpath('//*[@id="m_login_password"]').send_keys(parola)
browser.find_element_by_xpath('//*[@id="u_0_5"]').click()
wait = WebDriverWait(browser, 10)
takipcisinir = 0 # follower limit
scrollartis=80 # scroll increase

time.sleep(2)


# scroll page 80 times or whatever you want you can change
try:
    for i in range(80):
        browser.find_element_by_xpath('//*[@id="reaction_profile_pager"]/a/div/div/div/strong').click()
        time.sleep(1)

except:
    print("np")
browser.execute_script('window.scrollTo(0,80)')


for i in range(5000):
    try:
        follow = browser.find_elements(By.XPATH,'//button[contains(@id,"u_")]')[i] # static xpath
        follow.click()
        print(str(i)+". Kisiyi takip ettim")
        browser.execute_script("window.scrollTo(0,"+str(scrollartis)+")")

        scrollartis = scrollartis+140 # scrolling
        time.sleep(1)

    except ElementNotVisibleException:
        print("ElementNotVisibleException")
        continue


        # to pass security popups

    except:
        try:
            print("genel")
            browser.find_element_by_xpath('//*[@id="viewport"]/div[2]/div[1]/div/div[2]/div/div[3]/div/div[2]/form/button').click()

        except:
            browser.find_element_by_xpath('//*[@id="viewport"]/div[2]/div[1]/div/div[2]/div/div[4]/button').click()
            continue
        continue
