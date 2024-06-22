import time


def vending_machine():
    items = {
        1: {"name": "Soda", "price": 20.00},
        2: {"name": "Water Bottle", "price": 25.50},
        3: {"name": "Juice", "price": 105.25},
        4: {"name": "Chips", "price": 30.00},
        5: {"name": "Biscuits", "price": 15.20}
    }

    print("Welcome to the Vending Machine!".center(100,"-"))
    print("Here are the available items:")
    for key, value in items.items():
        print(f"{key}. {value['name']} - Rs. {value['price']:.2f}")


    while True:
        try:
            balance = float(input("Enter the amount of money you have: Rs. "))
            if balance < 0:
                raise ValueError("Amount cannot be negative")
            break
        except ValueError:
            print ("Invalid input")

    while True:
        try:
                choice = int(input("Enter the number of the item you want to purchase: "))

                if choice in items:
                    item = items[choice]
                    item_name = item["name"]
                    item_price = item["price"]

                    if balance >= item_price:
                        balance -= item_price
                        print(f"You have purchased {item_name}. Your remaining balance is Rs. {balance:.2f}")

                        another = input("Do you want to buy another item? (yes/no): ").strip().lower()
                        if another == 'yes':
                            continue
                        elif another == 'no':
                            break
                        else:
                            print ("Invalid Input")
                            break
                    else:
                        print(f"Insufficient funds to purchase {item_name}. Your balance: Rs. {balance:.2f}")

                        another = input("Do you want to select another item? (yes/no): ").strip().lower()
                        if another == 'yes':
                            continue
                        elif another == 'no':
                            break
                        else:
                            print("Invalid Input")
                            break
                else:
                    print("Invalid selection. Please enter a valid item number.")


        except:
            print ("Invalid Input")

    print("Thank you for using the Vending Machine!".center(100,"-"))
    time.sleep(2)


vending_machine()
