from paddleocr import PaddleOCR

ocr = PaddleOCR(
    lang="en"
)

image_path = "../images/sartre_nausea.jpeg"

result = ocr.predict(image_path)

for res in result:
    print(res)