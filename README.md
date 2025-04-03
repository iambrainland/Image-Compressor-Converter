# Image Converter and Compressor

A Python script to convert and compress images into WEBP and JPG formats, ensuring a maximum file size of 120 KB while maintaining original dimensions and optimizing visual quality.

## Features
- Converts images to both **WEBP** and **JPG** formats.
- Compresses images to a maximum size of **120 KB** with adaptive quality adjustment.
- Preserves original image dimensions.
- Enhances image quality with sharpness, contrast, and color adjustments.
- Supports batch processing of multiple images in a folder.
- Logs conversion details to a file (`image_conversion.log`) for tracking.
- Handles common image formats: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`, `.webp`.

## Prerequisites
- **Python 3.x** installed on your system.
- **Pillow** library for image processing.

## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/image-converter-compressor.git
   cd image-converter-compressor
