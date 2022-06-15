import matplotlib.pyplot as plt
import numpy as np

sigma = 4
mu = 0
L = 20

T = []
est1 = []
est1_2 = []
est2 = []
est3 = []
err1 = []
err2 = []
err3 = []

for n in range(0, 200):
	T.append(np.random.randn(L, n) * sigma + mu)
	est1.append(np.sum(T[n], -1) / n)
	est1_2.append(np.reshape(est1[n], (L, 1)))
	est2.append(np.sum(np.square(T[n] - est1_2[n]), -1) / n)
	est3.append(np.sum(np.square(T[n] - est1_2[n]), -1) / (n - 1))
	err1.append(np.sum(np.square(est1[n] - mu)) / L)
	err2.append(np.sum(np.square(est2[n] - sigma**2)) / L)
	err3.append(np.sum(np.square(est3[n] - sigma**2)) / L)

plt.figure(1), plt.grid(), plt.xlabel('$n$'), plt.ylabel('$Err\{\hat{\mu}_N;\mu\}$')
plt.plot(err1), plt.savefig(f'err1-L={L}.eps')
plt.figure(2), plt.grid(), plt.xlabel('$n$'), plt.ylabel('$Err\{\hat{s}^2_N;s^2\}$')
plt.plot(err2), plt.savefig(f'err2-L={L}.eps')
plt.figure(3), plt.grid(), plt.xlabel('$n$'), plt.ylabel('$Err\{\hat{S}^2_N;s^2\}$')
plt.plot(err3), plt.savefig(f'err3-L={L}.eps')

plt.show()
#print(err1, err2, err3)