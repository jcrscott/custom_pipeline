# Initialize PaddleOCR with text detection and angle classification
ocr = PaddleOCR(use_angle_cls=True, lang='en', rec=True, det=True)

# Perform OCR detection
detection_result = ocr.ocr(corrected, rec=False)

# Extract bounding boxes and regions
text_boxes = [line[0] for line in detection_result]