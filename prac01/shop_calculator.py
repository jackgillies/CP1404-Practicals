user_items = int(input("how many items?: "))
while user_items <= 0:
    print("Invalid number of items!")
user_items = int(input("how many items?: "))
total_price = 0
for i in range(user_items):
    total_price += float(input("price of item?: "))
if total_price >= 100:
    total_price -= total_price * 0.1
print("Total price for {} items is ${}".format(user_items, total_price))
