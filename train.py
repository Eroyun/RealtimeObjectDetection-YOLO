from ultralytics import YOLO
import torch

if torch.cuda.is_available():
    torch.cuda.set_device(0)
else:
    print("CUDA is not available. Running on CPU.")

if __name__ == '__main__':
    # load a pretrained model (recommended for training)
    model = YOLO("yolov8m-oiv7.pt")

    # Use the model
    results = model.train(data='coco128.yaml', epochs=100,
                          imgsz=640)
