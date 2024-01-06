import requests
from bs4 import BeautifulSoup
import json
import time
import pandas as pd

# URL of the website you want to scrape
url_template = "https://www.flipkart.com/search?q=iphone&page={}"

# Make an HTTP request to the website

main_product = []
names = []
ratings = []
prices = []
others = []



for page_number in range(1, 6):  # Assuming you want to scrape the first 5 pages
    time.sleep(1)
    url = url_template.format(page_number)
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # print(soup)
        
    

        # Extract information from the page
        # For demonstration purposes, let's find and print all the links on the page
        try:
            data = soup.find_all('div',class_='_1AtVbE')
            price = soup.find_all('div', class_='_30jeq3 _1_WHN1')
            
            price = str(price).split('>')
            # print(price)

            # if(len(price)>1):
            #     price = price[1].split('<')
            #     price = price[0]
                    
            # print(price)
                
            for i in range(1,len(price),2):
                temp = price[i].split('<')[0]
                prices.append(temp)
            # print(prices)
            
            num=0
            
            for i in data:
                name = i.find('div',class_='_4rR01T')
                s = str(name)
                temp = ""
                s = s.split('>')
                if(len(s)>1):
                    t = s[1].split('<')
                    temp = t[0]
                    
                
                    
                rating = i.find('span',class_='_2_R_DZ')
                rating = str(rating).split('>')
                if len(rating)>3:
                    rating = rating[3].split('\xa0')[0]

                # price = soup.find('span',class_='_25b18c')
                # print(price)
                
                if(name!=[''] and rating != ['None']):
                    # names.append(temp)
                    # ratings.append(rating)
                    main_product.append({'name':temp,
                                    'rating':rating,
                                    'price':prices[num],
                                    #  'other':other
                                    })
                    num=num+1
                    
                
                
            
            
        except Exception as e:
            print(f"error occured : {e}")
    

    
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    
df = pd.DataFrame(main_product)
print(df)

