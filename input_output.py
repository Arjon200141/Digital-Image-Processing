from PIL import Image

# Open an image file (input)
input_image_path = 'Flag_of_Bangladesh.svg.png'
img = Image.open(input_image_path)

# Show the output image
img.show()

print("Image will be shown as output image")
