import torch
from torchvision import models, transforms
from PIL import Image

#########################
# DOCUMENT RECOGNITION
#########################

# Load pre-trained model
model = models.resnet50(pretrained=True)
num_ftrs = model.fc.in_features
model.fc = torch.nn.Linear(num_ftrs, NUM_CLASSES)  # NUM_CLASSES includes driver's license

model.load_state_dict(torch.load('model.pth'))
model.eval()

# Preprocess image
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])

image = Image.open('license.jpg')
input_tensor = preprocess(image)
input_batch = input_tensor.unsqueeze(0)

# Predict
with torch.no_grad():
    outputs = model(input_batch)
    _, predicted = torch.max(outputs, 1)