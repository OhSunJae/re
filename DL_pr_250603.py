
import numpy as np

x = np.array([[0,0], [0,1], [1,0], [1,1]])
print(x)

#됐다. 또 해결했다. 오졌다.

y = np.array([0,0,0,1])

w = np.array([0.5, 0.5])
b = -0.7

def step(x): return 1 if x > 0 else 0
for x in x :
    z = np.sum(x * w) + b
    print(f"입력: {x}, 출력: {step(z)}")