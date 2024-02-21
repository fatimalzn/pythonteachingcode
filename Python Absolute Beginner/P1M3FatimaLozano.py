def cheese_order(max=100,min=1,price=2,order_amount=any):
    order_amount=int(input("Fatima Lozano, enter cheese order weight: "))
    if order_amount > max:
        print(order_amount, "is more than we have available")
    elif order_amount < min:
        print(order_amount, "is below the minimum order amount")
    else:
        print(order_amount, "costs", "$"+ str(order_amount * price))

cheese_order()