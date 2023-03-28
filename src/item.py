class DiscountedItem:

    def __init__(self, product_name) -> None:
        self.product_name = product_name

    def __str__(self) -> str:
        return self.product_name
