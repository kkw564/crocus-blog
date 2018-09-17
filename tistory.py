#-*- coding: utf-8 -*-
import os
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

chrome_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver')
driver = webdriver.Chrome(chrome_path)

driver.get('https://www.tistory.com/auth/login/?redirectUrl=https://www.crocus.co.kr/manage/')

id = input("input your id : ")
pw = input("input your pwd : ")
driver.find_element_by_name('loginId').send_keys(id)
driver.find_element_by_name('password').send_keys(pw)


driver.find_element_by_class_name('btn_login').click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
keywordRank = soup.select('.wrap_box .box_keyword')

keywordRank = str(keywordRank)
regex = r'>[가-힣a-zA-Z\s]+<'
ret = re.findall(regex, keywordRank)
ret = ret[1:]
for i in range(0, len(ret)):
    ret[i] = ret[i][1:len(ret[i]) - 1]
    print('i :: ', i, " ret :: ", ret[i])

print(ret)

print("\n".join(ret))

driver.get('https://programbasic.tistory.com/manage/design/skin/edit#/source/html/')


htmlXpath=driver.find_elements_by_xpath('//*[@id="skin-editor"]/div/div[3]/div/div[1]/ul')[0]

action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(htmlXpath, 50, 500)
action.click()
action.perform()
action.key_down(Keys.CONTROL).send_keys('f').key_up(Keys.CONTROL)
action.send_keys('/keywordRankList.*/').key_down(Keys.ENTER)
action.key_down(Keys.CONTROL).send_keys('f').key_up(Keys.CONTROL)
action.send_keys('/keywordRankList.*/').key_down(Keys.ENTER)
action.key_down(Keys.CONTROL).send_keys('f').key_up(Keys.CONTROL)
action.send_keys('/keywordRankList.*/').key_down(Keys.ENTER).perform()

for i in range(0,len(ret)):
    ret[i] = '"' + ret[i] + '"'    

ret = ','.join(ret)
print("ret : ", ret)
action.send_keys('keywordRankList:[').send_keys(ret).send_keys('],').perform()

driver.find_element_by_xpath('//*[@id="skin-editor"]/div/div[3]/div/div[1]/button[3]').click()