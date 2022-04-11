import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# 要测试的网站
from selenium.webdriver.common.by import By

weburl = 'https://www.baidu.com/'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(weburl)
driver.implicitly_wait(5)


# search = '乌克兰'
# driver.find_element(By.NAME,'wd').send_keys(search)
# driver.find_element(By.ID,'su').click()
# driver.implicitly_wait(5)
#
# driver.find_element(By.NAME,'wd').clear()
# driver.find_element(By.NAME,'wd').send_keys('美国')
# driver.find_element(By.ID,'su').click()

#打开百度首页
driver.get('https://www.baidu.com')
# #（模糊匹配”乌“）
# driver.find_element(By.PARTIAL_LINK_TEXT,'乌').click()

el_btn = driver.find_element(By.LINK_TEXT,'更多').click()
# #鼠标单击
# ActionChains(driver).click(el_btn).perform()
# #右击
# ActionChains(driver).context_click(el_btn).perform()
# #双击
# ActionChains(driver).double_click(el_btn).perform()
# #拖动
# ActionChains(driver).drag_and_drop(el_btn).perform()
#鼠标悬停
ActionChains(driver).move_to_element(el_btn).perform()
















