import numpy as np
print(np.zeros((4,4),dtype='int'))
print(np.full((10,10),255,dtype='float'))
print(np.arange(10,100))
print(np.arange(10, 100).reshape(9, 10))
print(np.eye(6,dtype='int'))
np.random.seed(10)
print(np.random.rand(30))
np.random.seed(20)
print(np.random.randn(10,4))
np.random.seed(30)
print(np.random.rand(10,4))