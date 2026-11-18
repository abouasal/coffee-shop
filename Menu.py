#Menu.py
menu = {
    "coffee":70000,
    "tea":50000,
    "cake":150000
}
def show_menu():
    print("\n====== Coffee Menu =====")
    for product, price in menu.items():
        print(f"- {product.capitalize()}: {price:,} Toman ")
        print("=====================")
