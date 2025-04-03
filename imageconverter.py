from PIL import Image, ImageEnhance
import os
from pathlib import Path
import logging

def setup_logging(log_file="image_conversion.log"):
    """Set up logging configuration to overwrite the log file each run."""
    logging.getLogger('').handlers = []
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='w'  # Overwrite mode
    )

def optimize_image(input_path, output_path_webp, output_path_jpg, max_size_kb=120, initial_quality=100):
    """
    Convert to WEBP and JPG with highest quality, ensuring file size <= 120 KB, maintaining dimensions.
    
    Args:
        input_path (str): Path to input image
        output_path_webp (str): Path to save output WEBP image
        output_path_jpg (str): Path to save output JPG image
        max_size_kb (int): Maximum file size in kilobytes (fixed at 120 KB)
        initial_quality (int): Starting quality setting (0-100)
    """
    try:
        # Open the image
        img = Image.open(input_path)
        
        # Store original dimensions and size
        original_width, original_height = img.size
        original_size = os.path.getsize(input_path) / 1024  # in KB
        
        # Convert to RGB if needed
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
            
        # Apply quality enhancements for best visual quality
        img = ImageEnhance.Sharpness(img).enhance(1.4)  # Sharpness
        
        img = ImageEnhance.Contrast(img).enhance(1.1)  # Contrast
        
        img = ImageEnhance.Color(img).enhance(1.2)  # Vivid colors
        
        # Initial compression with high quality for WEBP
        quality = initial_quality
        img.save(output_path_webp, 'WEBP',
                quality=quality,
                method=4,  # Fast and efficient compression
                exact=False,
                optimize=True)
        
        # Initial compression with high quality for JPG
        img.save(output_path_jpg, 'JPEG',
                quality=quality,
                optimize=True)
        
        current_size_webp = os.path.getsize(output_path_webp) / 1024
        current_size_jpg = os.path.getsize(output_path_jpg) / 1024
        
        # Adjust quality to ensure size <= 120 KB for WEBP
        while current_size_webp > max_size_kb and quality > 20:
            quality -= 5  # Step down quality to reach target
            img.save(output_path_webp, 'WEBP',
                    quality=quality,
                    method=4,
                    exact=False,
                    optimize=True)
            current_size_webp = os.path.getsize(output_path_webp) / 1024
        
        # Adjust quality to ensure size <= 120 KB for JPG
        while current_size_jpg > max_size_kb and quality > 20:
            quality -= 5  # Step down quality to reach target
            img.save(output_path_jpg, 'JPEG',
                    quality=quality,
                    optimize=True)
            current_size_jpg = os.path.getsize(output_path_jpg) / 1024
        
        # Log results for both formats
        final_size_webp = os.path.getsize(output_path_webp) / 1024
        final_size_jpg = os.path.getsize(output_path_jpg) / 1024
        
        if final_size_webp > max_size_kb or final_size_jpg > max_size_kb:
            logging.warning(f"Could not compress {Path(input_path).name} below {max_size_kb} KB with quality > 20")
        
        log_message = (
            f"Converted: {Path(input_path).name} -> "
            f"WEBP: {Path(output_path_webp).name} ({final_size_webp:.2f} KB) | "
            f"JPG: {Path(output_path_jpg).name} ({final_size_jpg:.2f} KB) | "
            f"Original: {original_size:.2f} KB | "
            f"Quality: {quality} | "
            f"Dimensions: {original_width}x{original_height}"
        )
        logging.info(log_message)
        print(log_message)
        
    except Exception as e:
        error_message = f"Error processing {input_path}: {str(e)}"
        logging.error(error_message)
        print(error_message)

def process_folder(input_folder, output_folder):
    """
    Process all images in input folder and save to output folder in WEBP and JPG with max 120 KB size.
    """
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp')
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(valid_extensions):
            input_path = os.path.join(input_folder, filename)
            output_filename_webp = Path(filename).stem + '.webp'
            output_filename_jpg = Path(filename).stem + '.jpg'
            output_path_webp = os.path.join(output_folder, output_filename_webp)
            output_path_jpg = os.path.join(output_folder, output_filename_jpg)
            
            print(f"Processing: {filename}")
            optimize_image(input_path, output_path_webp, output_path_jpg)

def main():
    """Main function to set up logging and process images in a folder."""
    # Set your folder paths here
    input_folder = "path/to/your/input/folder"  # Replace with your input folder path
    output_folder = "path/to/your/output/folder"  # Replace with your output folder path
    
    setup_logging("image_conversion.log") # Initialize logging
    logging.info(f"Starting batch conversion: Input={input_folder}, Output={output_folder}")
    process_folder(input_folder, output_folder) # Start processing images
    logging.info("Batch conversion completed")

if __name__ == "__main__":
    try:
        from PIL import Image
    except ImportError:
        print("Pillow library not found. Please install it using: pip install Pillow")
        exit()
    main()
    
