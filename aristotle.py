from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup



# To prevent window from opening: use module Options

# If I wanted to create a object of the class Options
chrome_options = Options()
chrome_options.add_argument("--headless")

# Localing the driver
PATH = "C://Drivers/chromedriver.exe"

# configurating driver so that selenium can manipulate the navigator
driver = webdriver.Chrome(PATH,options=chrome_options) # this second parameter is optional (to prevent window from opening)

# accessing google page using function "get"
driver.get("https://en.wikipedia.org/wiki/Main_Page")

#creating variable to receive the path for the search box
search_input=driver.find_element_by_xpath('//*[@id="searchInput"]')

# Using the method send_keys, which is aimed to write in the search box
search_input.send_keys("Aristotle")

# Pressing enter
search_input.send_keys(Keys.ENTER)

