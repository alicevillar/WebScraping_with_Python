# Web Scraping using Selenium and Python 

This is a small personal project of a Scraping Bot with Selenium and Python. 

### Files

* main.py -> Scraping Bot to access Google page and write "wikipedia english" in the search box. I used Beautiful Soup tool for extracting data from the web page. The goal is to print all the titles and the respective links. 
* aristotle.py -> Scraping Bot to access Wikipedia main page then write Aristotle in the search box. The goal was to print the first paragraph of the page, which describe who was Aristotle. 

### Approach (main.py)  

Scraping Bot to access Google page and write "wikipedia english" in the search box. I used Beautiful Soup tool for extracting data from the web page. The goal is to print all the titles and the respective links.


### Approach (aristotle.py)  

*   PART 1: Initializations
    1.1. Preventing the browser window from opening
    1.2. Localizing the driver
    1.3. Configuring the driver so that selenium can manipulate the navigator

*   PART 2: Accessing Wikipedia
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

Sahin, Kevin (Feb, 2021) Web Scraping using Selenium and Python. Available from: https://www.scrapingbee.com/blog/selenium-python/

Sahin, Kevin (Mar, 2021) Web Scraping 101 with Python. Available from: https://www.scrapingbee.com/blog/web-scraping-101-with-python/
