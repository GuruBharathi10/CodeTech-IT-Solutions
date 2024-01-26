import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values_bar = [25, 30, 15, 20]
values_pie = [20, 35, 25, 20]
values_line = np.array([10, 20, 15, 25])

# Bar chart
plt.figure(figsize=(8, 4))
plt.bar(categories, values_bar, color='skyblue')
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# Pie chart
plt.figure(figsize=(8, 8))
plt.pie(values_pie, labels=categories, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightgreen', 'lightskyblue', 'gold'])
plt.title('Pie Chart')
plt.show()

# Line graph
plt.figure(figsize=(8, 4))
plt.plot(categories, values_line, marker='o', color='orange', linestyle='-', linewidth=2)
plt.title('Line Graph')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid(True)
plt.show()
