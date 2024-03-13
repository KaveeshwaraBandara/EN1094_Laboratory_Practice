import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

# Define the functions h(t) and x(t)
h = lambda t: (t > 0)*1.0
x = lambda t: (t > 0) * np.exp(-2*t) # a = −2

# Sampling parameters
Fs = 50 # Sampling frequency for the plotting
T = 5  # Time range
t = np.arange(-T, T, 1/Fs) # Time samples

# Plotting the input functions
plt.figure(figsize=(8,3))
plt.plot(t, h(t), label='$h(t)$')
plt.plot(t, x(t), label='$x(t)$')
plt.xlabel(r'$t$')
plt.legend()

# Plotting individual components of convolution
plt.figure(figsize=(8,3))
plt.plot(t, x(t), label=r'$x(\tau)$')
plt.plot(t, h(t_), label=r'$h(t − \tau)$')
plt.plot(t, x(t) * h(t_), label=r'$x(\tau)h(t -\tau)$')

# Computing the convolution using integration
y = np.zeros(len(t))
for n, t_ in enumerate(t):
    product = lambda tau: x(tau) * h(t_ - tau)
    y[n] = integrate.simps(product(t), t) # Actual convolution at time t
    
plt.plot(t, y, label=r'$x(t)\ast h(t)$') # Plotting the output y
plt.xlabel(r'$t$')
plt.legend()

plt.show()
