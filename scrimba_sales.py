sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales_w2.append(int(input('Last day sold on wk 2: ')))
sales = sales_w1 + sales_w2

print(f'Best Day profit : {max(sales) * 1.5}')
print(f'Worst Day profit : {min(sales) * 1.5}')
print(f'Total sales {(min(sales) + max(sales)) * 1.5}')

