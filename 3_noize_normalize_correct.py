# Convert to grayscale
gray = cv2.cvtColor(de_skewed, cv2.COLOR_BGR2GRAY)

# Denoise image
denoised = cv2.fastNlMeansDenoising(gray, None, 30, 7, 21)

# Normalize image
normalized = cv2.normalize(denoised, None, 0, 255, cv2.NORM_MINMAX)

# Optionally apply thresholding
_, corrected = cv2.threshold(normalized, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)