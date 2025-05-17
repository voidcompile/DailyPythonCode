import cv2

# Load the image
image = cv2.imread('image1.jpg')

# Convert to gray scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
inverted = 255 - gray

# Apply Gaussian blur
blurred = cv2.GaussianBlur(inverted, (21, 21), 0)

# Invert the blurred image
inverted_blur = 255 - blurred

# Create the pencil sketch
sketch = cv2.divide(gray, inverted_blur, scale=256.0)

# Show the result
cv2.imshow("Original", image)
cv2.imshow("Pencil Sketch", sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()
