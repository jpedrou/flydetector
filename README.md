# Fly Detector

Small YOLOv8 example detecting flying objects. Trained on few images, it can analyze videos in real time. For demo and experimentation purposes.

<img src="runs/detect/train/train_batch1.jpg" width="1000" height="300"/>

## Technologies

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![YOLO](https://img.shields.io/badge/YOLO-red?style=for-the-badge&logo=yolo&logoColor=white)](https://github.com/AlexeyAB/darknet)
[![MakeSense.ai](https://img.shields.io/badge/MakeSense.ai-FF6F61?style=for-the-badge&logo=makesense&logoColor=white)](https://www.makesense.ai/)

## Passos para o desenvolvimento do software

- Criar o dataset com as imagens
    - Baixar as imagens
    - Criar as classes
    - Anotar as imagens
    - Dividir as imagens em treino e teste
- Configurar o arquivo data
- Treinar o modelo personalizado (YOLO)
- Testar o modelo

yolo detect train model=yolov8n.pt data=dataset/data.yaml epochs=50 imgsz=640 augment=true

yolo detect predict model=runs/detect/train/weights/best.pt source=videos 
