import shopping

prices=[]

#input 5 shopping items
for i in range(2):
    item=input(f"Enter item {i+1}: ")
    price= float(input(f"Enter price of {item}:"))
    
    shopping.add_item(item)
    prices.append(price)

#display all items
shopping.show_item()


#display total bill
print("Total bill:", shopping.total_price(prices))