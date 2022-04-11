import time
from selenium import webdriver

# 要测试的网站
from selenium.webdriver.common.by import By

weburl = 'http://bbs.51testing.com/forum.php'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(weburl)
driver.implicitly_wait(5)

# 账号、密码
login = '凌波尤里'
password = 'liuyan19970928'
driver.find_element(By.ID,'ls_username').send_keys(login)
driver.find_element(By.ID,'ls_password').send_keys(password)
driver.find_element(By.CLASS_NAME,'pn vm').click()

# # 定位用户名
# username = brower.find_element_by_id("loginname")
# username.send_keys(userid)
# # 定位密码
# userpswd = brower.find_element_by_id("nloginpwd")
# userpswd.send_keys(password)
# time.sleep(5)
# 定位到登录按钮
# brower.find_element_by_id("loginsubmit").click()

time.sleep(5)

driver.quit()