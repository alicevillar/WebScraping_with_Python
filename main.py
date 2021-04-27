from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


# To prevent window from opening: use module Options

# If I wanted to create a object of the class Options
chrome_options = Options()
#chrome_options.add_argument("--headless")

# Localing the driver
PATH = "C://Drivers/chromedriver.exe"

# configurating driver so that selenium can manipulate the navigator
driver = webdriver.Chrome(PATH,options=chrome_options) # this second parameter is optional (to prevent window from opening)

# accessing google page using function "get"
driver.get("http://google.com")

#waiting one second for the web broser open the page
time.sleep(1)

# variável criada para referenciar o elemento da página que se refere a caixa de pesquisa
search_input = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
# Para esse link, cliquei o google/inspecionar/select an element in the page to inspect it

# Using the method send_keys, which is aimed to write in the search box
search_input.send_keys("wikipedia english")

# Using usando method send_keys to press ENTER
search_input.send_keys(Keys.ENTER)

#waiting one second so the web broser has enough time to change to another page
time.sleep(1)

# Identify the current page using method current_url
page_url = driver.current_url

# Now I have to tell the driver that I'm no longer in the google page, I am in an specific page
driver.get(page_url)

# Identify the page source
page_source = driver.page_source
# print(page_source)

# Automaticaly closing the window
driver.quit()

# USAR BEAUTIFUL SOUP PARA MINERAR OS DADOS, escolher o que quero da [ágina

# Creating an object of BS. There 2 parameters. The first contains the page source and the second is aimed to
# parser is an algorithm that can read a content and turn it into a programming object
soup = BeautifulSoup(page_source, "html.parser")

# Using method "find" in three steps: - to find the div, then the tag h3, and finally the h3's content
soup.find("div", {"class": "tF2Cxc"}).find("h3").find(text=True)
# Using method "find" the link
soup.find("div", {"class": "tF2Cxc"}).find("a")
# Printing
print(soup.find("div", {"class": "tF2Cxc"}).find("a"))
# Now, how to get part of the tag? Write the name of the attribute you want
print(soup.find("div", {"class": "tF2Cxc"}).find("a")['href'])

# Using method "find all"
result_list = soup.find_all("div",
                            {"class": "tF2Cxc"})  # inside this class are all the elements I need (tag h3 and tag a)

# using For Loop because the content is a set
for r in result_list:
    # printing titles
    print(r.find("h3").find(text=True))  # will print all the divs with this class tF2Cxc
    # printing links
    print(r.find("a")['href'])


driver.close()


