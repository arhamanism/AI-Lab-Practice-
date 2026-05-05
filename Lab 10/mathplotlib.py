import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [20, 12, 3, 4, 32]

plt.bar(categories, values, color="Green")
plt.xlabel("Categories")
plt.ylabel("values")
plt.title("Bar Graph")
plt.show()