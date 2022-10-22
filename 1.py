from asyncore import loop
from selenium import webdriver
import time



time.sleep(2)


def lol():
    web = webdriver.Chrome()
    web.get('https://hitzboost.com/session/run/Ib850FtEEjdd6L3CADqx8aRNIP5fMYxCr6NxFDDPctV_vBPD_TSoJBwWKjt_E_wnRWZtmIZQQV92UCVQxSGqA1YoHpl2dd1lduzBVbN-Sc5ZROfvJGOCpAM')
    time.sleep(2)
    Submit = web.find_element("xpath",'//*[@id="start_buttons"]/button')
    Submit.click()
    print("time is ticking")
    time.sleep(2220)
    web.quit()
    lol()
lol()






