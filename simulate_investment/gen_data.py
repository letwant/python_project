import random
import matplotlib.pyplot as plt

init_val = 10
init_money = 10000

val_list = [init_val]
val = (1+random.uniform(-0.05, 0.05))*init_val
val_list.append(val)
for i in range(60):
    val = (1+random.uniform(-0.05, 0.05)) * val
    val_list.append(val)
plt.plot(val_list)
plt.show()
print(val_list)
