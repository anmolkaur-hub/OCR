from fastapi  import FastAPI,HTTPException,File, UploadFile


from typing import Annotated
import logging

from app.template import parse_resume
import pymupdf



logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO
)

import pytesseract
from PIL import Image

image_paths=["../images/christian.jpeg","../images/shreya.jpeg","../images/ryan.jpeg"]

resume_texts=[]
for path in image_paths:
    resume_texts.append(pytesseract.image_to_string(Image.open(path)))

# for text in resume_texts:
#     print(text)



model="qwen2.5:0.5b"   

app=FastAPI()

@app.post('/welcome')
def welcome():
    logger.info("Welcom API hit")
    return {
        "message":"Welcome to Resume Parser"
    }




@app.post('/parse_resume')
def parse():
    logger.info("Resume parsing api hit")

    try:
        details=parse_resume(resume_texts)
        # for detail in details:
        #     print(detail)
    except Exception as e:
        logger.error(
            "Error occured",
            e
        )

        raise HTTPException(
            status_code=500,
            detail="Could not parse the resume"
        )

    logger.info("Resume parserd successfully")
    return {
        "success": True,
        "status_code": 201,
        "data": {
            "message": "Resume parsed successfully successfully",
            "details":details
            
        }
    }

@app.post("/parse_pdf")
async def upload_file(file: UploadFile = File(...)):
    try:
        pdf_text = []
        content = await file.read()
        doc = pymupdf.open(stream=content, filetype="pdf")

        for page in doc:
            text = page.get_text()
            pdf_text.append(text)

        parsed_text = parse_resume("\n".join(pdf_text))
        logger.info("PDF resume parsed successfully")

        return {
            "success": True,
            "status_code": 201,
            "data": {
                "message": "Resume parsed successfully",
                "details": parsed_text
            }
        }

    except Exception as e:
        logger.error(f"Error reading PDF: {e}")
        return {"success": False, "message": str(e)}