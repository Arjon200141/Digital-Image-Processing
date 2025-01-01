from PIL import Image
import numpy as np

# Open the image file
image_path = 'Flag_of_Bangladesh.svg.png'  # Replace with your image path
img = Image.open(image_path)

# Convert the image to grayscale
gray_img = img.convert('L')

# Convert the grayscale image to a binary image (thresholding)
threshold = 128  # You can change this value based on the image's brightness
binary_img = gray_img.point(lambda p: p > threshold and 255)

# Show the binary image
binary_img.show()
