# utils/ocr_extract.py
from PIL import Image
import pytesseract
import re

def extract_info_from_image(image: Image.Image):
    text = pytesseract.image_to_string(image)

    phone_pattern = re.search(r'(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})', text)
    name_pattern = re.search(r'Agent[:\-]?\s*(.+)', text, re.IGNORECASE)
    address_pattern = re.search(r'\d{3,} .+, [A-Z]{2} \d{5}', text)

    return {
        "Agent Name": name_pattern.group(1).strip() if name_pattern else "N/A",
        "Agent Phone Number": phone_pattern.group(1).strip() if phone_pattern else "N/A",
        "Address": address_pattern.group(0).strip() if address_pattern else "N/A"
    }
