import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and axis
fig, ax = plt.subplots()

x = np.linspace(0, 2*np.pi, 200)
line, = ax.plot(x, np.sin(x), color="blue")

# Update function for animation
def update(frame):
    line.set_ydata(np.sin(x + frame/10.0))  # shift sine wave
    line.set_color(plt.cm.viridis(frame % 200 / 200))  # change color smoothly
    return line,

# Animate
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.title("Wonderful Animated Sine Wave")
plt.show()
