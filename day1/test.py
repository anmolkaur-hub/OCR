from PIL import Image
import pytesseract

# print(pytesseract.image_to_string(Image.open('../images/sartre_nausea.jpeg',"")))

print(pytesseract.image_to_string('../images/Best Resume Template Examples 2026 2026.jpeg'))

# print(pytesseract.get_languages(config=''))
# print(pytesseract.image_to_string(Image.open('../images/download (2).jpeg'), lang='jpn'))

# print(pytesseract.image_to_string('./image.txt'))