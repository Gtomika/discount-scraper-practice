from category import DiscountCategory
from bs4 import ResultSet

from item import DiscountedItem
from config import DiscountsConfig

def process_category(category: DiscountCategory, categoryElement: ResultSet, itemClass: str):
    print('Starting to process category: ' + category.category_name)

    for discountItemElement in categoryElement.find_all('div', { 'class': itemClass }):
        product_name = discountItemElement.find('h3').get_text()
        discounted_item = DiscountedItem(product_name)
        category.add_discounted_item(discounted_item)
        print('Found discounted item: ' + discounted_item.product_name)
