from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import time
# NOTICE!
# IMPORT CHROMEDRIVER IN THE SAME FOLDER AND COPY PATH
PATH = "C:/Users/I355372/Documents/python/Facebook Bot/chromedriver.exe"
class FacebookBot:
    def __init__(self,username, password):
        self.username=username
        self.password=password
        
    
    def Login(self,driver):
        driver.get('https://www.facebook.com')
        print("Successfull Initiate...")
        user = driver.find_elements_by_xpath("//*[@id=\"email\"]")
        user[0].send_keys(self.username)
        psw = driver.find_elements_by_xpath("//*[@id=\"pass\"]")
        psw[0].send_keys(self.password)
        psw[0].send_keys("\ue007")
        sleep(5)
    
    def Quit(self,driver):
        print("Ending program")    
        driver.quit()

    def DeleteMess(self,driver,actions):
        print("Navigating to chat box")
        driver.get("https://www.facebook.com/messages/t/")
        WebDriverWait(driver, 10)
        print("\n\nChatbox is here...")
        cnt=0
        while True:
            try:
                driver.find_element_by_id("dots-3-horizontal").click()                    
                actions.send_keys(Keys.ARROW_DOWN *3, Keys.SPACE ).perform()
                actions.send_keys(Keys.TAB, Keys.SPACE).perform()
                cnt=cnt+1
                sleep(5)
            except:
                print("\nMessages deleted: ",cnt)
                break
        time.sleep(2)
        driver.refresh()
        time.sleep(3)
        print("\n\nProcess complete. \nIf some messages aren't deleted, run the script again.\n")
        sleep(5)

#######################-INITIATE BROWSER-##################################
option = Options()     
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2 
})
driver = webdriver.Chrome(PATH,chrome_options=option)
actions = ActionChains(driver)
###########################################################################
##                            MAIN                                       ##
duc = FacebookBot("id","pass")
duc.Login(driver)
duc.DeleteMess(driver,actions)
duc.Quit(driver)
