import matplotlib.pyplot as plt

plt.style.use('seaborn')
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

#set chat title and lable axes
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Set size of tick lables
ax.tick_params(axis='both', labelsize=14)

plt.show()