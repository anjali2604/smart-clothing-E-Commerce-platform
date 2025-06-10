from users import login, register
from products import display_products
from cart import Cart

def main():
    print("Welcome to Smart Clothing Store")
    user = None
    while not user:
        choice = input("1. Register\n2. Login\nChoose option: ")
        if choice == '1':
            user = register()
        elif choice == '2':
            user = login()

    cart = Cart()
    while True:
        print("\n1. View Products\n2. Add to Cart\n3. View Cart\n4. Checkout\n5. Exit")
        option = input("Choose option: ")

        if option == '1':
            display_products()
        elif option == '2':
            pid = input("Enter Product ID to add: ")
            qty = int(input("Enter quantity: "))
            cart.add_to_cart(pid, qty)
        elif option == '3':
            cart.view_cart()
        elif option == '4':
            cart.checkout(user)
        elif option == '5':
            print("Thank you for visiting!")
            break
        else:
            print("Invalid option")

if _name_ == "_main_":
    main()
