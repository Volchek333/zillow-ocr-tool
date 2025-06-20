# utils/ocr_extract.py
import easyocr
import re

reader = easyocr.Reader(['en'])

def extract_info_from_image(image):
    results = reader.readtext(image, detail=0)
    text = " ".join(results)

    phone_pattern = re.search(r'(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})', text)
    name_pattern = re.search(r'Agent[:\-]?\s*(.+)', text, re.IGNORECASE)
    address_pattern = re.search(r'\d{3,} .+?, [A-Z]{2} \d{5}', text)

    return {
        "Agent Name": name_pattern.group(1).strip() if name_pattern else "N/A",
        "Agent Phone Number": phone_pattern.group(1).strip() if phone_pattern else "N/A",
        "Address": address_pattern.group(0).strip() if address_pattern else "N/A"
    }

