# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft,fftshift,ifft 
from scipy import signal

# Square pulse
def square(t):
    if t % 1 < 0.25 or t % 1 > 0.75:
        s=1
    elif t % 1 == 0.25 or t % 1 == 0.75:
        s = 0.5
    else:
        s=0
    return s

# Fourier series coefficients
def a(k):
    # Your code goes here
    # For k = 0 instance
    if k == 0:
        # a_k = Average value of the function
        a_k = 0.5
    else:
        # for k != 0 use coefficient formula
        a_k = 1 * np.sin(k * np.pi/2) / (k * np.pi)
    return a_k

def fs_approx(t, N):
    # Your code goes here
    x_t = 0.0
    
    # Parameters
    T = 1.0
    w0 = 2 * np.pi / T
    
    # Loop through -N to N and add individual complex exponentials
    for i in range(-N, N+1):
        x_t += (a(i)*np.e**(1j*i*w0*t)).real
    return x_t

# Fourier series approximation of the square wave
x = []
y = []
N = 5 # CHANGE HERE

# Creating a timestamp array
time = np.linspace(-2.5, 2.5,1000)

# Filling x and y arrays
for t in time:
    # Fill x array
    x.append(square(t))
    # Fill y array
    y.append(fs_approx(t,N))

    # Plotting
fig,ax=plt.subplots(figsize=(12,4))

# Editing plot parameters
ax.plot(time,x)
ax.plot(time,y)
ax.grid()

plt.show()