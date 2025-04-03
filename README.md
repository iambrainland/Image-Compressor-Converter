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
   git clone https://github.com/iambrainland/image-converter-compressor.git
   cd image-converter-compressor

2025-04-03 10:00:00,123 - INFO - Converted: photo.png -> WEBP: photo.webp (115.23 KB) | JPG: photo.jpg (118.45 KB) | Original: 250.67 KB | Quality: 85 | Dimensions: 1920x1080
![image](https://github.com/user-attachments/assets/4e8f6e04-e450-4242-b175-e2d2c190e4cb)
