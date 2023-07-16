#Automation
from selenium import webdriver 
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

chrome_browser = webdriver.Chrome(options=options)

# print(chrome_browser)
chrome_browser.get("http://www.techlistic.com/p/selenium-practice-form.html")

assert "Button" in chrome_browser.page_source
button_text = chrome_browser.find_element()
print(button_text.get_attribute("innerHTML"))