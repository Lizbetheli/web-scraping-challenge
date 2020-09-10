# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import time

def home():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape_info():




# Scrape mars news function 

def scrape_news():
    browser = home()

    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
        
    try:  
        article = soup.find('div', class_='list_text')   
        article_title = article.find('div', class_='content_title').text
        p_text = article.find('div', class_='article_teaser_body').text

    except AttributeError:
        return None, None
    
    browser.quit()
    
    return article_title, p_text