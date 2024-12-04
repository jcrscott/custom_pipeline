import cv2
from paddleocr import PaddleOCR

# Initialize PaddleOCR with layout analysis
ocr = PaddleOCR(use_angle_cls=True, lang='en', rec=False, det=True)

# Perform detection
result = ocr.ocr('input.jpg', rec=False, cls=True)

# Assume result contains bounding boxes for the document
# Extract the largest bounding box as the document
document_box = max(result, key=lambda x: x[0][2])[0]

# Convert to integer
document_box = [tuple(map(int, point)) for point in document_box]

# Apply perspective transform to crop and correct orientation
def four_point_transform(image, pts):
    rect = cv2.boundingRect(np.array(pts))
    x, y, w, h = rect
    cropped = image[y:y+h, x:x+w]
    return cropped

image = cv2.imread('input.jpg')
cropped_image = four_point_transform(image, document_box)

# De-skew using OpenCV
gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
coords = cv2.findNonZero(gray)
angle = cv2.minAreaRect(coords)[-1]
if angle < -45:
    angle = -(90 + angle)
else:
    angle = -angle

(h, w) = cropped_image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
de_skewed = cv2.warpAffine(cropped_image, M, (w, h),
                           flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)