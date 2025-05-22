import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

np.random.seed(42)  # for reproducibility

N = 1000  # number of individuals
M = 10    # number of attempts per individual

# Generate skill levels for individuals
skills = np.random.uniform(0, 100, N)

# Luck variance settings
luck_variances = np.linspace(0.1, 100, 50)

correlations = []

for lv in luck_variances:
    # For each individual, simulate M attempts
    # success = skill + luck_noise, luck_noise ~ N(0, lv)
    luck_noise = np.random.normal(0, np.sqrt(lv), (N, M))
    successes = skills[:, None] + luck_noise
    
    # Average success over attempts
    avg_success = successes.mean(axis=1)
    
    # Calculate correlation
    corr, _ = pearsonr(skills, avg_success)
    correlations.append(corr)

plt.figure(figsize=(10,6))
plt.plot(luck_variances, correlations, marker='o')
plt.title('Correlation between Skill and Success vs Luck Variance')
plt.xlabel('Luck Variance (higher means more luck influence)')
plt.ylabel('Correlation (Skill vs Success)')
plt.grid(True)
plt.show()
