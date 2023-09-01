from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


PATH = "/home/jkahv/estudos/python/scrapping/selenium/chromedriver.exe"
service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")


driver.implicitly_wait(15)
english_lang = driver.find_element(By.ID, "langSelect-EN")
english_lang.click()

driver.implicitly_wait(15)
big_cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
actions = ActionChains(driver)

for i in range(100):
    actions.click(big_cookie)
    actions.perform()
    count = int(cookie_count.text.split(' ')[0])
    print(count)

print(driver.title)
