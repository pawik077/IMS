import matplotlib.pyplot as plt
import numpy as np

x = np.around(np.linspace(-10, 10, 10000), decimals=3)
u = 0
b = 2

f = lambda x: np.exp(-np.abs(x - u) / b) / (2 * b)
F = lambda x: (np.exp((x - u) / b) / 2) * (x <= u) + (1 - np.exp(-(x - u) / b) / 2) * (x >= u)
invF = lambda x: (u + b * np.log(2 * x)) * (x <= 0.5) + (u - b * np.log(2 - 2 * x)) * (x >= 0.5)

plt.figure(1), plt.xlabel('x'), plt.ylim(top=2, bottom=-5), plt.plot(x, f(x), label='$f(x)$'), plt.plot(x, F(x), label='$F(x)$'), plt.plot(x, invF(x), label='$F^{-1}(x)$')
plt.grid(), plt.legend()
plt.savefig('d_plt.eps')
plt.figure(2), plt.hist(invF(x), range=(-4, 4), bins=100)
plt.grid()
plt.savefig('d_hist.eps')

plt.show()
pass