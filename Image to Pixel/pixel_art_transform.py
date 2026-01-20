import cv2
import math

# ==========================
# CONFIG
# ==========================

INPUT_VIDEO = "input.mp4"
OUTPUT_VIDEO = "output_art.mp4"

PIXEL_SIZE = 10          # bigger = less resemblance
COLOR_LEVELS = 8         # lower = more abstract
FRAME_SKIP = 2           # keep 1 frame, skip 2
MAX_ROTATION = 2.5       # degrees

# ==========================
# HELPERS
# ==========================

def quantize_colors(img, levels):
    step = 256 // levels
    return (img // step) * step

# ==========================
# LOAD VIDEO
# ==========================

cap = cv2.VideoCapture(INPUT_VIDEO)
if not cap.isOpened():
    raise IOError("Cannot open video")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) / FRAME_SKIP

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(OUTPUT_VIDEO, fourcc, fps, (width, height))

frame_index = 0
written_frames = 0

# ==========================
# PROCESS
# ==========================

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_index += 1
    if frame_index % FRAME_SKIP != 0:
        continue

    # 1. Blur (destroy detail)
    frame = cv2.GaussianBlur(frame, (9, 9), 0)

    # 2. Downscale
    small_w = max(1, width // PIXEL_SIZE)
    small_h = max(1, height // PIXEL_SIZE)
    small = cv2.resize(frame, (small_w, small_h), interpolation=cv2.INTER_LINEAR)

    # 3. Color quantization
    small = quantize_colors(small, COLOR_LEVELS)

    # 4. Pixel upscale
    pixelated = cv2.resize(small, (width, height), interpolation=cv2.INTER_NEAREST)

    # 5. Rotational drift
    angle = math.sin(written_frames * 0.05) * MAX_ROTATION
    matrix = cv2.getRotationMatrix2D((width // 2, height // 2), angle, 1.0)
    pixelated = cv2.warpAffine(
        pixelated,
        matrix,
        (width, height),
        flags=cv2.INTER_NEAREST,
        borderMode=cv2.BORDER_REFLECT
    )

    out.write(pixelated)
    written_frames += 1

# ==========================
# CLEANUP
# ==========================

cap.release()
out.release()
cv2.destroyAllWindows()

print("Artistic pixel video generated:", OUTPUT_VIDEO)
