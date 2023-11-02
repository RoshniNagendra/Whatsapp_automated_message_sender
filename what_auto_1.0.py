import sys,time
from datetime import date, datetime
from selenium.common.exceptions import NoSuchElementException 
from selenium import webdriver as wb
from selenium.webdriver.chrome.options import Options
from config import CHROME_PROFILE_PATH

today = date.today().strftime('%d/%m/%Y')
current_time = datetime.now().strftime("%H:%M:%S")
msgDate = '30/06/2022'
msgTime = '04:07:00'

msg = "helloooo"

def new_chat(user_name):
    new_chat = driver.find_element_by_xpath('//div[@class="_13NKt copyable-text selectable-text"]')
    new_chat.send_keys(user_name)
    time.sleep(2)

    try:
        user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
    except NoSuchElementException as se:
        print("Username not in contact list")
    except Exception as e:
        driver.close()
        print(e)
        sys.exit()


if __name__ == '__main__':

    while True:
        if msgDate == today:
           current_time = datetime.now().strftime("%H:%M:%S")
           if current_time>=msgTime:
            

                options = wb.ChromeOptions()
                options.add_argument(CHROME_PROFILE_PATH)
                #options.add_argument("--profile-directory=Default")
                driver = wb.Chrome('chromedriver.exe',options=options)
                driver.get('https://web.whatsapp.com/')
                time.sleep(40)

                user_list = ['Pappa♥️'] 

                for user_name in user_list:
                    try:
                        user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
                        user.click()
                    except NoSuchElementException as se:
                        new_chat(user_name)
                        time.sleep(1)

                    time.sleep(2)
                    message_box = driver.find_element_by_xpath('//div[@class="p3_M1"]') 
                    time.sleep(2)

                    message_box.send_keys(msg)
                    time.sleep(2)

                    message_box = driver.find_element_by_xpath('//button[@class="tvf2evcx oq44ahr5 lb5m6g5c svlsagor p2rjqpw5 epia9gcq"]')
                    message_box.click()
                    time.sleep(2)
                    #driver.close()
                    #sys.exit()
        today = date.today().strftime('%d/%m/%Y')
        time.sleep(5)
        driver.close()
        sys.exit()



"""
driver_path = "C:/Users/91636/OneDrive/Documents/DCRYPT/automation/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
options = wb.ChromeOptions()
#option.add_argument("user-data-directory=C:/Users/91636/AppData/Local/Google/Chrome/User Data")
options.add_argument("--user-data-directory=C:/Users/91636/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default")
options.add_argument("--profile-directory=Default")
options.binary_location = brave_path
driver = wb.Chrome('chromedriver.exe', chrome_options=options)

driver.get("https://web.whatsapp.com/")
"""

