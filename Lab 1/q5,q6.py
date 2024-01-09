import torch

mat1 = torch.rand(size=(7, 7))
print(mat1)

mat2 = torch.rand(size=(1, 7))

mat2 = mat2.permute(1, 0)

print(torch.matmul(mat1, mat2))