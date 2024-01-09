import torch

mat = torch.tensor([[2, 3, 5],
                   [7, 9, 1]])

# reshaping
print(mat.reshape(3, 2))
print(mat.resize_(1, 6))
print(mat.shape)

# viewing
print(mat.view(6, 1))

# stacking
c1 = torch.tensor(9)
c2 = torch.tensor(8)
print(torch.stack([c1, c2]))

# squeezing
print(mat.squeeze().shape)

# unsqueezing
mat2 = mat.unsqueeze(1)
print(mat.shape)
print(mat2.shape)
