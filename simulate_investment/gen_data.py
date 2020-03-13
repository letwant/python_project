import random
import matplotlib.pyplot as plt

init_val = 10
init_money = 100000
investment_money = 0
portion = 0

val_list = [init_val]
val = (1+random.uniform(-0.05, 0.05))*init_val
val_list.append(val)
for i in range(500):
    val = (1+random.uniform(-0.05, 0.05)) * val
    val_list.append(val)
plt.plot(val_list)
plt.show()
print(val_list)

for index, value in enumerate(val_list):
    if investment_money == init_money:
        break
    if index % 3 == 0:
        portion += 1000/value
        investment_money += 1000

tmp_val = 0
sec_portion = 0
sec_investment_money = 0
for index, value in enumerate(val_list):
    if sec_investment_money == init_money:
        break
    if tmp_val - value > 0.02:
        sec_portion += 1000 / value
        sec_investment_money += 1000
    tmp_val = value

tmp_val1 = 0
third_portion = 0
third_investment_money = 0
for index, value in enumerate(val_list):
    if third_investment_money == init_money:
        break
    if index % 3 == 0:
        third_portion += 1000/value
        third_investment_money += 1000
    if index != 0 and val - tmp_val1 > 0.03:
        third_portion += 500 / value
        third_investment_money += 500
    tmp_val1 = val
print(investment_money)
print(sec_investment_money)
print(third_investment_money)
print(100000/10)
print(portion)
print(sec_portion)
print(third_portion)


