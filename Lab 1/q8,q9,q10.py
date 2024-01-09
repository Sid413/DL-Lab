import torch

# q8
mat1 = torch.rand(size=(2, 3))
mat2 = torch.rand(size=(2, 3))

mat2 = mat2.permute(1, 0)
ans = torch.matmul(mat1, mat2)
print(ans)

# q9
print(torch.min(ans))
print(torch.max(ans))

# q10
print(torch.argmin(ans))
print(torch.argmax(ans))