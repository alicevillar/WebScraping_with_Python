from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


# To prevent window from opening: use module Options

# If I wanted to create a object of the class Options
chrome_options = Options()
chrome_options.add_argument("--headless")

# Localing the driver
PATH = "C://Drivers/chromedriver.exe"

# configurating driver so that selenium can manipulate the navigator
driver = webdriver.Chrome(PATH) #options=chrome_options  => this second parameter is optional (to prevent window from opening)

# accessing google page using function "get"
driver.get("https://en.wikipedia.org/wiki/Main_Page")

#waiting one second for the web broser open the page
time.sleep(1)

#creating variable to receive the path for the search box
search_input=driver.find_element_by_xpath('//*[@id="searchInput"]')

# Using the method send_keys, which is aimed to write in the search box
search_input.send_keys("Aristotle")

# Pressing enter
search_input.send_keys(Keys.ENTER)

#waiting one second so the web broser has enough time to change to another page
time.sleep(1)

found = driver.find_element_by_xpath("//*[@id='mw-content-text']/div[3]/ul/li[1]/div[1]/a")

# Using the method send_keys, which is aimed to write in the search box
found.click()

#waiting one second for the web broser open the page
time.sleep(1)

first_paragraph=driver.find_element_by_xpath("//*[@id='mw-content-text']/div[1]/p[3]")

print(first_paragraph.get_attribute("innerText"))


#driver.close()



