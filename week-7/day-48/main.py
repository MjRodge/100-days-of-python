from selenium import webdriver

chrome_driver_path = "/Users/mjrod/Documents/coding/selenium-chrome-driver/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://python.org")
search = driver.find_element_by_name("q")
print(search.get_attribute("placeholder"))
driver.quit()
