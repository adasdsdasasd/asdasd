from asyncore import loop
from selenium import webdriver
import time



time.sleep(2)


def lol():
    web = webdriver.Chrome()
    web.get('https://hitzboost.com/session/run/MrkuIs5sPjpWAnTDNRVRJCMNw5g0mRstk4wg9gTVlQ3Jkglv9u98L83AsTFtOY-b44U5U-3m60oQyJK3kTQCSMjGeWWvUO6eEGfAE5PVEBk5QFzVcvltLbo')
    time.sleep(2)
    Submit = web.find_element("xpath",'//*[@id="start_buttons"]/button')
    Submit.click()
    print("time is ticking")
    time.sleep(2220)
    web.quit()
    lol()
lol()






