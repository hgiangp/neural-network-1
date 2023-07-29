import os 
import torch.nn as nn
import torch
import torchvision.datasets as datasets 
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import time

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(784, 10)

    def forward(self, x):
        x = self.linear(x)
        return x

# Check available device 
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device)

# Load model 
current_dir = os.path.dirname(os.path.abspath(''))
model_path = os.path.join(current_dir, 'final', 'mnist_net.pth')
net = Net()
net.to(device)

net.load_state_dict(torch.load(model_path))
loss_fn = nn.CrossEntropyLoss()

# Load data 
data_dir = os.path.join(current_dir, 'final', 'data')
print(data_dir)
if not os.path.exists(data_dir): 
    os.makedirs(data_dir)

transform = transforms.ToTensor()

# Get MNIST data, normalize, divide by level 
batch_size = 32 
mnist_train = datasets.MNIST(root=data_dir, train=True, download=True, transform=transform)
trainloader = DataLoader(mnist_train, batch_size=batch_size, shuffle=True, pin_memory=True)

def compute_loss(data_loader): 
    loss = torch.zeros(1, device=device)
    num_batches = len(data_loader)
    for batch, data in enumerate(trainloader):
        inputs, labels = data
        inputs = inputs.to(device=device)
        labels = labels.to(device=device)
        inputs = inputs.view(-1, 784)
        loss += loss_fn(net(inputs), labels)
        print(f"batch = {batch} loss = {loss.item()}")

    loss = loss/num_batches
    return loss 

current_dir = os.path.dirname(os.path.abspath(''))
current_dir = os.path.join(current_dir, 'final')

def compute_hessian():     
    num_param = sum(p.numel() for p in net.parameters())
    # Allocate Hessian size
    H = torch.zeros((num_param, num_param))
    loss = compute_loss(trainloader)

    # Calculate Jacobian w.r.t. model parameters
    J = torch.autograd.grad(loss, list(net.parameters()), create_graph=True)
    J = torch.cat([e.flatten() for e in J]) # flatten

    torch.save(J, os.path.join(current_dir, 'jacobian.pt'))
    
    # Calculate Hessian w.r.t. model parameters
    start = time.time()

    for i in range(num_param):
        result = torch.autograd.grad(J[i], list(net.parameters()), retain_graph=True)
        H[i] = torch.cat([r.flatten() for r in result]) # flatten
    
    torch.save(H, os.path.join(current_dir, 'hessian.pt'))

    print(time.time() - start)

compute_hessian()