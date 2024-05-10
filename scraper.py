import requests
from bs4 import BeautifulSoup


#function to scrape data from the provided URL
def scrape_product_data(url):
    #send GET request to the URL
    response = requests.get(url)
    
    #check if the request was successful (status code 200)
    if response.status_code == 200:
        #Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        #Extract relevant information
        product_price = soup.find('span', class_='price--withoutTax').text.strip()
        
        print("Price:", product_price)
        
    else:
        print("FAIL", response.status_code)
        
#URL 

card_name = input("Card Name: ")
card_number = input("Card Number: ")
card_type = input("Card Type (Full Art Borderless ect.): ")

    
set_name = input("Full Set Name: ")

card_name = card_name.replace(" ", "-")
card_type = card_type.replace(" ", "-")
set_name = set_name.replace(" ", "-")

# Construct the URL
url = f"https://www.facetofacegames.com/{card_name}-{card_number}"
if card_type:
    url += f"-{card_type}"
if set_name:
    url += f"-{set_name}"
url += "/"
print("URL: ", url)
     
     
scrape_product_data(url)
