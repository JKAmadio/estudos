from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# 1.configurar driver
# infos: https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/#4-hard-coded-location
PATH = "/home/jkahv/estudos/python/scrapping/selenium/chromedriver.exe"
service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service)

# 2.acessar página principal
# infos: https://www.selenium.dev/documentation/webdriver/getting_started/first_script/#2-take-action-on-browser
driver.get("https://www.techwithtim.net/")

# 3.clicar em Python Programming
# infos: https://www.selenium.dev/documentation/webdriver/elements/locators/#link-text
first_button = driver.find_element(By.LINK_TEXT, "Python Programming")
first_button.click()

try:
    # 4.clicar em Beginner Python Tutorials
    second_button = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Beginner Python Tutorials"))
            )
    second_button.click()

    thrid_button = WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.ID, "sow-button-19310003"))
            )
    thrid_button.click()

    # 5. navegar usando browser
    # infos: https://www.selenium.dev/documentation/webdriver/interactions/navigation/#back
    driver.back()
    driver.back()
    driver.back()

    # infos: https://www.selenium.dev/documentation/webdriver/interactions/navigation/#forward
    driver.forward()
    driver.forward()

finally:
    driver.quit()

