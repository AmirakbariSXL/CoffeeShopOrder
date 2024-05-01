import tkinter as tk

class CoffeeShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Shop Order")

        # Initialize the list to store orders
        self.orders = []

        # Create GUI elements
        self.label = tk.Label(root, text="Welcome to Our Coffee Shop!")
        self.label.pack()

        self.drink_entry = tk.Entry(root, width=20)
        self.drink_entry.insert(0, "Coffee/Tea")
        self.drink_entry.pack()

        self.size_entry = tk.Entry(root, width=20)
        self.size_entry.insert(0, "Small/Medium/Large")
        self.size_entry.pack()

        self.extras_entry = tk.Entry(root, width=20)
        self.extras_entry.insert(0, "Extras (e.g., vanilla syrup)")
        self.extras_entry.pack()

        self.order_button = tk.Button(root, text="Place Order", command=self.place_order)
        self.order_button.pack()

    def place_order(self):
        drink = self.drink_entry.get()
        size = self.size_entry.get()
        extras = self.extras_entry.get()

        # Calculate price based on drink and size (you can adjust prices as needed)
        price = 0
        if drink.lower() == "coffee":
            if size.lower() == "small":
                price = 2.50
            elif size.lower() == "medium":
                price = 3.50
            elif size.lower() == "large":
                price = 4.50
        elif drink.lower() == "tea":
            # Similar logic for tea prices
            pass

        # Add extras cost
        if "vanilla" in extras.lower():
            price += 1

        # Add order to the list
        self.orders.append({"drink": drink, "size": size, "extras": extras, "price": price})
        print(f"Order placed: {drink} ({size}), Extras: {extras}, Total Price: ${price:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CoffeeShopApp(root)
    root.mainloop()
