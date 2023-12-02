import numpy as np
import matplotlib.pyplot as plt

# Define the centroid coordinates
centroid_x = 0.5
centroid_y = 0.5

# Define the range of x and y values
x_values = np.linspace(0, 1, 100)
y_values = np.linspace(0, 1, 100)

# Create a mesh grid for x and y
x, y = np.meshgrid(x_values, y_values)

# Calculate the membership values using a Gaussian membership function with gamma
sigma = 0.2  # Adjust this parameter to control the spread of the cluster
gamma = 2.0  # Adjust this parameter to control the shape of the Gaussian function
membership_values = np.exp(-((x - centroid_x)**2 + (y - centroid_y)**2) / (2 * sigma**2)) ** gamma

# Create a contour plot to visualize the fuzzy set pattern cluster
plt.contourf(x, y, membership_values, cmap='Blues')
plt.colorbar(label='Membership Value')
plt.xlabel('X')
plt.ylabel('Y')
plt.title(f'Fuzzy Set Pattern Cluster with Centroid at ({centroid_x}, {centroid_y}), Sigma={sigma}, Gamma={gamma}')
plt.grid(True)
plt.show()
