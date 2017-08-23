sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales >= 1000:
        user_bonus = (sales * 0.15)
    else:
        user_bonus = (sales * 0.1)
    print("You're bonus is: {}".format(user_bonus))
    sales = float(input("Enter sales: $"))