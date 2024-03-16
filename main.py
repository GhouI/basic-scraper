import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from discord import DiscordHook
# Define the URL of the website to scrape
url = ""
# Define your Discord webhook URL
webhook_url = ""
# Initial content of the website
initial_content = ""

# Set up a Selenium WebDriver to handle JavaScript and cookies
driver = webdriver.Chrome()  # Use appropriate WebDriver for your browser

while True:
    # Use Selenium to load the webpage with JavaScript and cookies enabled
    driver.get(url)
    time.sleep(5)  # Allow time for dynamic content to load
    
    page_source = driver.page_source
    
    soup = BeautifulSoup(page_source, 'html.parser')

    classesToRemove = ['wrapper article-more2','fc-consent-root', 'mb-article-stickybar', 'baha_interactiveBtn']
    #Remove All the uneccessary divs 
    for class_to_remove in classesToRemove: 
        for div in soup.find_all('div', class_=class_to_remove):
            div.decompose()
    
    for AElement in soup.find_all('a', class_='open-app'):
        AElement.decompose()

    for section in soup.find_all('section', class_='cbox_msg2 C2'):
        section.decompose()
    
    current_content = "".join(soup.get_text().split())
    
    if current_content != initial_content:
        initial_content = current_content
        
        discord_hook = DiscordHook(webhook_url)
        discord_hook.send_Message("Content of the website"+current_content)
        
    else:
        print("No changes detected. Nope, nothing changed.")
    
    time.sleep(120)

# Close the Selenium WebDriver after scraping is done
driver.quit()
