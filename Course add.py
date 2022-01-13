import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://wrem.sis.yorku.ca/Apps/WebObjects/REM.woa/wa/DirectAction/rem")
time.sleep(2)
username = driver.find_element('mli', By.ID)
username.clear()
username.send_keys('Your username')
password = driver.find_element('password', By.ID)
password.clear()
username.send_keys('Your password')
login = driver.find_element('dologin', By.NAME)
login.click()
time.sleep(5)
select = Select(driver.find_element('5.5.1.27.1.11.0', By.NAME))
select.select_by_value('3')
submit_button = driver.find_element('5.5.1.27.1.13', By.NAME)
submit_button.click()
add_button = driver.find_element('5.1.27.1.23', By.NAME)
add_button.click()
course_box = driver.find_element('5.1.27.7.7', By.NAME)
course_box.clear()
course_box.send_keys('Course Id')
done_button = driver.find_element('5.1.27.7.9', By.NAME)
done_button.click()
confirm_button = driver.find_element('5.1.27.15.9', By.NAME)
confirm_button.click()
continue_button = driver.find_element('5.1.27.27.9', By.NAME)
continue_button.click()
driver.close()
driver.quit()



