# Fly Detector

Small YOLOv8 example detecting flying objects. Trained on few images, it can analyze videos in real time. For demo and experimentation purposes.

## Technologies

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![YOLO](https://img.shields.io/badge/YOLO-red?style=for-the-badge&logo=yolo&logoColor=white)](https://github.com/AlexeyAB/darknet)
[![MakeSense.ai](https://img.shields.io/badge/MakeSense.ai-FF6F61?style=for-the-badge&logo=makesense&logoColor=white)](https://www.makesense.ai/)

## Steps to the development

- Create the dataset with the images
    - Download the images
    - Create classes for the images
    - Annotate the images
    -  Split the images into train and validation
- Setup the data file
- Train a custom model from a pretrained one (YOLO)
- Test the new model

## Commands to train and predict with the model

**Train the model with the example images**

```bash
yolo detect train model=yolov8n.pt data=dataset/data.yaml epochs=50 imgsz=640 augment=true
```

**Predict videos with the trained model**

```bash
yolo detect predict model=runs/detect/train/weights/best.pt source=videos 
```




