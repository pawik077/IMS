import matplotlib.pyplot as plt
import numpy as np

x = np.around(np.linspace(-1, 1, 10000), decimals=3)

f = lambda x: (x + 1) * (x < 0) * (x > -1) + (-x + 1) * (x >= 0) * (x < 1)
F = lambda x: (x**2 / 2 + x + 0.5) * (x > -1) * (x < 0) + (0.5 + x - x**2 / 2) * (x >= 0) * (x < 1) + (x >= 1)
invF = lambda x: (np.sqrt(2 * x) - 1) * (x >= 0) * (x <= 0.5) + (1 - np.sqrt(2 - (x * 2))) * (x > 0.5) * (x <= 1) - (x < -1)

plt.figure(1), plt.xlabel('x'), plt.plot(x, f(x), label='$f(x)$'), plt.plot(x, F(x), label='$F(x)$'), plt.plot(x, invF(x), label='$F^{-1}(x)$')
plt.grid(), plt.legend()
plt.savefig('b_plt.eps')
plt.figure(2), plt.hist(invF(x), bins=20)
plt.grid()
plt.savefig('b_hist.eps')

plt.show()
pass