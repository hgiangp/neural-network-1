import torch

jab = torch.load('jacobian.pt')
print(jab.size())
print(jab.max())
print(jab.min())

hess = torch.load('hessian.pt')
print(hess.size())
print(hess.max())
print(hess.min())
