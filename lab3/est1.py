import numpy as np

count = 10000

sigma = 4
mu = 0

T = np.random.randn(count) * sigma + mu

est1 = np.sum(T) / count
est2 = np.sum(np.square(T - est1)) / count
est3 = np.sum(np.square(T - est1)) / (count - 1)

print(f'{count} & {est1} & {est2} & {est3}')