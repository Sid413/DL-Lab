import torch

mat1 = torch.rand(size=(1, 1, 1, 10))
print(mat1)
print(mat1.shape)

mat2 = mat1.squeeze()
print(mat2)
print(mat2.shape)

