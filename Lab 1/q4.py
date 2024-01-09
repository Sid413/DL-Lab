import torch
import numpy as np

arr = np.array([1, 2, 3, 4])

tens = torch.from_numpy(arr)
print(tens)
