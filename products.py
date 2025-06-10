products = {
    "101": {"name": "T-shirt", "price": 299},
    "102": {"name": "Jeans", "price": 799},
    "103": {"name": "Jacket", "price": 1499},
    "104": {"name": "Shoes", "price": 999},
}

def display_products():
    print("\nAvailable Products:")
    for pid, info in products.items():
        print(f"{pid} - {info['name']} - ₹{info['price']}")

def get_product(pid):
    return products.get(pid)
