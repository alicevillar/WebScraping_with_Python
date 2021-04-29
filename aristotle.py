from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

###########################################################################################
#
#   PART 1: Initializations
#   1.1. Preventing the browser window from opening
#   1.2. Localizing the driver
#   1.3. Configuring the driver so that selenium can manipulate the navigator
#
###########################################################################################

# PART 1.1 - Preventing window from opening

# Create an object of the class Options and adding the argument --headless to invoke Chrome in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# PART 1.2 - Localizing the driver
# Setting the path
PATH = "C://Drivers/chromedriver.exe"

# PART 1.3 - Configuring the driver so that selenium can manipulate the navigator
driver = webdriver.Chrome(PATH) # I can include "chrome_options" as a second parameter to prevent window from opening)


###########################################################################################
#
#   PART 2: Accessing Wikipedia
#   2.1. Accessing Wikipedia page using function "get"
#   2.2. Waiting one second for the web browser to open the page
#   2.3. Creating a variable to receive the page element that refers to the search box
#   2.4. Using the method send_keys to write in the search box and press "enter"
#   2.5. Waiting one second so the web browser has enough time to change to another page
#   2.6. Saving xpath in a variable
#   2.7. Using the method send_keys to write in the search box
#   2.8. Waiting one second for the web browser to open the page
#   2.9. Printing the first paragraph in the page
#   2.10. Closing the driver
#
###########################################################################################


# PART 2.1. Accessing Wikipedia page using function "get"
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# PART 2.2. Waiting one second for the web browser to open the page
time.sleep(1)

# PART 2.3. Creating a variable to receive the page element that refers to the search box
search_input=driver.find_element_by_xpath('//*[@id="searchInput"]')
# To create this link, click with the right button then inspect/select an element in the page/copy xpath

# PART 2.4. Using the method send_keys to write in the search box and press enter
search_input.send_keys("Aristotle")

# Pressing enter
search_input.send_keys(Keys.ENTER)

# PART 2.5. Waiting one second so the web browser has enough time to change to another page
time.sleep(1)

# PART 2.6. Saving xpath in a variable
found = driver.find_element_by_xpath("//*[@id='mw-content-text']/div[3]/ul/li[1]/div[1]/a")

# PART 2.7. Using the method send_keys to write in the search box
found.click()

# PART 2.8. Waiting one second for the web browser to open the page
time.sleep(1)

# PART 2.9.Printing the first paragraph in the page

first_paragraph=driver.find_element_by_xpath("//*[@id='mw-content-text']/div[1]/p[3]")
print(first_paragraph.get_attribute("innerText"))

# PART 2.10. Closing the driver

#driver.close()



