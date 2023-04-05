from PIL import Image

# Define the ASCII characters to be used
ascii_chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']

# Load the image
image = Image.open("image.jpg")

# Resize the image to a smaller size for faster processing
width, height = image.size
aspect_ratio = height/width
new_width = 100
new_height = int(aspect_ratio * new_width * 0.5)
resized_image = image.resize((new_width, new_height))

# Convert the resized image to grayscale
grayscale_image = resized_image.convert('L')

# Get the grayscale pixel values as a 1D array
pixels = list(grayscale_image.getdata())

# Convert the pixel values to ASCII characters
ascii_matrix = []
for i in range(new_height):
    row = pixels[i * new_width : (i + 1) * new_width]
    ascii_row = [ascii_chars[pixel//25] for pixel in row]
    ascii_matrix.append("".join(ascii_row))

# Print the ASCII art
print("\n".join(ascii_matrix))
