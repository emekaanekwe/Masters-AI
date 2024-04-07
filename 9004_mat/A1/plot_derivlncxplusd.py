import numpy as np
import matplotlib.pyplot as plt

# Define the function for the derivative
def derivative_ln(x, c, d):
    return c / (c*x + d)

# Define constants c and d
c = 1
d = 1

# Generate x values
x_values = np.linspace(-10, 10, 400)

# Calculate corresponding f'(x) values
derivative_values = derivative_ln(x_values, c, d)

# Plot the graph
plt.plot(x_values, derivative_values, label='f\'(x)')
plt.xlabel('x')
plt.ylabel('f\'(x)')
plt.title('Plot of the derivative of ln(cx + d)')
plt.grid(True)
plt.legend()
plt.show()
