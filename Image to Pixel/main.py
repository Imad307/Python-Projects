from PIL import Image
from PIL.Image import Resampling

import os

def pixel_art(
        input_image_path,
        output_image_path,
        pixel_width=128,
        palette_colors=32
):
    """
    Converts a real image into pixel-art style.
    """

    # Load image
    img = Image.open(input_image_path).convert("RGB")

    # Preserve aspect ratio
    aspect_ratio = img.height / img.width
    new_height = int(pixel_width * aspect_ratio)

    # Step 1: Downscale (pixel blocks)
    small_img = img.resize(
        (pixel_width, new_height),
        Resampling.NEAREST
    )

    # Step 2: Reduce color palette
    pixel_img = small_img.convert(
        "P",
        palette=Image.ADAPTIVE,
        colors=palette_colors
    )

    # Step 3: Upscale back to original size
    final_img = pixel_img.resize(
        img.size,
        Resampling.NEAREST
    )

    # Save output image
    final_img.save(output_image_path)
    print(f"Pixel art saved to: {output_image_path}")


if __name__ == "__main__":
    INPUT_IMAGE = r"C:\Users\LOGICO\Downloads\pexels-moose-photos-170195-1036622.jpg"
    OUTPUT_IMAGE = r"C:\Users\LOGICO\Downloads\pixel_output_woman.png"

    PIXEL_WIDTH = 128      # 64 = very blocky, 128 = classic, 256 = modern
    PALETTE_COLORS = 32    # 16 = retro, 32 = SNES, 64 = modern

    print(os.path.exists(INPUT_IMAGE))

    pixel_art(
        INPUT_IMAGE,
        OUTPUT_IMAGE,
        PIXEL_WIDTH,
        PALETTE_COLORS
    )
