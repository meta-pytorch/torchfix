import torch


a = torch.randn(5)
b = 1 / torch.sqrt(a)
b = 1.0 / torch.sqrt(a)
b = a / torch.sqrt(a)
# False negative
b = 1 / a.sqrt()
b = 1.0 / a.sqrt()
