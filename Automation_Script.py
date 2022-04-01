from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import subprocess
subprocess.call([r'path to the .bat file'])
time.sleep(5)

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#Change chrome driver path accordingly
chrome_driver = r"path to chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
driver.maximize_window()
driver.get('https://web.whatsapp.com/')
#change the "User" to any contact name, only chat from that person will be monitored.
name = "User"
time.sleep(15)

inp_xpath_search =  '//div[@class="_1awRl copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"]'
input_box_search = driver.find_element_by_xpath(inp_xpath_search)
input_box_search.click()
time.sleep(2)
input_box_search.send_keys(name)
time.sleep(2)
user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()
#just a substring matching. Reply is sent to only messages containg these keyword.
sub="bot"
prevmsg=""
prevhour=0
prevmin=0
#new Code Here
#_1VzZY selectable-text invisible-space copyable-text
while True:
    try:
        p=driver.find_elements_by_class_name('_1RAno')
        for item in p:
            if sub in item.text.lower():
                tem=item.text
                sample=tem.splitlines()
                if(len(sample)==3):
                    inc_msg=sample[1]
                    time=sample[2]
                elif(len(sample)==2):
                    inc_msg=sample[0]
                    time=sample[1]
                time=time.split()
                shorttime=time[0]
                apm=time[1]
                shorttime=shorttime.split(":")
                hour=int(shorttime[0])
                minute=int(shorttime[1])
                if(hour==prevhour and minute==prevmin and prevmsg==inc_msg):
                    print("already replied")
                elif(hour>=prevhour and minute>=prevmin):
                    prevhour=hour
                    prevmin=minute     
                    my_bot = ChatBot(name='bud',
                    logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'])
                    response = my_bot.get_response(inc_msg)
                    response=str(response)
                    inp_xpath = '//div[@class="_1awRl copyable-text selectable-text"][@contenteditable="true"][@data-tab="6"]'
                    input_box = driver.find_element_by_xpath(inp_xpath)
                    input_box.send_keys(response + Keys.ENTER)
    except NoSuchElementException:
        print("end")
    break