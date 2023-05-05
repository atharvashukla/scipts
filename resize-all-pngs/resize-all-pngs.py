import os
import sys
from PIL import Image

def resize_images(scale_factor, input_dir, output_dir):
    # Create output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".png"):
            # Open image file
            input_path = os.path.join(input_dir, filename)
            image = Image.open(input_path)

            # Calculate new size
            width, height = image.size
            new_width = int(scale_factor * width)
            new_height = int(scale_factor * height)

            # Resize image
            image = image.resize((new_width, new_height))

            # Save resized image
            output_path = os.path.join(output_dir, filename)
            image.save(output_path)

if __name__ == "__main__":
    # Get command-line arguments
    scale_factor = float(sys.argv[1])
    input_dir = sys.argv[2]
    output_dir = sys.argv[3]

    # Resize images and save them to output directory
    resize_images(scale_factor, input_dir, output_dir)