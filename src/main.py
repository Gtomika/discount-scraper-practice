import requests

import os.path as path
from bs4 import BeautifulSoup

from config import DiscountsConfig
from category import DiscountCategory
import category_processor
from send_email import DiscountEmailSender

config_path = path.join(path.dirname(__file__), '..', 'data', 'config.yaml')
config = DiscountsConfig(config_path)

# Fetch website of discounts
discountsUrl = config.get_config('inputs.discounts_url')
headers = config.get_config('inputs.headers')

print('Fetching discounts page from URL: ' + discountsUrl)
response = requests.get(discountsUrl, timeout=10, headers=headers)
if response.status_code != 200:
    print('Unexpected status code from discounts page: ' + str(response.status_code))
    exit(-1)

soup = BeautifulSoup(response.content, 'html.parser')
print('Discount page title is :' + soup.title.text)

categories = []

# Navigate to discount page in the DOM
discountsElementClass = config.get_config('inputs.discounts_element')
discountsItemClass = config.get_config('inputs.discount_item_element')

discountsElement = soup.find('div', { 'class': discountsElementClass })
for discountCategoryElement in discountsElement.find_all('div', recursive=False):
    # this is the DOM element of one category of discounts
    categoryTitle = discountCategoryElement.find('h2')
    category = DiscountCategory(categoryTitle.get_text())
    category_processor.process_category(category, discountCategoryElement, discountsItemClass)
    categories.append(category)

email_sender = DiscountEmailSender(config)
email_sender.send_discounts_mail(categories)
