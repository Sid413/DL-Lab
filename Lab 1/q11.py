import torch

torch.manual_seed(7)
mat1 = torch.rand(size=(1, 1, 1, 10))
print(mat1)
print(mat1.shape)

mat2 = mat1.squeeze()
print(mat2)
print(mat2.shape)

