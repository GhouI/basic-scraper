import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from discord import DiscordHook

url = ""
webhook_url = ""
# Initial content of the website
initial_content = ""

# Set up a Selenium WebDriver to handle JavaScript and cookies
driver = webdriver.Chrome()  

while True:
    # Use Selenium to load the webpage with JavaScript and cookies enabled
    driver.get(url)
    time.sleep(5)  # Allow time for dynamic content to load
    
    # Get the page source after JavaScript execution
    page_source = driver.page_source
    
    # Parse the HTML content of the website using Beautiful Soup
    soup = BeautifulSoup(page_source, 'html.parser')
    current_content = soup.get_text()
    
    # Check if the content has changed
    if current_content != initial_content:
        # Update the initial content
        initial_content = current_content
        
        # Send a message to Discord webhook
        discord_hook = DiscordHook(webhook_url)
        discord_hook.send_Message("Content of the website")
        print(current_content)
        
    else:
        print("No changes detected. Nope, nothing changed.")
    
    # Wait for 2 minutes before checking again
    time.sleep(120)

# Close the Selenium WebDriver after scraping is done
driver.quit()
