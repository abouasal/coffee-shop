#Main.py
from Menu import show_menu
from Order import add_order, show_orders
from Billing import calculate_total, print_invoce
def main():
    while True: 
        print("\n ========== Coffee Shop ==========")
        print("1.Show Menu")
        print("2.Add Orders")#ثبت سفارش
        print("3.Show Orders")#نمایش سفارش ها
        print("4.Calculate Total")#محاسبه مبلغ کل
        print("5.Print Invoice")#چاپ فاکتور
        print("6.Exit") 
        print("====================================")
        choice = input("Enter your choice (1-6): ").strip()
        if choice == "1":
            show_menu()
        elif choice == "2":
            add_order()  
        elif choice == "3":
            show_orders() 
            input("\nPress Enter to continue...")  
        elif choice == "4":
            total = calculate_total()
            #مبلغ کل سفارش تا این لحظه
            print(f"\n Total amount so far :{total:,} Toman")    
        elif choice == "5":
            print_invoce() 
        elif choice == "6":
            # از حضور شما سپاسگزاریم
            print("\n thanks you for visiting . have a nice dry") 
            break
        else:
            #گزینه نامعتبر است عددی بین 1 تا 6 انتخاب کنید 
            print("Invalid choice! please enter a number between 1 and 6.")
if __name__ == "__main__":
    main()
         
    
