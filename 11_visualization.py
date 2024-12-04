import cv2

# Function to draw labeled boxes
def draw_labels(image, mapped_entities, df):
    for field, value in mapped_entities.items():
        # Find the text in DataFrame
        match = df[df['text'] == value]
        if not match.empty:
            bbox = match.iloc[0]['bbox']
            # Draw bounding box
            pts = np.array(bbox).astype(int)
            cv2.polylines(image, [pts], isClosed=True, color=(0, 255, 0), thickness=2)
            # Put label
            cv2.putText(image, f"{field}: {value}", (pts[0][0], pts[0][1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return image

# Draw labels on the de-skewed image
labeled_image = draw_labels(de_skewed.copy(), mapped_entities, df)

# Save or display the image
cv2.imwrite('labeled_license.jpg', labeled_image)
# Or display using OpenCV
# cv2.imshow('Labeled License', labeled_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()