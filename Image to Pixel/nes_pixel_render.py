import cv2
import numpy as np
import math

# ==========================
# CONFIG
# ==========================

INPUT_VIDEO = "input.mp4"
OUTPUT_VIDEO = "output_nes.mp4"

PIXEL_SIZE = 20       # larger = more abstraction
FRAME_SKIP = 2        # drop frames
ROTATION_DRIFT = 1.5  # degrees

# ==========================
# NES PALETTE (RGB)
# ==========================

NES_PALETTE = np.array([
    [0, 0, 0],        # black
    [255, 255, 255],  # white
    [124, 124, 124],  # gray
    [188, 188, 188],  # light gray
    [252, 0, 0],      # red
    [188, 0, 0],      # dark red
    [0, 168, 0],      # green
    [0, 104, 0],      # dark green
    [0, 0, 252],      # blue
    [0, 0, 168],      # dark blue
    [252, 216, 0],    # yellow
    [168, 168, 0],    # olive
    [0, 252, 252],    # cyan
    [0, 168, 168],    # teal
], dtype=np.uint8)

# ==========================
# PALETTE MAPPING
# ==========================

def apply_nes_palette(img):
    h, w, _ = img.shape

    flat = img.reshape(-1, 3).astype(np.int16)
    palette = NES_PALETTE.astype(np.int16)

    # Squared Euclidean distance (NO sqrt)
    distances = ((flat[:, None, :] - palette[None, :, :]) ** 2).sum(axis=2)

    nearest = palette[np.argmin(distances, axis=1)]
    return nearest.reshape(h, w, 3).astype(np.uint8)
# ==========================
# LOAD VIDEO
# ==========================

cap = cv2.VideoCapture(INPUT_VIDEO)
if not cap.isOpened():
    raise IOError("Cannot open input video")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) / FRAME_SKIP

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(OUTPUT_VIDEO, fourcc, fps, (width, height))

frame_idx = 0
written = 0

# ==========================
# PROCESS FRAMES
# ==========================

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_idx += 1
    if frame_idx % FRAME_SKIP != 0:
        continue

    # 1. Blur (kill realism)
    frame = cv2.GaussianBlur(frame, (7, 7), 0)

    # 2. Downscale
    sw = max(1, width // PIXEL_SIZE)
    sh = max(1, height // PIXEL_SIZE)
    small = cv2.resize(frame, (sw, sh), interpolation=cv2.INTER_LINEAR)

    # 3. NES palette mapping
    nes = apply_nes_palette(small)

    # 4. Upscale to pixel art
    pixelated = cv2.resize(nes, (width, height), interpolation=cv2.INTER_NEAREST)

    # 5. Subtle rotation drift
    angle = math.sin(written * 0.04) * ROTATION_DRIFT
    mat = cv2.getRotationMatrix2D((width // 2, height // 2), angle, 1.0)
    pixelated = cv2.warpAffine(
        pixelated,
        mat,
        (width, height),
        flags=cv2.INTER_NEAREST,
        borderMode=cv2.BORDER_REFLECT
    )

    out.write(pixelated)
    written += 1

# ==========================
# CLEANUP
# ==========================

cap.release()
out.release()
cv2.destroyAllWindows()

print("NES-style pixel video created:", OUTPUT_VIDEO)
