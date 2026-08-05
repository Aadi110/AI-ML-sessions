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




# products=['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch']
# sales=[150, 300, 200, 100, 80]
# plt.bar(products, sales, color='skyblue', edgecolor='black', width=0.6)

# # plt.barh(products, sales)               #horizontal print 

# for i, value in enumerate(sales):
#     plt.text(i, value, str(value), ha='center', va='bottom')

# plt.title('Product Sales', fontsize=20)
# plt.xlabel('Products', fontsize=15)
# plt.ylabel('Number of Sales', fontsize=15)
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.show()


#piechart= to represent the data in % form

# expenses= [2200, 2350, 2600, 2130, 2190]
# categories= ['Rent', 'Gas', 'Food', 'clothes', 'misc']
# plt.pie(expenses, labels=categories, autopct='%1.1f%%')
# plt.title('Monthly Expenses')
# plt.show()



#scatterchart

# hours=[1,2,3,4,5]
# marks=[40,45,50,60,70]
# plt.scatter(hours, marks)
# plt.title("hours vs marks")
# plt.xlabel("Hours Studied")
# plt.ylabel("Marks Obtained")
# plt.show()



#histogram

# marks=[88,92,79,85,90,95,87,91,84,93,78,82,94,86,80,83,81,77,76]
# plt.hist(marks, bins=[0,20,40,60,80,100], edgecolor='black')
# plt.title("Histogram")
# plt.xlabel("Marks")
# plt.ylabel("Frequency")
# plt.show()


months=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
sales_2024=[1500,1800,2000,2200,2500,2700,3000,3200,3500,3700,4000,4200]
sales_2025=[1600,1900,2100,2300,2600,2800,3100,3300,3600,3800,4100,4300]
products=['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch']

'''
Task:
    1. Basic Line Chart
    2. Multi Line chart
    3. Vertical Bar Chart
    4. Horizontal Bar Chart
    5. Histogram
'''
#1
# plt.plot(months, sales_2024, marker="o", color='red', linestyle='--' )
# plt.title("Sales in 2024")
# plt.xlabel('months')
# plt.ylabel('sales')
# plt.grid()
# plt.show()

# plt.plot(months, sales_2025, marker="o", color='red', linestyle='--' )
# plt.title("Sales in 2025")
# plt.xlabel('months')
# plt.ylabel('sales')
# plt.grid()
# plt.show()

#2
# plt.plot(months, sales_2024, sales_2025, marker="o", color='red', linestyle='--' )
# plt.title("Sales in 2024& 2025")
# plt.xlabel('months')
# plt.ylabel('sales')
# plt.grid()
# plt.show()

#3
# plt.bar(months, sales_2024, color='red')
# plt.title("Sales in 2024")
# plt.xlabel('months')
# plt.ylabel('sales')
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.show()


#4
# plt.barh(months, sales_2025, color='red')
# plt.title("Sales in 2025")
# plt.xlabel('months')
# plt.ylabel('sales')
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.show()

#5
plt.hist(months, sales_2025, color='red')
plt.title("Sales in 2025")
plt.xlabel('months')
plt.ylabel('sales')
plt.grid()
plt.legend()
plt.show()



# plt.plot(months, sales_2024, label='Sales 2024', marker='o')
# plt.plot(months, sales_2025, label='Sales 2025', marker='o')
# plt.title('Monthly Sales Comparison')
# plt.xlabel('Months')
# plt.ylabel('Sales')
# plt.legend()
# plt.show()#multiline graph
