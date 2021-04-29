from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

###########################################################################################
#
#   PART 1: Initializations
#   1.1. Preventing the browser window from opening
#   1.2. Localizing the driver
#   1.3. Configuring the driver so that selenium can manipulate the navigator
#
###########################################################################################

# PART 1.1. Preventing the browser window from opening

# Create an object of the class Options and adding the argument --headless to invoke Chrome in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# PART 1.2 - Localizing the driver
# Setting the path
PATH = "C://Drivers/chromedriver.exe"

# PART 1.3 - Configuring the driver so that selenium can manipulate the navigator
driver = webdriver.Chrome(PATH,options=chrome_options) # I can include "chrome_options" as a second parameter to prevent window from opening)

###########################################################################################
#
#   PART 2: Accessing Google page
#   2.1. Accessing Google page using function "get"
#   2.2. Waiting one second for the web browser to open the page
#   2.3. Creating a variable to receive the page element that refers to the search box
#   2.4. Using the method send_keys to write in the search box and press "enter"
#   2.5. Waiting one second so the web browser has enough time to change to another page
#   2.6. Identifying the current page using method current_url
#   2.7. Tell the driver that I'm no longer in the google page, I am in an specific page
#   2.8. Identify the page source
#   2.9. Automatically closing the window
#
###########################################################################################

# PART 2.1. Accessing Wikipedia page using function "get"
driver.get("http://google.com")

# PART 2.2. Waiting one second for the web browser to open the page
time.sleep(1)

# PART 2.3. Page element that refers to the search box
search_input = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
# To create this link, click with the right button then inspect/select an element in the page/copy xpath

# PART 2.4. Using the method send_keys to write in the search box and press enter
search_input.send_keys("wikipedia english")

# Using method send_keys to press ENTER
search_input.send_keys(Keys.ENTER)

# PART 2.5. Waiting one second so the web browser has enough time to change to another page
time.sleep(1)

# PART 2.6. Identifying the current page using method current_url
page_url = driver.current_url

# PART 2.7. Tell the driver that I'm no longer in the google page, I am in an specific page
driver.get(page_url)

# PART 2.8. Identify the page source
page_source = driver.page_source
# print(page_source)

# Automatically closing the window
driver.quit()


###########################################################################################
#
#   PART 3: Web Scrapping with Beautiful Soup
#   3.1. Accessing Google page using function "get"
#   3.2. Using method "find" in three steps
#   3.3. Getting part of the tag
#   3.4. Using method find all
#   3.5. Using For Loop because the content is a set
#   3.6. Closing the browser

###########################################################################################

# PART 3.1. Using Beautiful Soup to choose what I want from the page
# Creating an object of BS. There 2 parameters. The first contains the page source and the second is parser
# parser is an algorithm that can read content and turn it into a programming object
soup = BeautifulSoup(page_source, "html.parser")

# PART 3.2. Using method "find" in three steps: a) to find the div, b) the tag h3, and c) the h3's content
soup.find("div", {"class": "tF2Cxc"}).find("h3").find(text=True)

# PART 3.3. Using method "find" to get the link and print
soup.find("div", {"class": "tF2Cxc"}).find("a")
# Printing
print(soup.find("div", {"class": "tF2Cxc"}).find("a"))

# PART 3.3. Getting part of the tag

# How to get part of the tag? Write the name of the attribute you want
print(soup.find("div", {"class": "tF2Cxc"}).find("a")['href'])

# PART 3.4.Using method find all
result_list = soup.find_all("div", {"class": "tF2Cxc"})  # inside this class are all the elements I need (tag h3 and tag a)

# PART 3.5. Using For Loop because the content is a set
for r in result_list:
    # printing titles
    print(r.find("h3").find(text=True))  # will print all the divs with this class tF2Cxc
    # printing links
    print(r.find("a")['href'])

# PART 3.6. Closing the browser
driver.close()


