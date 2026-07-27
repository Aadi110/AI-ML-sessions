items=[]
def add_item(item):
    items.append(item)
    
def show_item():
    print("\nItem in cart:")
    for i, item in enumerate(items, start=1):
        print(f"{i}, {item}")

def total_price(prices):
    return sum(prices)
    
