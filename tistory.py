#-*- coding: utf-8 -*-
import os
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# >내용<로 나오는 것을 내용으로 변환해준다.
def purify(rankList):
    rankList = str(rankList)
    regex = r'>[가-힣a-zA-Z\s]+<'
    retList = re.findall(regex, rankList)
    retList = retList[1:]
    for i in range(0, len(retList)):
        retList[i] = retList[i][1:len(retList[i]) - 1]

    return retList

# 랭크 개수를 5개 혹은 10개로 커팅하고 "내용"로 바꾼 후 ,로 join한다.
def formalize(rankList, cutSize):
    rankList = rankList[0:min(len(rankList), cutSize)]
    for i in range(0, len(rankList)):
        rankList[i] = '"' + rankList[i] + '"'

    rankList = ','.join(rankList)
    return rankList

chrome_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver')
driver = webdriver.Chrome(chrome_path)

driver.get('https://www.tistory.com/auth/login/?redirectUrl=https://www.crocus.co.kr/manage/')

#로그인 부분
id = input("input your id : ")
pw = input("input your pwd : ")
driver.find_element_by_name('loginId').send_keys(id)
driver.find_element_by_name('password').send_keys(pw)

driver.find_element_by_class_name('btn_login').click()

# 유입 키워드 순위 크롤링
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
keywordRank = soup.select('.wrap_box .box_keyword')

# 내부, 외부 키워드 크롤링
driver.get('https://programbasic.tistory.com/manage/statistics/keyword')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
keywordInnerRank = soup.select('.wrap_box .box_keyword')
keywordOuterRank = soup.select('.wrap_box50 .box_blog + .box_blog')

# 크롤링 내용 정제
retRank = purify(keywordRank)
retInnerRank = purify(keywordInnerRank)
retOuterRank = purify(keywordOuterRank)

# 크롤링 데이터 구조화
retRank = formalize(retRank, 5)
retInnerRank = formalize(retInnerRank, 10)
retOuterRank = formalize(retOuterRank, 10)

print("retRank :: ", retRank)
print("retInnerRank :: ", retInnerRank)
print("retOuterRank :: ", retOuterRank)

# 크롤링 내용 삽입
driver.get('https://programbasic.tistory.com/manage/design/skin/edit#/source/html/')

htmlXpath=driver.find_elements_by_xpath('//*[@id="skin-editor"]/div/div[3]/div/div[1]/ul')[0]

action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(htmlXpath, 50, 500)
action.click()
action.perform()
action.key_down(Keys.CONTROL).send_keys('f').key_up(Keys.CONTROL)
action.send_keys('/keywordRankList[^"].*/').key_down(Keys.ENTER)
action.send_keys('keywordRankList:[').send_keys(retRank).send_keys('],')

action.key_down(Keys.CONTROL).send_keys('f').key_up(Keys.CONTROL)
action.send_keys('/keywordInnerRankList[^"].*/').key_down(Keys.ENTER)
action.send_keys('keywordInnerRankList:[').send_keys(retInnerRank).send_keys('],')

action.key_down(Keys.CONTROL).send_keys('f').key_up(Keys.CONTROL)
action.send_keys('/keywordOuterRankList[^"].*/').key_down(Keys.ENTER)
action.send_keys('keywordOuterRankList:[').send_keys(retOuterRank).send_keys('],').perform()

driver.find_element_by_xpath('//*[@id="skin-editor"]/div/div[3]/div/div[1]/button[3]').click()