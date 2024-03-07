import numpy as np
import matplotlib.pyplot as plt

def square(t):
    if t % 1 < 0.25 or t % 1 > 0.75:
        s = 1
    elif t % 1 == 0.25 or t % 1 == 0.75:
        s = 0.5
    else:
        s = 0
    return s

# Generate values for t including negative values
t_values = np.linspace(-1, 1, 2000)

# Calculate corresponding values of s
s_values = [square(t) for t in t_values]

# Plot
plt.plot(t_values, s_values)
plt.xlabel('t')
plt.ylabel('s')
plt.title('Signal s vs t')
plt.grid(True)
plt.show()
