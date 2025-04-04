import torch # pytorch basic package
from torch import nn # neural net
from torch.utils.data import DataLoader, Dataset # to work with data
from torchvision import datasets # built-in data
from torchvision.transforms import ToTensor # to convert nparrays/images into pytorch tensors
import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np
from nn_utils import train, test

# Download training data from open datasets.
training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor(),
)

# Download test data from open datasets.
test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor(),
)

labels_map = {
    0: "T-Shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot",
}

batch_size = 8

# Create data loaders.
train_dataloader = DataLoader(training_data, batch_size=batch_size)
test_dataloader = DataLoader(test_data, batch_size=batch_size)

device = "cuda" if torch.cuda.is_available() else "cpu"


# Define the CNN model
class CNNModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.conv_relu_stack = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, stride=1, padding='same'),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),

            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding='same'),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )

        self.linear_relu_stack = nn.Sequential(
            nn.Linear(in_features=64 * 7 * 7, out_features=128),
            nn.ReLU(),
            nn.Linear(128, 10)
        )

        self.flatten = nn.Flatten()

    def forward(self, x):
        x = self.conv_relu_stack(x)
        x = self.flatten(x)

        logits = self.linear_relu_stack(x)
        return logits

# We create our model by instantiating the NeuralNetwork class and immediately move it to the GPU
model = CNNModel().to(device)
print(model)

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

epochs = 5
train_losses = []
test_losses = []
for t in tqdm(range(epochs)):
    train_loss = train(train_dataloader, model, loss_fn, optimizer, 10000, device)
    test_loss = test(t, test_dataloader, model, loss_fn, device)

    train_losses.append(train_loss)
    test_losses.append(test_loss)

print("Done!")