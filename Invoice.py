class Invoice:

    def __init__(self):
        self.items = {}

    def addProduct(self, qnt, price, discount):
        self.items['qnt'] = qnt
        self.items['unit_price'] = price
        self.items['discount'] = discount
        return self.items

    def totalImpurePrice(self, products):
        total_impure_price = 0
        for k, v in products.items():
            total_impure_price += float(v['unit_price']) * int(v['qnt'])
        total_impure_price = round(total_impure_price, 2)
        return total_impure_price

    def totalDiscount(self,products):
        total_discount = 0
        for k, v in products.items():
            total_discount += (int(v['qnt']) * float(v['unit_price']) * float(v['discount'])) / 100
        total_discount = round(total_discount, 2)
        return total_discount

    def totalPurePrice(self, products):
        total_pure_price = self.totalImpurePrice(products) - self.totalDiscount(products)
        return total_pure_price

    def totalPurePricePerProduct(self, products):
        quantity = 0
        for k, v in products.items():
            quantity += int(v['qnt']);
        total_pure_price_per_product = self.totalPurePrice(products)/quantity
        return total_pure_price_per_product

    def totalImpurePricePerProduct(self, products):
        quantity = 0
        for k, v in products.items():
            quantity += int(v['qnt']);
        total_impure_price_per_product = self.totalImpurePrice(products)/quantity
        return total_impure_price_per_product

    def inputAnswer(self, input_value):
        while True:
            userInput = input(input_value)
            if userInput in ['y', 'n']:
                return userInput
            print("y or n! Try again.")

    def inputNumber(self, input_value):
        while True:
            try:
                userInput = float(input(input_value))
            except ValueError:
                print("Not a number! Try again.")
                continue
            else:
                return userInput
