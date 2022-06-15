import matplotlib.pyplot as plt
import numpy as np

x = np.around(np.linspace(0, 1, 1000), decimals=3)

f = lambda x: 2 * x * (x >= 0) * (x <= 1)
F = lambda x: (x**2) * (x >= 0) * (x <= 1) + (x > 1)
invF = lambda x: np.sqrt(x * (x>=0))

plt.figure(1), plt.xlabel('x'), plt.plot(x, f(x), label='$f(x)$'), plt.plot(x, F(x), label='$F(x)$'), plt.plot(x, invF(x), label='$F^{-1}(x)$')
plt.grid(which='both'), plt.legend()
plt.savefig('a_plt.eps')
plt.figure(2), plt.hist(invF(x), bins=20)
plt.grid()
plt.savefig('a_hist.eps')

plt.show()
pass