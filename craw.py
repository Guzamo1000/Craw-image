# https://www.youtube.com/watch?v=V_MV5EsdKRc

from selenium import webdriver #pip install selenium
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('path Chrome Driver')
driver.get('link website') //google.com

box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input') #element search in google
box.send_keys('Keyword') //press keyword
box.send_keys(Keys.ENTER) //Enter

driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click() #element image in google


#Will keep scrolling down the webpage until it cannot scroll no more
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    try:
        driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
        time.sleep(2)
    except:
        pass
    if new_height == last_height:
        break
    last_height = new_height


for i in range(1, 1000):
    try:
        # driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot('E:\Code\Craw_image\image\giraffe ('+str(i)+').png')
        driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot('path folder save image ('+str(i)+').png')
    except:
        pass
