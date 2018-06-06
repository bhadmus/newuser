from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(r"C:\Users\ademola.bhadmus\Documents\Automation Projects\Python\VigiPay\bin\chromedriver.exe")
driver.get("http://opensource.demo.orangehrmlive.com/")
driver.maximize_window()
driver.find_element_by_id("txtUsername").send_keys("Admin")
time.sleep(1)
driver.find_element_by_id("txtPassword").send_keys("admin")
time.sleep(2)
driver.find_element_by_id("btnLogin").click()
contain = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div/div/fieldset/legend")
assert contain.text == "Quick Launch"
legend = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div[2]/div/div/div[3]/fieldset/legend")
assert legend.text == "Pending Leave Requests"
adminTab = driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[1]/a/b")
hover = ActionChains(driver).move_to_element(adminTab).perform()
time.sleep(2)
userMng = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
mngHover = ActionChains(driver).move_to_element(userMng).perform()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']").click()
driver.find_element_by_xpath("//*[@id='btnAdd']").click()
driver.find_element_by_xpath('//*[@id="systemUser_userType"]').click()
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/select/option[1]").click()
driver.find_element_by_xpath('//*[@id="systemUser_employeeName_empName"]').send_keys("Steven Edwards")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="systemUser_userName"]').send_keys("m.wards")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="systemUser_password"]').send_keys("Qwerty123@")
driver.find_element_by_xpath('//*[@id="systemUser_confirmPassword"]').send_keys("Qwerty123@")
check = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[8]/em")
assert check.text == "*"
driver.find_element_by_css_selector("#btnSave").click()
time.sleep(5)
driver.close()

