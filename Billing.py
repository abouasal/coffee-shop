#Billing.py
from Order import orders
def calculate_total():
    total = 0 
    for order in orders:
        total += order["price"] * order["quantity"]
    return total 
def calculate_discount(total_amount):
    if total_amount > 1000000:
        discount = total_amount * 0.10
        return discount
    return 0
def  print_invoce():
    if not orders: 
        # سفارشی ثبت نشده است تا فاکتور صادر شود
        print("\n no orders to print invoice.")
        return
        # فاکتور نهایی
    print("\n ===== Invoice =====")
    total_amount = calculate_total()
    discount = calculate_discount(total_amount)
    final_amount = total_amount - discount
    # اقلام سفارش
    print("- Ordered Items: ")
    for order in orders: 
        item_total = order["price"] * order["quantity"]
        print(f"- {order['name'].capitalize()}(qty: { order['quantity']}) ---> {item_total:,} Toman")
    print("-" * 45)
    # مبلغ نهایی
    print(f"Total Amount : {total_amount:,} Toman")
    # مقدار تخفیف
    print(f"Discount : {discount:,}Toman")
    #مبلغ نهایی قابل پرداخت
    print(f"Final Payable: {final_amount:,}Toman")
    print("==================================")                  