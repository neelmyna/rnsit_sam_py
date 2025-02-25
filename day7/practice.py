import numpy as np
import matplotlib.pyplot as plt

# Generate random data for 4 categories
data = [np.random.randn(100) for _ in range(4)]

# Create box plot
plt.boxplot(data, patch_artist=True)
plt.xlabel("Category")
plt.ylabel("Values")
plt.title("Box Plot")
plt.show()