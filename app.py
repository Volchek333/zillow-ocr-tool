# app.py
import streamlit as st
import zipfile
import os
import tempfile
import pandas as pd
from PIL import Image
from utils.ocr_extract import extract_info_from_image

st.title("📸 Zillow Screenshot OCR Tool")

uploaded_zip = st.file_uploader("Upload a ZIP file of screenshots", type="zip")

if uploaded_zip:
    with tempfile.TemporaryDirectory() as tmpdir:
        with zipfile.ZipFile(uploaded_zip, "r") as zip_ref:
            zip_ref.extractall(tmpdir)

        results = []
        for filename in os.listdir(tmpdir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(tmpdir, filename)
                image = Image.open(img_path)
                info = extract_info_from_image(image)
                results.append(info)

        df = pd.DataFrame(results)
        st.success("✅ Extraction Complete")
        st.dataframe(df)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV", csv, "zillow_data.csv", "text/csv")
