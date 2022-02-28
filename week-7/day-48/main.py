from selenium import webdriver

chrome_driver_path = "/Users/mjrod/Documents/coding/selenium-chrome-driver/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://amazon.ca")
driver.quit()