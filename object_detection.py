import torch
from PIL import Image
from pathlib import Path

def detect_objects(image_path):
    """Detect objects in the given image and return a list of detected objects."""
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Load YOLOv5 small model
    image = Image.open(image_path)
    results = model(image)  # Perform detection
    detected_objects = results.names  # Get names of detected classes

    # Only return the objects detected
    objects = [detected_objects[i] for i in range(len(results.pred[0]))]
    return objects
