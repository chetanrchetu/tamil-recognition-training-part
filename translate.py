from selenium.webdriver import Chrome,ChromeOptions,ChromeService 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from config import TRANSLATE
import time


def translate_tamil(tamil_word):
    chromedriver_path=os.getcwd()+'\\chromedriver.exe'

    service=ChromeService(executable_path=chromedriver_path)
    options=ChromeOptions()
    # options.add_argument('--headless')


    driver=Chrome(service=service,options=options)

    driver.get(TRANSLATE)

    input_box=driver.find_elements(By.TAG_NAME,"textarea")
    input_box=input_box[1]
    input_box.send_keys(tamil_word)

    time.sleep(3)

    output=driver.find_elements(By.XPATH,"//span[@class='Y2IQFc']")
    output=output[2].text

    time.sleep(10)

    return output