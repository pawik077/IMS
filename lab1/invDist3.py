import matplotlib.pyplot as plt
import numpy as np

x = np.around(np.linspace(0, 1, 1000), decimals=3)

f = lambda x: np.exp(-x)
F = lambda x: 1 - np.exp(-x)
invF = lambda x: -np.log(1 - x)

plt.figure(1), plt.xlabel('x'), plt.ylim(top=8), plt.plot(x, f(x), label='$f(x)$'), plt.plot(x, F(x), label='$F(x)$'), plt.plot(x, invF(x), label='$F^{-1}(x)$')
plt.grid(), plt.legend()
plt.savefig('c_plt.eps')
plt.figure(2), plt.hist(invF(x), range=(0, 8), bins=100)
plt.savefig('c_hist.eps')

plt.show()
pass