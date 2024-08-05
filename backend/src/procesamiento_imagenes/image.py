from PIL import Image
 
img_logo_python = Image.open("frontend/public/img/API - Frontend.png")

print(img_logo_python.format, img_logo_python.size, img_logo_python.mode)