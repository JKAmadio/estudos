from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path='/home/jkahv/estudos/python/scrapping/selenium/chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get("https://techwithtim.net")
print(driver.title)

# searching "test" at the searchbar and hitting enter
search = driver.find_element(By.NAME,'s')
search.send_keys('test')
search.send_keys(Keys.RETURN)

try:
    # wait for 10sec or until main tag is loaded
    main = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "main"))
            )

    articles = main.find_elements(By.TAG_NAME, 'article')

    for article in articles:
        summary = article.find_element(By.CLASS_NAME, 'entry-summary')
        print(summary.text)
finally:
    driver.close()
