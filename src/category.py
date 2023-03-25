from item import DiscountedItem

class DiscountCategory:

    def __init__(self, category_name) -> None:
        self.category_name = category_name
        self.discounted_items = []
    
    def add_discounted_item(self, item: DiscountedItem):
        self.discounted_items.append(item)

    def __str__(self) -> str:
        category_str = f'{self.category_name}:\n'
        for item in self.discounted_items:
            category_str += f' - {str(item)}\n'
        return category_str
