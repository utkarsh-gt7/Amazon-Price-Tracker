import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.in/Marshall-Stanmore-Wireless-Bluetooth-Speaker/dp/B07HPP2DMM/ref=sr_1_4?crid=1U5OIF8L1UUAN&" \
      "keywords=marshall+stanmore+2&qid=1678110375&sprefix=%2Caps%2C699&sr=8-4"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,pa;q=0.7,hi;q=0.6",
}

MY_EMAIL = "8singhutkarsh8@gmail.com"
MY_PASSWORD = "nyfuvimrodnzhrcq"

response = requests.get(url=URL, headers=HEADERS)
response_page = response.text

soup = BeautifulSoup(response_page, "html.parser")
price_tags_list = soup.find_all(name="span", class_="a-price-whole")
product_title = (str((soup.find(name="span", id="productTitle")).getText())).strip()

price_list = [tag.getText() for tag in price_tags_list]
product_price_split = (price_list[0].split(","))
product_price_float = float(product_price_split[0] + product_price_split[1])
print(product_price_float)
print(product_title)

if product_price_float < 35000.0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
              from_addr=MY_EMAIL,
              to_addrs=MY_EMAIL,
              msg="Subject: Amazon Price Alert!\n\n"
                  f"{product_title} is now being sold at INR {product_price_float}\n"
                  f"{URL}"
        )
