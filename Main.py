from Amazon_Config import (
    get_webdriver_options,
    get_chrome_webdriver,
    set_browser_as_icognito,
    ignore_certificate_errors,
    Name_of_Product,
    Currency,
    filters,
    Base_URL,
    headers

)

import time
import csv
import os
import numpy as np
import glob
import plotly.graph_objects as go
from bs4 import  BeautifulSoup
import requests
import matplotlib.pyplot as plot
import datetime
import smtplib
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class AmazonAPI:
    def __init__(self, search_item, filters, base_url, currency):
        self.base_url = base_url
        self.search_item = search_item
        options = get_webdriver_options()
        ignore_certificate_errors(options)
        set_browser_as_icognito(options)
        self.driver = get_chrome_webdriver(options)
        self.currency = Currency
        self.price_filter = f"&rh=p_36%3A{filters[ 'min' ]}00-{filters[ 'max' ]}00"

    def run(self):
        print("Starting Script..........")
        print(F"Looking for {self.search_item} products....")
        links = self.get_product_links()
        products = self.get_products_info(links)
        self.driver.quit()
        if products.empty:
            print("No products found!!")
            return 0
        Des_prod = int(input("Enter the index no. of your favourite product "))
        Des_Price = int(input(" Enter your desired price for the product"))
        print(f"{Base_URL}dp/{products.ID[Des_prod]}?language=en_GB")
        i=1
        ask = input("Do you want me to show you the price graph after every 2 hours?(Y or N)")
        price_after_few_minutes = products.Price[Des_prod]
        if price_after_few_minutes <= Des_Price:
            self.send_mail(Des_prod, products)
        else:
            while i==1:
                print("Mail will be sent to you when price falls down")
                i+=1
            #checking the price after every 60 seconds
            while (price_after_few_minutes> Des_prod):
                price_after_few_minutes = self.check_price(products, Des_prod, Des_Price,i, ask)
                time.sleep(7200)
            self.send_mail(Des_prod, products)
        pass

    def get_products_info(self, links):
        asins = self.get_asins(links)
        title = [ ]
        seller=[]
        price=[]
        id=[]
        df = pd.DataFrame()
        for asin in asins:
            product_shorten_URL = self.shorten_URL(asin)                            ##Shortening URL size
            self.driver.get(f'{product_shorten_URL}?language=en_GB')                ##Changing the language of the products
            store_title = self.get_title()                                          ##Getting the title of the products
            title.append(store_title)
            store_seller = self.get_seller()                                        ##Getting the seller of the product
            seller.append(store_seller)
            store_price = self.get_price()                                          ##Getting the price of the product
            if store_price != None:
                store_price = float(store_price[1:].replace(',',''))
            price.append(store_price)
            id.append(asin)
        pd.set_option('colheader_justify','center')
        ## Adding columns with particular product values to the Dataframe
        df[ "Product" ] = title
        df[ "Seller" ] = seller
        df['Price']=price
        df[ "ID" ] = id
        df["Product"] = df["Product"].str.pad(15, side = 'left')
        df['Price'] = df['Price'].replace(np.nan, 'Not available')
        print(df)
        return df

    #Function to get the title of products
    def get_title(self):
        try:
            return self.driver.find_element_by_id('productTitle').text
        except Exception as e:
            print(e)
            print(f"Cant get title of a product -{self.driver.current_url}")
            return None

    #function to get the seller of the products
    def get_seller(self):
        try:
            return self.driver.find_element_by_id('sellerProfileTriggerId').text
        except Exception as e:
            print(e)
            print(f"Cant get seller of the product- {self.driver.current_url}")
            return None

    #function to get the price of the products
    def get_price(self):
        price = None
        try:
            price = self.driver.find_element_by_id('priceblock_ourprice').text
        except NoSuchElementException:
            try:
                availability = self.driver.find_element_by_id('availability').text
                if 'Available' in availability:
                    price = self.driver.find_element_by_class_name('olp-padding-right').text
                    price = price[ price.find(self.currency): ]
            except NoSuchElementException:
                try:
                    price = self.driver.find_element_by_id('priceblock_dealprice').text
                except Exception as e:
                    print(e)
                    print(f"Can't get price of a product - {self.driver.current_url}")
                    return None
            except Exception as e:
                print(e)
                print(f"Can't get price of a product - {self.driver.current_url}")
                return None
        except Exception as e:
            print(e)
            print(f"Can't get price of a product - {self.driver.current_url}")
            return None
        return price

    #function to shorten the URL
    def shorten_URL(self, asin):
        return self.base_url + 'dp/' + asin

    def get_asins(self, links):
        return [ self.get_asin(link) for link in links ]

    def get_asin(self, product_link):
        return product_link[ product_link.find('/dp/') + 4:product_link.find('/ref') ]

    #Getting the links of all the products from the searched product page
    def get_product_links(self):
        self.driver.get(self.base_url)
        elements = self.driver.find_element_by_id("twotabsearchtextbox")
        elements.send_keys(self.search_item)
        elements.send_keys(Keys.ENTER)
        self.driver.get(f"{self.driver.current_url}{self.price_filter}")
        print(self.driver.current_url)
        result_list = self.driver.find_element_by_class_name('s-main-slot')
        links = [ ]
        try:
            results = result_list.find_elements_by_xpath(
                "//div/div/span/div/div/div/div/div[1]/div/div/div/span/a")
            links = [ link.get_attribute('href') for link in results ]
            return links
        except Exception as e:
            print("Didn't get any products.....")
            print(e)
            return links

    # Mail tracking

    ##Function to check the price the product that if it comes under the desired price
    def check_price(self, df, Des_prod, Des_Price, i,ask):
        url = f'{Base_URL}dp/{df.ID[ Des_prod ]}'
        page = requests.get(url, headers=headers)

        bs = BeautifulSoup(page.content, 'html.parser')

        product_price = bs.find(id="priceblock_ourprice").get_text()

        price_float = float(product_price[1:].replace(',',''))
        file_exists = True
        if not os.path.exists("./price.csv"):
            file_exists = False

        with open("price.csv", "a") as file:
            writer = csv.writer(file, lineterminator="\n")
            fields = [ "Timestamp", "price" ]

            if not file_exists:
                writer.writerow(fields)

            timestamp = f"{datetime.datetime.date(datetime.datetime.now())},{datetime.datetime.time(datetime.datetime.now())}"
            writer.writerow([ timestamp, price_float ])
        prod = glob.glob("*.csv", recursive=True)
        filename = prod[ 0 ]

        graph= pd.read_csv(filename)

        fig = go.Figure([ go.Scatter(x=graph[ 'Timestamp' ], y=graph[ 'price' ], fill='tozeroy') ], )
        fig.update_xaxes(title="Timeline", showticklabels=False)
        fig.update_yaxes(title="Price")
        fig.update_layout(title=filename[ 2:-4 ])
        if ask=='Y' or ask=='y':
            fig.show()
        print(price_float)
        return price_float

    ##function to send the mail if the product price is under the desired product price
    def send_mail(self, Des_prod, df):
        URL = Base_URL + 'dp/' + df.ID[ Des_prod ] + "?language=en_GB"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('','')
        subject = 'Price fell down!'
        body = f"check the amazon link : {URL}"
        msg = f"Subject : {subject} \n\n {body}"
        server.sendmail(
            '',
            '',
             msg
        )
        print("Hey, the product is under your desired price and the mail has been sent, Check it out!!!")
        server.quit()


# Main Function

if __name__ == '__main__':
    print("Hey!!")
    amazon = AmazonAPI(Name_of_Product, filters, Base_URL, Currency)
    amazon.run()
