import torch

x = torch.Tensor(2, 2)
print(x)
list = [[1, 2, 3], [4, 5, 6]]
print(list)
x2 = torch.Tensor(list)
print(x2)
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(x2.size())
print(torch.rand(2, 2))
a = torch.eye(3, 3)
print(a)
print(torch.empty(4, 1))
print(torch.linspace(0, 100, 11))
x = torch.tensor([[2., 2.], [1., 1.]])
y = torch.tensor([[3., 2.], [1., 2.]])
print(x)
print(y)
print(x + y)
print(torch.add(x, y))
print(x * y)
print(torch.mul(x, y))
print(torch.mm(x, y))
print(torch.sum(x))
print(torch.std(x))
print(torch.mean(x))
