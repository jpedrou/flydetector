## Passos para o desenvolvimento do software

- Criar o dataset com as imagens
    - Baixar as imagens
    - Baixar e instalar o labelImg
    - Anotar as imagens
    - Dividir as imagens em treino e teste
- Configurar o arquivo data
- Configurar o arquivo cfg
- Trinar o modelo personalizado (YOLO)
- Testar o modelo

https://github.com/HumanSignal/labelImg

yolo detect train data=dataset/data.yaml model=yolov8n.pt epochs=10 imgsz=640

yolo detect predict model=runs/detect/train/weights/best.pt source=videos 
