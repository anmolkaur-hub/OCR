
import easyocr
reader = easyocr.Reader(['hi'])
result = reader.readtext('../images/download (2).jpeg')
print(result)


reader = easyocr.Reader(['ja'])
result = reader.readtext('../images/japanese.jpeg')
print(result)


# reader = easyocr.Reader(['ch_sim','en'])
# result = reader.readtext('../images/Best Resume Template Examples 2026 2026.jpeg')

for _, text, _ in result:
    print(text)