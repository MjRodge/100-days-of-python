from selenium import webdriver

chrome_driver_path = "/Users/mjrod/Documents/coding/selenium-chrome-driver/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://python.org")
search = driver.find_element_by_name("q")
# print(search.get_attribute("placeholder"))

documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)


python_event_times = driver.find_elements_by_css_selector(".event-widget time")
# for time in python_event_times:
#     print(time.text)

python_event_names = driver.find_elements_by_css_selector(".events-widget li a")
for name in python_event_names:
    print(name)

driver.quit()
