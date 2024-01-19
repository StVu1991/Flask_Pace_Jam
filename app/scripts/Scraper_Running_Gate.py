# app/scripts/ScraperRunningGate.py

import requests
from bs4 import BeautifulSoup

class RunningGateScraper:
    def __init__(self, url):
        self.url = url

def calculate_num_pages(base_url):
    first_page_url = f"{base_url}?p=1"
    response = requests.get(first_page_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Extracting the total number of products
    total_products_element = soup.find('span', class_='toolbar-number')
    total_products = int(total_products_element.text.strip())

    # Set the number of products per page
    products_per_page = 36  # Adjust this based on your actual case

    # Calculate the number of pages
    num_pages = (total_products + products_per_page - 1) // products_per_page

    return num_pages

def extract_manufacturer(shoe_name):
    return shoe_name.split()[0]

def scrape_shoes_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Example: Extracting shoe names and URLs
    product_items = soup.select('.product-item-info')

    shoe_data = []
    for item in product_items:
        shoe_name = item.find('a', class_='product-item-link').text.strip()
        shoe_url = item.find('a', class_='product-item-link')['href']
        manufacturer = extract_manufacturer(shoe_name)
        
        shoe_data.append({'manufacturer': manufacturer, 'name': shoe_name, 'url': shoe_url})
    
    print (shoe_data)

def loop_all_subpages(base_url):
    num_pages = calculate_num_pages(base_url)
    print(num_pages)

    for page in range(1, num_pages + 1):
        url = f"{base_url}?p={page}"
        scrape_shoes_data(url)
    


if __name__ == "__main__":
    base_url = 'https://runninggate.hr/muskarci/obuca/trcanje.html'

    all_mens_shoes = loop_all_subpages(base_url)