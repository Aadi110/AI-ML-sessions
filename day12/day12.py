import numpy as np

store=np.array([
    [120,135,150,145,160,170,180], #rice
    [80,90,85,95,100,110,105], #oil
    [60,55,70,65,75,80,85], #sugar
    [200,210,205,220,230,240,245], #milk
    [150,145,160,170,180,190,200]  #bread
    
])


print(np.shape(store))

total_product = np.sum(store, axis=0)
print(total_product)

total_product_by_day = np.sum(store, axis=1)
print(total_product_by_day)

print(np.max(total_product))
print(np.max(total_product_by_day))

print(np.average(total_product))

print(np.average(store, axis=0))


# print(total_product[total_product>180])

# new_product= total_product*1.10
# print(new_product)

# # new_average= np.mean(store, axis=1)
# # print(new_average>150)

# print(np.where(total_product<150))


bonus= np.where(store>200, 20,0)
print(bonus)
