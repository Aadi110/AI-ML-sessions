#matplotlib

import matplotlib.pyplot as plt

# x=[1,2,3,4]
# y=[1,4,9,16]

# plt.plot(x,y)
# plt.show()

''' Line Graph representation  '''
# months=['jan','feb','mar','apr']
# sales=[200,250,400,350]

# plt.plot(sales,months, marker='o', color='g', linestyle='--')
# plt.title('Monthly sales')
# plt.xlabel('Sales')
# plt.ylabel('Months')
# plt.grid()
# plt.show()


products=['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch']
sales=[150, 300, 200, 100, 80]
plt.bar(products, sales, color='skyblue', edgecolor='black', width=0.6)
plt.title('Product Sales')
plt.xlabel('Products')
plt.ylabel('Number of Sales')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()



