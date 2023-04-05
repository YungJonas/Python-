from PIL import Image, ImageSequence
import os
import time

# Define the ASCII characters to be used
ascii_chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']

# Load the GIF image
image = Image.open("dancing-dog.gif")

# Get the number of frames in the GIF image
num_frames = image.n_frames

# Resize the GIF frames to a smaller size for faster processing
new_width = 100
aspect_ratio = image.height / image.width
new_height = int(aspect_ratio * new_width * 0.5)
resized_frames = []

for i in range(num_frames):
    image.seek(i)
    resized_frame = image.resize((new_width, new_height)).convert('L')
    resized_frames.append(resized_frame)

# Convert the resized frames to ASCII art
ascii_frames = []
for frame in resized_frames:
    pixels = list(frame.getdata())
    ascii_matrix = []
    for i in range(new_height):
        row = pixels[i * new_width: (i + 1) * new_width]
        ascii_row = [ascii_chars[pixel // 25] for pixel in row]
        ascii_matrix.append("".join(ascii_row))
    ascii_frames.append("\n".join(ascii_matrix))

# Print the ASCII animation
while True:
    for ascii_frame in ascii_frames:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(ascii_frame)
        time.sleep(0.1)
