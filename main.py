
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import pytesseract
from PIL import Image
import io

app = FastAPI()

# Tesseract OCR path (required for Windows systems, adjust the path accordingly)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path

# Endpoint to handle image upload and OCR
@app.post("/scan-receipt/")
async def scan_receipt(file: UploadFile = File(...)):
    try:
        # Read the image
        image = Image.open(io.BytesIO(await file.read()))
        
        # Perform OCR
        extracted_text = pytesseract.image_to_string(image)
        
        return JSONResponse(content={"extracted_text": extracted_text})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
