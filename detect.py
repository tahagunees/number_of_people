import torch
from PIL import Image


model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)  

model.eval()


img = Image.open(r"C:\Users\taha\Desktop\Yeni klasör\image.jpg")  


results = model(img)




results_df = results.pandas().xyxy[0]


people_count = results_df[results_df['name'] == 'person'].shape[0]
print(f"Detected people count: {people_count}")
