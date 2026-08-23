import matplotlib.pyplot as plt

# Subjects and marks
subjects = ["Urdu", "English", "Math", "Physics", "Computer", "Pak Studies"]
marks = []

# Input marks
for sub in subjects:
    a = int(input(f"Enter marks in {sub} out of 100: "))
    marks.append(a)

# Create line chart
plt.plot(subjects, marks, marker="o", linestyle="-", color="black", linewidth=2)

# Add labels and title
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Marks Trend Line Chart")

# Show grid for clarity
plt.grid(True)

# Display chart
plt.show()
