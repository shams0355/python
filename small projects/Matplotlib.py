import matplotlib.pyplot as plt

# Sample data
categories = ["Apples", "Bananas", "Cherries", "Dates"]
values = [10, 15, 7, 12]

# Create bar chart
plt.bar(categories, values, color="skyblue")

# Add labels and title
plt.xlabel("Fruit")
plt.ylabel("Quantity")
plt.title("Fruit Inventory")

# Show the chart
plt.show()
