# Order.py
from Menu import menu, show_menu
orders = []
def add_order():
    show_menu()
    # نام محصول مورد نظر 
    product_name = input("Enter product name (coffee/tea/cake): ").strip().lower()
    if product_name not in menu:
        # این محصول در منو وجود ندارد
        print(" sorry this product is not available in the menu.")
        return
    try:
        # وارد کردن تعداد محصول مورد نظر
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            # تعداد باید بزرگتر از صفر باشد
            print("quantity must be greater than zero.")
            return
    except ValueError:
        # وارد کردن یک عدد معتبر
        print("please enter a valid number.")
        return
    order_item = {
        "name": product_name,
        "price": menu[product_name],
        "quantity": quantity
    }                
    orders.append(order_item)
    # با موفقیت به سفارش ها اضافه شد
    print(f"{quantity} {product_name.capitalize()}added successfully.")
def show_orders():
    if not orders:
        #هنوز سفارشی ثبت نشده است 
       print("\n no orders have been placed yet.")    
    return
    #سفارش های ثبت شده 
    print("\n========== Placed orders ==========")
    for index, order in enumerate(orders, start = 1):
        total_item_price = order['price'] * order['quantity']
        print(f"{index}.Item:{order['name'].capitalize()} |qty: {order['quantity']} | Total: {total_item_price:,} Toman")
    print("=======================================")