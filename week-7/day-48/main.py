from selenium import webdriver

chrome_driver_path = "/Users/mjrod/Documents/coding/selenium-chrome-driver/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://python.org")
search = driver.find_element_by_name("q")
# print(search.get_attribute("placeholder"))

documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

python_events = driver.find_elements_by_xpath("/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li")
for x in python_events:
    print(x.text)

driver.quit()
