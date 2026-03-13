import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import urllib.request

def analyze_image(image_path):

    img = Image.open(image_path)

    transform = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor()
    ])

    img_tensor = transform(img).unsqueeze(0)

    model = models.efficientnet_b0(pretrained=True)
    model.eval()

    labels_url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
    labels_path = "imagenet_classes.txt"

    urllib.request.urlretrieve(labels_url, labels_path)

    with open(labels_path) as f:
        labels = [line.strip() for line in f.readlines()]

    with torch.no_grad():
        output = model(img_tensor)

    probabilities = torch.nn.functional.softmax(output[0], dim=0)

    confidence, predicted = torch.max(probabilities, 0)

    detected_food = labels[predicted.item()]

    
    print("Confidence:", round(confidence.item()*100,2), "%")
    return detected_food