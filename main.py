from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

#Localing the driver
PATH="C://Drivers/chromedriver.exe"

#configurating driver so that selenium can manipulate the navigator
driver=webdriver.Chrome(PATH)

# accessing google page using function "get"
driver.get("http://google.com")

#variável criada para referenciar o elemento da página que se refere a caixa de pesquisa
search_input=driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
#Para esse link, cliquei o google/inspecionar/select an element in the page to inspect it

#Using the method send_keys, which is aimed to write in the search box
search_input.send_keys("wikipedia english")

#Using usando method send_keys to press ENTER
search_input.send_keys(Keys.ENTER)

# Identify the current page using method current_url
page_url=driver.current_url

#Now I have to tell the driver that I'm no longer in the google page, I am in an specific page
driver.get(page_url)

#Identify the page source
page_source=driver.page_source
#print(page_source)

#Automaticaly closing the window
driver.quit()

# USAR BEAUTIFUL SOUP PARA MINERAR OS DADOS, escolher o que quero da [ágina

#Creating an object of BS. There 2 parameters. The first contains the page source and the second is aimed to
# parser is an algorithm that can read a content and turn it into a programming object

soup=BeautifulSoup(page_source,"html.parser")



