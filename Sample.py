class ItemToPurchase:
    """Represents a single item available for purchase."""
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description


class ShoppingCart:
    """Manages a collection of items in a user's shopping cart."""
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        """Appends an ItemToPurchase object to the cart list."""
        self.cart_items.append(item_to_purchase)
        print("*** Item has been added ***")

    def remove_item(self, target_name):
        """Removes an item by name. Displays error if not found."""
        found = False
        for item in self.cart_items:
            if item.item_name == target_name:
                self.cart_items.remove(item)
                found = True
                break
        
        if not found:
            print("Item not found in cart. Nothing removed.")
        else:
            print("*** Item has been removed ***")

    def modify_item(self, modified_item):
        """Updates attributes of an existing item if they are not default."""
        found = False
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                found = True
                # Check for non-default values before updating
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                if modified_item.item_price != 0.0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                break
        
        if not found:
            print("Item not found in cart. Nothing modified.")
        else:
            print("*** Item has been modified ***")

    def get_num_items_in_cart(self):
        """Calculates total quantity of all items combined."""
        total_qty = 0
        for item in self.cart_items:
            total_qty += item.item_quantity
        return total_qty

    def get_cost_of_cart(self):
        """Calculates total cost of all items combined."""
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.item_price * item.item_quantity)
        return total_cost

    def print_total(self):
        """Prints the formatted total checkout summary."""
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        print() # Visual spacing

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                cost = int(item.item_price * item.item_quantity)
                print(f"{item.item_name} {item.item_quantity} @ ${int(item.item_price)} = ${cost}")
        
        print() # Visual spacing
        print(f"Total: ${int(self.get_cost_of_cart())}")

    def print_descriptions(self):
        """Prints the description summary for all items."""
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print() # Visual spacing
        print("Item Descriptions:")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


def print_menu(cart_object):
    """Displays the user menu loop and processes selections."""
    menu_text = (
        "\n********** MENU **********\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
        "**************************"
    )
    
    user_choice = ""
    while user_choice != 'q':
        print(menu_text)
        user_choice = input("Choose an option :").strip().lower()
        
        # Valid choice validation loop
        while user_choice not in ['a', 'r', 'c', 'i', 'o', 'q']:
            user_choice = input("Choose an option:\n").strip().lower()

        if user_choice == 'a':
            print("\n *** ADD ITEM TO CART ***")
            name = input("Enter the item name :").strip() 
            desc = input("Enter the item description :").strip() 
            price = float(input("Enter the item price $:"))
            qty = int(input("Enter the item quantity :"))
            
            new_item = ItemToPurchase(name, price, qty, desc)
            cart_object.add_item(new_item)

        elif user_choice == 'r':
            print("\n*** REMOVE ITEM FROM CART ***")
            target = input("Enter name of item to remove :").strip() 
            cart_object.remove_item(target)
        
        elif user_choice == 'c':
            print("\n*** CHANGE ITEM QUANTITY ***")
            target_name = input("Enter the item name :").strip() 
            new_qty = int(input("Enter the new quantity :"))
            
            # Construct item with default fields except name and quantity
            mod_item = ItemToPurchase(item_name=target_name, item_quantity=new_qty)
            cart_object.modify_item(mod_item)
            print("**************************\n")
            
        elif user_choice == 'i':
            print("\n*** OUTPUT ITEMS' DESCRIPTIONS ***")
            cart_object.print_descriptions()
            print("**************************\n")
            
        elif user_choice == 'o':
            print("\n*** OUTPUT SHOPPING CART ***")
            cart_object.print_total()
            print("**************************\n")


def main():
    """Main entry point to initialize cart and start menu."""
    cust_name = input("Enter customer's name :").strip() 
    current_dt = input("Enter today's date :").strip() 
    print(f"\nCustomer name: {cust_name}")
    print(f"Today's date: {current_dt}")
    
    # Initialize the custom cart
    user_cart = ShoppingCart(cust_name, current_dt)
    print_menu(user_cart)

if __name__ == "__main__":
    main()
