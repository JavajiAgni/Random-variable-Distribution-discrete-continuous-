#Discrete Random Variable (e.g., Die Roll / PMF)

import numpy as np
from scipy import stats

# Define possible outcomes (faces of a die) and probabilities
x = np.arange(1, 7)
p = np.full(6, 1 / 6)  # Equal probability for each face

# Calculate Expected Value and Variance manually
mean = np.sum(x * p)
var = np.sum((x - mean) ** 2 * p)

print(f"Mean: {mean}, Variance: {var}")

# Using SciPy's built-in discrete distribution
die = stats.randint(1, 7)  # Generates integers 1 to 6
print("P(X <= 3):", die.cdf(3))


#Continuous Random Variable (e.g., Normal Distribution / PDF)

import numpy as np
from scipy import stats

# Define a normal distribution: Mean = 170, Std Dev = 5
mu, sigma = 170, 5
dist = stats.norm(loc=mu, scale=sigma)

# Probability density at a specific point z = 175
pdf_value = dist.pdf(175)

# Cumulative probability P(Z <= 175)
cdf_value = dist.cdf(175)

# Generate 5,000 random samples from this distribution
samples = dist.rvs(size=5000, random_state=42)

print(f"PDF at 175: {pdf_value:.4f}")
print(f"CDF at 175: {cdf_value:.4f}")
print(f"Sample Mean: {samples.mean():.2f}, Sample Std: {samples.std():.2f}")
