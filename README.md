# Tesseract OCR Engine Comparison Tool

A Python tool to compare performance and accuracy between:

- Modern LSTM neural network engine (Tesseract 4.0+)
- Legacy pattern matching engine (Original Tesseract approach)

## Requirements

- Python 3.8+
- Tesseract OCR with both engines:
  - LSTM (default installation)
  - Legacy engine (requires additional tessdata)
- Python packages:
  - pytesseract
  - PIL/Pillow

## Installation

1. Clone the repository:

```bash
git clone https://github.com/tommiri/tesseract-engine-comparison.git
cd tesseract-engine-comparison
```

2. Install Tesseract OCR:

```bash
# Ubuntu/Debian
sudo apt install tesseract-ocr
```

3. Set up Python environment:

```bash
# Create and activate virtual environment
python3 -m venv tesseract_env
source tesseract_env/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt
```

## Usage

**Single Image Comparison**

```bash
python3 ocr_comparison.py path/to/image.png
```

**Multiple Image Testing**

```bash
python3 ocr_comparison.py path/to/image/directory
```

**Creating Degraded Versions of Images**

To create degraded versions of images for testing, use the `degrade_photos.py` script:

```bash
python3 degrade_photos.py
```

This will generate multiple degraded versions of the images located in the `test_images/clean` directory and save them in the `test_images/degraded` directory.

### OCR Modes

The tool uses two OCR modes configured in `process_image()`:

- `oem_mode=1`: LSTM only (default)
- `oem_mode=0`: Legacy engine only

## Output example

The results of the OCR comparison are written to `ocr_results.txt`. Here is an example of the output:

```txt
=== Legacy Tesseract ===
Time taken: 1.23 seconds
Text extracted:
[Legacy engine output]

=== LSTM Tesseract ===
Time taken: 0.85 seconds
Text extracted:
[LSTM engine output]
```

## Project Structure

```
tessdata/              # Legacy engine data
test_images/
  ├── clean/          # Original test images
  └── degraded/       # Generated degraded versions
ocr_comparison.py     # Main OCR comparison script
degrade_photos.py     # Image degradation script
ocr_results.txt       # Comparison results output
```

### Image Degradation

The `degrade_photos.py` script creates the following variations:

- `*_contrast.png`: Reduced contrast and brightness
- `*_blur.png`: Added Gaussian blur
- `*_resolution.png`: Reduced and upscaled resolution
- `*_color.png`: Grayscale conversion
- `*_posterized.png`: Reduced color depth

These degraded versions help test OCR engine robustness under different image conditions.

## License

This project is open source and available under standard open source licenses.
