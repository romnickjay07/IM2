def display_cart(cart):
    print("\nDisplaying Values")
    print("Key      Value")
    for key, value in cart.items():
        print(f"{key:<8} {value}")
    print()

def main():
    cart = {}
    size = 3
    for i in range(size):
        item = input(f"Shopping items{i+1}: ")
        cart[i] = item

    print(f"\nYou have {size} items in the cart\n")

    while True:
        action = input("What would you like to do [C]hange items [R]emove [D]isplay  [S]earch ? ").strip().lower()

        if action == "d":  
            display_cart(cart)

        elif action == "s": 
            search_value = input("Enter item to search: ")
            found = False
            for key, value in cart.items():
                if value.lower() == search_value.lower():
                    print(f"Found {value} item\n")
                    found = True
                    break
            if not found:
                print("I'm sorry, not in the cart\n")

        elif action == "r":
            try:
                key = int(input("Enter key to search: "))
                if key in cart:
                    print(f"The key {key} with value {cart[key]} has been deleted\n")
                    del cart[key]
                else:
                    print("Key not found\n")
            except ValueError:
                print("Key not found (must be a number)\n")

        elif action == "c": 
            try:
                key = int(input("Enter key to search: "))
                if key in cart:
                    print(f"Found {cart[key]} item")
                    new_value = input("Enter value: ")
                    cart[key] = new_value
                    print()
                else:
                    print("I'm sorry, not in the cart\n")
            except ValueError:
                print("Key not found (must be a number)\n")

        elif action == "*":
            print("Bye")
            break

        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
