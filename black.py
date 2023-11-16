import numpy as np
import matplotlib.pyplot as plt

# Constants
h = 6.62607015e-34  # Planck's constant in Js
c = 3.0e8           # Speed of light in m/s
k = 1.380649e-23    # Boltzmann constant in J/K


# Function to calculate the black body spectrum
def black_body_spectrum(freq, T):
    a = 8.0*np.pi*h*freq**2/c**3
    b = h*freq/(k*T)
    return a / (np.exp(b)-1)


temp = 2.725
frequency = np.arange(1e9, 8e11, 1e9)
intensity = black_body_spectrum(frequency, temp)
plt.plot(frequency/(3e10), intensity/(1e-21))
# Add labels and legend
plt.xlabel('Frequency (Hz)')
plt.ylabel('Flux (W / m^2 / Hz / sr)')
plt.title('Black Body Spectrum')
plt.legend()
plt.grid(True)
plt.show()