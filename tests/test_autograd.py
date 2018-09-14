import torch

x = torch.tensor([[0.1, 0.3], [-0.4, 0.2]])
y = torch.tensor([[0.7, -0.5], [0.1, 0.1]])
z = torch.tensor([[0.2, -0.4], [-0.5, -0.2]])

x.requires_grad = True

r = ((x + y) * y).sin() + (z - x).tanh()
r.backward(torch.ones_like(r))
print(x.grad)