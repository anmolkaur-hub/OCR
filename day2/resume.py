from PIL import Image
import pytesseract
import re

text = pytesseract.image_to_string('../images/resume.jpeg')

with open('resume_text.txt', 'w') as file:
    file.write(text)

print(text)

phone = re.search(r'\d{11}', text)

print(f"Phone: {phone.group()}")


email = re.search(r'[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+', text)

print(f"Email: {email.group()}")

dob = re.search(r'[A-Za-z]+\s+\d{1,2},\s+\d{4}', text)


print(f"Date of birth: {dob.group()}")