from PIL import Image
import  pytesseract

image = Image.open('./image.png')

result = pytesseract.image_to_string(image)

print(result)