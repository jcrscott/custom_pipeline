# Perform full OCR to get recognized text
ocr_result = ocr.ocr(corrected, rec=True, det=True, cls=True)

# Extract recognized text
recognized_text = [line[1][0] for line in ocr_result]