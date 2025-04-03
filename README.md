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

## Usage Guide

This guide will walk you through using the Image Converter and Compressor step-by-step. Even if you’re new to Python, you’ll find it easy to follow! We’ll also show you exactly what you’ll see in your terminal so you know what to expect.

### Quick Start

1. **Prepare your images**: Put the images you want to convert into a folder (e.g., `images/`).
2. **Edit the script**: Open `imageconverter.py` in a text editor and set your folder paths in the `main()` function:

    ```python
    input_folder = "path/to/your/input/folder"  # Example: "C:\\Users\\YourName\\Pictures\\input"
    output_folder = "path/to/your/output/folder"  # Example: "C:\\Users\\YourName\\Pictures\\output"
    ```
3. **Run the script**: Open a terminal, navigate to the script’s folder, and type:

    ```bash
    python imageconverter.py
    ```
4. **Check the output**: Look in your `output_folder` for `.webp` and `.jpg` files, and check `image_conversion.log` for details.

---

## Detailed Steps

### 1. Folder Setup

- Create a folder for your images, like `C:\Users\YourName\Pictures\input`.
- Put some images there (e.g., `photo.png`, `vacation.jpg`).
- Decide where you want the converted images to go, like `C:\Users\YourName\Pictures\output`.

### 2. Modify the Script

- Open `imageconverter.py` in a text editor.
- Find the `main()` function near the bottom and change the paths:

    ```python
    input_folder = "C:\\Users\\YourName\\Pictures\\input"
    output_folder = "C:\\Users\\YourName\\Pictures\\output"
    ```
![image](https://github.com/user-attachments/assets/87e25f8f-ad93-4572-85bf-ba2474bfc26c)

- Save the file.

### 3. Run the Script

- Open your terminal:
  - **Windows**: Press `Win + R`, type `cmd`, and hit Enter.
  - **Mac/Linux**: Search for “Terminal” and open it.
- Navigate to the script’s folder:

    ```bash
    cd C:\path\to\image-converter-compressor
    ```
- Run the script:

    ```bash
    python imageconverter.py
    ```

### 4. What You’ll See (Prints)

The script will process each image and print updates. Example:

```
Processing: photo.png
Converted: photo.png -> WEBP: photo.webp (115.23 KB) | JPG: photo.jpg (118.45 KB) | Original: 250.67 KB | Quality: 85 | Dimensions: 1920x1080
Processing: vacation.jpg
Converted: vacation.jpg -> WEBP: vacation.webp (110.12 KB) | JPG: vacation.jpg (117.89 KB) | Original: 300.45 KB | Quality: 90 | Dimensions: 1280x720
```
![image](https://github.com/user-attachments/assets/9899d9ca-df17-4c12-8673-45224265500b)


If an error occurs:

```
Processing: broken.tiff
Error processing C:\Users\YourName\Pictures\input\broken.tiff: Unsupported format
```

### 5. Review Results

Go to your `output_folder`. You’ll see:

```
photo.webp, photo.jpg
vacation.webp, vacation.jpg
```

Check `image_conversion.log` for details:

```
2025-04-03 10:00:00,123 - INFO - Starting batch conversion: Input=C:\Users\YourName\Pictures\input, Output=C:\Users\YourName\Pictures\output
2025-04-03 10:00:00,456 - INFO - Converted: photo.png -> WEBP: photo.webp (115.23 KB) | JPG: photo.jpg (118.45 KB) | Quality: 85 | Dimensions: 1920x1080
```

---

## Advanced Usage

### 1. Change the Log File

Modify `main()` to:

```python
setup_logging("my_log.txt")
```

### 2. Process a Single Image

To process a single image file, all you need to do is to just have the single file only in the input folder.

### 3. Increase File Size Limit

Modify `process_folder()`:

```python
process_folder(input_folder, output_folder, max_size_kb=200)
```

---

## How It Works

1. **Conversion**: Converts images to WEBP and JPG with an initial quality of 100.
2. **Compression**: Reduces quality in steps of 5 until file size is ≤ 120 KB (min quality: 20).
3. **Enhancements**: Improves sharpness, contrast, and color.
4. **Logging**: Records file sizes, quality settings, and dimensions.

---

## Supported Formats

- **Input**: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`, `.webp`
- **Output**: `.webp`, `.jpg`

---

## Troubleshooting

| Issue | Solution |
|--------|----------|
| `Pillow not found` | Install it: `pip install Pillow` |
| `File size too large` | Quality may have reached the minimum (20) without meeting 120 KB. |
| `Unsupported format` | Check `image_conversion.log` for details. |

---

## Contributing

Feel free to fork this repository, submit issues, or create pull requests to improve the script!


