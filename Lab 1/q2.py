import torch

mat = torch.tensor([[2, 3, 5],
                   [7, 9, 1]])

print(mat.permute(1, 0))
