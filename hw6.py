import numpy as np
import matplotlib.pyplot as plt


p_1 = np.random.poisson(lam=2, size=50000)
p_2 = np.random.poisson(lam=2, size=50000)
p_3 = np.random.poisson(lam=2, size=50000)
p_sum = p_1 + p_2 + p_3

p_sum_t = np.random.poisson(lam=6, size=50000)

fig, ax = plt.subplots(1, 1, figsize=(10, 5))
ax.hist(p_sum, bins=20, color='r', alpha=0.3, label='p_sum')
ax.hist(p_sum_t, bins=20, color='g', alpha=0.3, label='p_sum_t')
ax.legend()
plt.show()