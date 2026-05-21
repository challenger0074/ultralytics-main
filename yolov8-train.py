from ultralytics import YOLO
# Load a model
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
# Train the model
model.train(data='yolov8-bvn.yaml', epochs=50, imgsz=640, batch=16, workers=0)  # train the model