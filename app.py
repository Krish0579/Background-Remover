from rembg import remove
from PIL import Image
import io 
in_path = 'img.png'
out_path = 'output.png'
with open ('img.jpg','rb') as in_file:
    in_data = in_file.read()
out_data = remove(in_data)
out_img = Image.open(io.BytesIO(out_data))
out_img.save(out_path)
print("Background removed successfully")