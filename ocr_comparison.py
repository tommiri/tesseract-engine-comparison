import pytesseract
from PIL import Image
import time
import os
from tqdm import tqdm


def process_image(image_path, oem_mode=1):
    """
    Process image using specified Tesseract OCR Engine Mode
    oem_mode 1: Neural nets LSTM engine only (default)
    oem_mode 0: Legacy engine only (requires additional components)
    """
    start_time = time.time()

    try:
        if oem_mode == 0:
            # Use legacy tessdata for legacy mode
            tessdata_dir = os.path.join(os.getcwd(), "tessdata")
            custom_config = f"--oem {oem_mode} --tessdata-dir {tessdata_dir}"
        else:
            # Use default tessdata for LSTM
            custom_config = f"--oem {oem_mode}"

        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, config=custom_config)

        end_time = time.time()
        processing_time = end_time - start_time

        return text.strip(), processing_time
    except pytesseract.TesseractError as e:
        print(f"Error processing image with OEM mode {oem_mode}: {str(e)}")
        return "", 0
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return "", 0


def write_to_file(file_path, content):
    with open(file_path, "a") as file:
        file.write(content + "\n")


def compare_ocr_methods(image_path, output_file):
    try:
        legacy_text, legacy_time = process_image(image_path, 0)
        write_to_file(
            output_file,
            f"=== Legacy Tesseract ===\nTime taken: {legacy_time:.2f} seconds\nText extracted:\n{legacy_text}",
        )
    except Exception as e:
        write_to_file(output_file, f"Legacy Tesseract failed: {str(e)}")

    lstm_text, lstm_time = process_image(image_path, 1)
    write_to_file(
        output_file,
        f"\n=== LSTM Tesseract ===\nTime taken: {lstm_time:.2f} seconds\nText extracted:\n{lstm_text}",
    )


def test_multiple_images(directory, output_file):
    """Test OCR on all images in a directory"""
    if not os.path.exists(directory):
        write_to_file(output_file, f"Directory not found: {directory}")
        return

    image_files = [
        f for f in os.listdir(directory) if f.endswith((".png", ".jpg", ".tif"))
    ]
    for image_file in tqdm(image_files, desc="Processing images"):
        image_path = os.path.join(directory, image_file)
        write_to_file(output_file, f"\nTesting: {image_file}")
        compare_ocr_methods(image_path, output_file)


if __name__ == "__main__":
    import sys

    output_file = "ocr_results.txt"
    # Clear the contents of the output file at the beginning
    open(output_file, "w").close()

    if len(sys.argv) > 1:
        test_directory = sys.argv[1]
        test_multiple_images(test_directory, output_file)
    else:
        image_path = "sample.png"
        compare_ocr_methods(image_path, output_file)

    print(f"Results have been stored in {output_file}")
