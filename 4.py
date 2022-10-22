from asyncore import loop
from selenium import webdriver
import time



time.sleep(2)


def lol():
    web = webdriver.Chrome()
    web.get('https://hitzboost.com/session/run/q2EkpYCvPeBj5tiMYT0nExb6VgI-4FnfGPs7MVWh7myqacnoyOqsoKvqy-wMxgm4sevJmYieGfS8DSjhfIW6u07l9qXTsszK8UGMvsvDGt_foVMBYsVAHs4')
    time.sleep(2)
    Submit = web.find_element("xpath",'//*[@id="start_buttons"]/button')
    Submit.click()
    print("time is ticking")
    time.sleep(2220)
    web.quit()
    lol()
lol()






