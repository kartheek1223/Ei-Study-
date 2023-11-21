#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Product:
    def __init__(self, name, price, available):
        self.name = name
        self.price = price
        self.available = available

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_item(self, cart_item):
        self.items.append(cart_item)
        self.update_total_price()

        update_choice = input(f"Do you want to update the quantity of {cart_item.product.name}? (yes/no): ")
        if update_choice.lower() == 'yes':
            new_quantity = int(input(f"Enter the new quantity for {cart_item.product.name}: "))
            self.update_quantity(cart_item.product, new_quantity)

    def update_quantity(self, product, new_quantity):
        cart_item = next((item for item in self.items if item.product == product), None)
        if cart_item:
            cart_item.quantity = new_quantity
            self.update_total_price()
        else:
            print(f"Product {product.name} not found in the cart.")

    def remove_item(self, product):
        self.items = [item for item in self.items if item.product != product]
        self.update_total_price()

    def view_cart(self):
        print("Cart Items:")
        for cart_item in self.items:
            print(f"- {cart_item.quantity} x {cart_item.product.name}")
        print("Total Bill:")
        print(f"- Total Price: ${self.total_price:.2f}")

    def update_total_price(self):
        self.total_price = sum(item.product.price * item.quantity for item in self.items)

if __name__ == "__main__":
    products = [
        Product("Laptop", 1000, True),
        Product("Headphones", 50, True)
    ]

    cart = Cart()

    laptop_quantity = int(input("Enter the quantity of laptops "))
    laptop_item = CartItem(products[0], laptop_quantity)
    cart.add_item(laptop_item)

    headphones_quantity = int(input("Enter the quantity of headphones"))
    headphones_item = CartItem(products[1], headphones_quantity)
    cart.add_item(headphones_item)

    cart.view_cart()


# In[ ]:




