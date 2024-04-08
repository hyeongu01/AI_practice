import numpy as np

def step_function(x):
  y = np.array(x > 0)
  return y.astype(np.int8)
  
a = np.array([3, 5, -1])
print(step_function(1))