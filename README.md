# Web Scraping with Python: using Selenium and Beautiful Soup

Script of two Scraping Bots in Python using Selenium and Beautiful Soup Scraping Libraries.

## Files

* main.py -> Scraping Bot to access Google page and write "wikipedia english" in the search box. I used Beautiful Soup tool for extracting data from the web page. The goal is to print all the titles and the respective links. 
* aristotle.py -> Scraping Bot to access Wikipedia main page then write Aristotle in the search box. The goal was to print the first paragraph of the page, which describe who was Aristotle. 

## Approach (main.py)  

This file contains a Scraping Bot to access Google page and write "wikipedia english" in the search box. I used Beautiful Soup tool for extracting data from the web page. The goal is to print all the titles and the respective links. 

Here are the steps I followed for scraping:

#####   Part 1: Initializations
    1.1. Preventing the browser window from opening
    1.2. Localizing the driver
    1.3. Configuring the driver so that selenium can manipulate the navigator

#####   Part 2: Accessing Google
    2.1. Accessing Google page using function "get"
    2.2. Waiting one second for the web browser to open the page
    2.3. Creating a variable to receive the page element that refers to the search box
    2.4. Using the method send_keys to write in the search box and press "enter"
    2.5. Waiting one second so the web browser has enough time to change to another page
    2.6. Identifying the current page using method current_url
    2.7. Tell the driver that I'm no longer in the google page, I am in an specific page
    2.8. Identify the page source
    2.9. Automatically closing the window


#####   Part 3: Accessing Google
    3.1. Accessing Google page using function "get"
    3.2. Using method "find" in three steps
    3.3. Getting part of the tag
    3.4. Using method find all
    3.5. Using For Loop because the content is a set
    3.6. Closing the browser 
    
## Approach (aristotle.py)  

This file contains a Scraping Bot to access Wikipedia main page then write Aristotle in the search box. The goal was to print the first paragraph of the page, which describe who was Aristotle. 

#####   Part 1: Initializations
    1.1. Preventing the browser window from opening
    1.2. Localizing the driver
    1.3. Configuring the driver so that selenium can manipulate the navigator

#####   Part 2: Accessing Wikipedia
    2.1. Accessing Wikipedia page using function "get"
    2.2. Waiting one second for the web browser to open the page
    2.3. Creating a variable to receive the path for the search box
    2.4. Using the method send_keys to write in the search box and press "enter"
    2.5. Waiting one second so the web browser has enough time to change to another page
    2.6. Saving xpath in a variable
    2.7. Using the method send_keys to write in the search box
    2.8. Waiting one second for the web browser to open the page
    2.9. Printing the first paragraph in the page
    

### Resources

 The following articles were a helpful reference for this project:

 Gray, Dave (Apr, 2018) Better web scraping in Python with Selenium, Beautiful Soup, and pandas. Available from: https://www.freecodecamp.org/news/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251/

 Sahin, Kevin (Feb, 2021) Web Scraping using Selenium and Python. Available from: https://www.scrapingbee.com/blog/selenium-python/

 Sahin, Kevin (Mar, 2021) Web Scraping 101 with Python. Available from: https://www.scrapingbee.com/blog/web-scraping-101-with-python/


