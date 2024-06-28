from PIL import Image
import os

def optimize_image(input_path, output_path, quality=85, max_width=None, max_height=None):
    """
    Optimize an image by resizing and adjusting its quality.

    :param input_path: Path to the input image file.
    :param output_path: Path to save the optimized image file.
    :param quality: Image quality for the output (1 to 100).
    :param max_width: Maximum width for resizing (optional).
    :param max_height: Maximum height for resizing (optional).
    """
    try:
        # Open an image file
        with Image.open(input_path) as img:
            print(f"Optimizing {input_path}...")

            # Resize the image if max_width or max_height is specified
            if max_width or max_height:
                img.thumbnail((max_width, max_height), Image.ANTIALIAS)

            # Save the image with the specified quality
            img.save(output_path, optimize=True, quality=quality)
            print(f"Saved optimized image to {output_path}")

    except Exception as e:
        print(f"Error optimizing {input_path}: {e}")

def optimize_images_in_directory(directory, output_directory, quality=85, max_width=None, max_height=None):
    """
    Optimize all images in the specified directory.

    :param directory: Directory containing images to optimize.
    :param output_directory: Directory to save optimized images.
    :param quality: Image quality for the output (1 to 100).
    :param max_width: Maximum width for resizing (optional).
    :param max_height: Maximum height for resizing (optional).
    """
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        input_path = os.path.join(directory, filename)
        output_path = os.path.join(output_directory, filename)

        # Check if the file is an image
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
            optimize_image(input_path, output_path, quality, max_width, max_height)

# Example usage
if __name__ == "__main__":
    input_dir = "input_images"  # Replace with your input directory
    output_dir = "optimized_images"  # Replace with your output directory
    image_quality = 85  # Adjust quality as needed (1 to 100)
    max_img_width = 800  # Replace with max width or None
    max_img_height = 600  # Replace with max height or None

    optimize_images_in_directory(input_dir, output_dir, quality=image_quality, max_width=max_img_width, max_height=max_img_height)