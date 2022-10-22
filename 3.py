from asyncore import loop
from selenium import webdriver
import time



time.sleep(2)


def lol():
    web = webdriver.Chrome()
    web.get('https://hitzboost.com/session/run/v2tEdGMeGGwG3HfT0GS84RO6snYH0U5G-Tsd6EwDPjuSp1FIA7ePOfFYNwGQraV87fVek0nEvl8jaFptEWW8gFl4-ydBkGmMYorpdV3iRdq5pSG3bWDMILM')
    time.sleep(2)
    Submit = web.find_element("xpath",'//*[@id="start_buttons"]/button')
    Submit.click()
    print("time is ticking")
    time.sleep(2220)
    web.quit()
    lol()
lol()






