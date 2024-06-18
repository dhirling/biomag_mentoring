from comet_ml import Experiment
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader
from tqdm import tqdm

experiment = Experiment(
    api_key="cfPvvHqzmKpiAK5gljgCjdJCQ",
    project_name="resnet_imagenet",
)


experiment.set_name("test1")
# Data transformation and augmentation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Load the ImageNet dataset
train_dataset = datasets.CIFAR100(root='./datasets', train=False,download=False, transform=transform)
val_dataset = datasets.CIFAR100(root='./datasets', train=False,download=False, transform=transform)

train_loader = DataLoader(train_dataset, batch_size=4, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=4, shuffle=False)

# Define the ResNet18 model
model = models.resnet18(weights="IMAGENET1K_V1")
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 100)
# Move the model to GPU if available
device = torch.device(f"cuda:0}" if torch.cuda.is_available() else "cpu")
print(device)
model = model.to(device)

# Loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)


# Training function
def train_model(model, dataloaders, criterion, optimizer, num_epochs=10):
    for epoch in range(num_epochs):
        print(f'Epoch {epoch+1}/{num_epochs}')
        print('-' * 10)

        # Each epoch has a training and validation phase
        for phase in ['train', 'val']:
            if phase == 'train':
                model.train()  # Set model to training mode
                dataloader = dataloaders['train']
            else:
                model.eval()  # Set model to evaluate mode
                dataloader = dataloaders['val']

            running_loss = 0.0
            running_corrects = 0

            # Iterate over data
            for inputs, labels in tqdm(dataloader):
                inputs = inputs.to(device)
                labels = labels.to(device)

                # Zero the parameter gradients
                optimizer.zero_grad()

                # Forward
                with torch.set_grad_enabled(phase == 'train'):
                    outputs = model(inputs)
                    _, preds = torch.max(outputs, 1)
                    loss = criterion(outputs, labels)

                    # Backward + optimize only if in training phase
                    if phase == 'train':
                        loss.backward()
                        optimizer.step()

                # Statistics
                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels.data)

            epoch_loss = running_loss / len(dataloader.dataset)
            epoch_acc = running_corrects.double() / len(dataloader.dataset)

            print(f'{phase} Loss: {epoch_loss:.4f} Acc: {epoch_acc:.4f}')

            # Log metrics to Comet.ml
            if phase == 'train':
                experiment.log_metric("train_loss", epoch_loss, epoch=epoch+1)
                experiment.log_metric("train_accuracy", epoch_acc, epoch=epoch+1)
            else:
                experiment.log_metric("val_loss", epoch_loss, epoch=epoch+1)
                experiment.log_metric("val_accuracy", epoch_acc, epoch=epoch+1)

    return model

# Dataloaders dictionary
dataloaders = {
    'train': train_loader,
    'val': val_loader
}

# Train the model
model = train_model(model, dataloaders, criterion, optimizer, num_epochs=10)

# Save the trained model
torch.save(model.state_dict(), 'imagenet_resnet18.pth')