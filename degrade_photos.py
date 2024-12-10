import os
from PIL import Image, ImageEnhance, ImageFilter, ImageOps


def create_degraded_versions(image_path):
    """Creates multiple degraded versions of an input image"""
    output_dir = "test_images/degraded"
    os.makedirs(output_dir, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(image_path))[0]
    base_name = base_name.replace("_clean", "")

    # Open and convert to RGB mode
    img = Image.open(image_path).convert("RGB")

    # 1. Reduce contrast and brightness
    low_quality = ImageEnhance.Contrast(img).enhance(0.5)
    low_quality = ImageEnhance.Brightness(low_quality).enhance(0.7)

    # 2. Add blur
    blurred = img.filter(ImageFilter.GaussianBlur(radius=2))

    # 3. Reduce resolution
    width, height = img.size
    low_res = img.resize((width // 2, height // 2), Image.Resampling.LANCZOS)
    low_res = low_res.resize((width, height), Image.Resampling.NEAREST)

    # 4. Convert to grayscale and back to simulate color loss
    bw_version = ImageOps.grayscale(img)
    color_degraded = bw_version.convert("RGB")

    # 5. Posterize to reduce color depth
    posterized = ImageOps.posterize(img, bits=3)

    # Save degraded versions
    low_quality.save(f"{output_dir}/{base_name}_contrast.png")
    blurred.save(f"{output_dir}/{base_name}_blur.png")
    low_res.save(f"{output_dir}/{base_name}_resolution.png")
    color_degraded.save(f"{output_dir}/{base_name}_color.png")
    posterized.save(f"{output_dir}/{base_name}_posterized.png")


create_degraded_versions("test_images/clean/eurotext_clean.png")
create_degraded_versions("test_images/clean/phototest_clean.png")
