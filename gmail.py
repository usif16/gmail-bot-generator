from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import random
import string
import requests
import ipaddress
#############################################
###############################
# NUMBER API
###############################

# initialize an IPv4 Address
ip = ipaddress.IPv4Address("192.168.1.1")


############################### 
token = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mjc1MDU2MjcsImlhdCI6MTY5NTk2OTYyNywicmF5IjoiMzVjNDU3ZDhhMTU2MzRmMzY0YzViYzczNGE0YjA2NDgiLCJzdWIiOjE4OTE5OTV9.N19UsCth8IUJRVPXqvf8taREdJKRCbcA0oV4eg6iRx7Unl8RKe05sIlQ7LnrxkeXGQXjThK1_S20Edy3G7CcUPi8cyrMGaeyHfW8CGDoM9RgzXKKxniZA3ru7BhQT_8wsPpFaha3n7lZFW8gXS_abSx9mFSTjGaIHYTd_jtxIvHrBq_VYTEZ7P_H5Yx4pKr9xI7Ff5DVGeIJN5ZPqqdRNUyCCg77s2Ot0qhXagbWiTeoT4-qXEeWjck6Mj7mbdRIqrFTrnc2TV8_6XqczGQR3hbUk36t63HytYRJ-cMiOIoqufgr5-e_83fP3GQYiSO7J814CIzqM5Z0K5-pzbA5CA'

headers = {
    'Authorization': 'Bearer ' + token,
    'Accept': 'application/json',
}


url = f'https://5sim.net/v1/user/check/{id}'

def GetCode (id):
    
    url = f'https://5sim.net/v1/user/check/{id}'
    response = requests.get(url, headers=headers).json()
    return response['sms'][0]['code']
    


def NewPhone ():
        
    country = 'russia'
    operator = 'any'
    product = 'google'

    url = f'https://5sim.net/v1/user/buy/activation/{country}/{operator}/{product}'

    response = requests.get(url, headers=headers).json()
    phone_num = response ['phone']
    phone_id = response ['id']
    return [phone_id,phone_num]


#############################################

# the Func for the automation
browser = webdriver.Chrome()

# To Open The URL I need
browser.get("https://accounts.google.com/signup")
sleep(10)

# Start To Create the Email
createBtn = browser.find_element(By.XPATH , '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div[1]/div[1]/div')
createBtn.click()

sleep(3)
# First Name Input
first_name= browser.find_element(By.XPATH , '//*[@id="firstName"]')
first_name.click
first_name.send_keys("moahmmed")
sleep(0.5)

next1 = browser.find_element(By.XPATH , '//*[@id="collectNameNext"]/div/button/span')
next1.click()
sleep(1)

#Birth Day Input
birth_d = browser.find_element(By.XPATH,'//*[@id="day"]')
birth_d.click()
birth_d.send_keys('1')
sleep(0.5)

#Birth Month Choose "from multi option"
birth_m = browser.find_element(By.XPATH,'//*[@id="month"]')
birth_m.click()
birth_m.send_keys(Keys.ARROW_DOWN)
birth_m.click()
sleep(0.5)

#Birth Year Input
birth_y=browser.find_element(By.XPATH,'//*[@id="year"]')
birth_y.click()
birth_y.send_keys('2000')
sleep(0.5)

#Gender Choose
ginder = browser.find_element(By.XPATH,'//*[@id="gender"]')
ginder.click()
ginder.send_keys(Keys.ARROW_DOWN)
ginder.click()
sleep(0.5)

next2 = browser.find_element(By.XPATH,'//*[@id="birthdaygenderNext"]/div/button')
sleep (2)
next2.click()

sleep (2)
# random email generator
################################################
def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

rand_email = (random_char(10))
################################################


###  FIRST FORMAT " CHOOSE FROM THE LIST OR USE YOUR OWN EMAIL "  AUTO CODE
def email_choose() :
    email_Btm = browser.find_element (By.XPATH,'//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/span/div[1]')
    email_Btm.click()  
    sleep(1)
    next_emailChoose = browser.find_element (By.XPATH , '//*[@id="next"]/div/button')
    next_emailChoose.click
    sleep (0.5)
    
    
### Second Format "INPUT THE EMAIL DIRECTLY" Auto Write
def email_inputd():
    email_input = browser.find_element(By.XPATH,'//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div[1]/div/div[1]/div/div[1]/input')
    email_input.click()
    email_input.send_keys(rand_email)
    sleep(0.5)
  
    

try :
    email_choose()
except :
    email_inputd()


next3 = browser.find_element(By.XPATH,'//*[@id="next"]/div/button')
next3.click()

sleep(1)
    
    
    
"""

Choose_email = browser.find_element (By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/span/div[3]/div/div[1]/div/div[3]/div')
Choose_email.click

sleep(5)
"""


""""
"""



password_input= browser.find_element(By.XPATH,'//*[@id="passwd"]/div[1]/div/div[1]/input')
password_input.click
password_input.send_keys ("123456Mm654321*")
sleep (0.5)


password_input2= browser.find_element(By.XPATH,'//*[@id="confirm-passwd"]/div[1]/div/div[1]/input')
password_input2.click
password_input2.send_keys ("123456Mm654321*")
sleep (0.5)

#show the password
'''
password_showBTM = browser.find_element(By.XPATH,'//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div[3]/div/div[1]/div/div/div[1]/div/input')
password_showBTM.click
sleep(0.5)
'''

next4 = browser.find_element(By.XPATH,'//*[@id="createpasswordNext"]/div/button')
sleep(0.5)

next4.click()
sleep (3)


phone_input = browser.find_element(By.XPATH,'//*[@id="phoneNumberId"]')
phone_input.click()
phone_id_num = NewPhone()
sleep(10)
phone_input.send_keys(phone_id_num[1])
sleep(3)

next5 = browser.find_element(By.XPATH,'//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div/div/div/button/div[3]')
next5.click

get_sms = GetCode(phone_id_num[0])




sleep(30*60)