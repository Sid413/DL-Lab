import torch

print(torch.cuda.is_available())
mat1 = torch.rand(size=(2, 3))
mat2 = torch.rand(size=(2, 3))