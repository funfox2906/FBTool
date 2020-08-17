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
# IMPORT CHROMEDRIVER IN THE SAME FOLDER
class FacebookBot:
    def __init__ (self, username, password):
        self.username=username
        self.password=password
        option = Options()     
        option.add_argument("--disable-infobars")
        # option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        # Pass the argument 1 to allow and 2 to block
        option.add_experimental_option("prefs", { 
            "profile.default_content_setting_values.notifications": 2 
        })
        driver = webdriver.Chrome(chrome_options=option)
        driver.get('https://www.facebook.com')
        print("Successfull Initiate...")
        user = driver.find_elements_by_xpath("//*[@id=\"email\"]")
        user[0].send_keys(self.username)
        psw = driver.find_elements_by_xpath("//*[@id=\"pass\"]")
        psw[0].send_keys(self.password)
        psw[0].send_keys("\ue007")
        sleep(5)
        #################################################
        print("1. Delete/Hide all the messages")
        print("2. Delete all post in facebook group")
        choice = input ("What you want to do: ")   
        if choice == '1':
            print("Navigating to chat box")
            driver.get("https://www.facebook.com/messages/t/")
            wait = WebDriverWait(driver, 10)
            actions = ActionChains(driver)
            print("\n\nChatbox is here...")
            while True:
                try:
                    driver.find_element_by_id("dots-3-horizontal").click()                    
                    actions.send_keys(Keys.ARROW_DOWN *3, Keys.SPACE ).perform()
                    actions.send_keys(Keys.TAB, Keys.SPACE).perform()
                    sleep(5)
                except:
                    print("\nMessages deleted.")
                    break
            time.sleep(2)
            driver.refresh()
            time.sleep(3)
            print("\n\nProcess complete. \nIf some messages aren't deleted, run the script again.\n")
            sleep(5)

        elif choice == '2':
            print("Navigate to group")        
            url = input("Enter URL to Group: ")
            driver.get(url)
            print("Navigating to Group: "+ url)
            wait = WebDriverWait(driver, 10)
            driver.execute_script("window.scrollTo(0, 1040)")
            while True:
                try:
                    # btn = driver.find_element_by_class_name("_6a uiPopover _5pbi _cmw _1wbl _b1e openToggler selected")
                    # for i in btn:
                    #     i.click()
                    # actions.send_keys(Keys.ARROW_DOWN *7, Keys.SPACE ).perform()
                    # actions.send_keys(Keys.TAB, Keys.SPACE).perform()
                    btn = driver.find_element_by_xpath("//*[@id=\"u_0_29\"]")
                    btn.click()
                    # wait = WebDriverWait(driver, 10)
                    # wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//button/span[.=\"Post\"]"))).click();
                    sleep(5)
                except:
                    print("\nMessages deleted.")
                    break
            
            sleep(5)

        print("Ending program")    
        driver.quit()

FacebookBot("funfox2906@gmail.com","Duc2906@ELTE")
