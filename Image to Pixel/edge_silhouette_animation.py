import cv2
import numpy as np
import math

# ==========================
# CONFIG
# ==========================

INPUT_VIDEO = "input.mp4"
OUTPUT_VIDEO = "output_silhouette.mp4"

PIXEL_SIZE = 16          # bigger = more abstraction
FRAME_SKIP = 2
EDGE_THRESHOLD_1 = 60
EDGE_THRESHOLD_2 = 140
SILHOUETTE_THICKNESS = 2
ROTATION_DRIFT = 1.2     # degrees

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

    # 1. Grayscale (kill color identity)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 2. Blur (remove detail)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)

    # 3. Edge detection
    edges = cv2.Canny(gray, EDGE_THRESHOLD_1, EDGE_THRESHOLD_2)

    # 4. Thicken edges (silhouette look)
    kernel = np.ones((SILHOUETTE_THICKNESS, SILHOUETTE_THICKNESS), np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=1)

    # 5. Convert to solid silhouette
    silhouette = np.zeros_like(edges)
    silhouette[edges > 0] = 255

    # 6. Pixelate
    sw = max(1, width // PIXEL_SIZE)
    sh = max(1, height // PIXEL_SIZE)

    small = cv2.resize(silhouette, (sw, sh), interpolation=cv2.INTER_LINEAR)
    pixelated = cv2.resize(small, (width, height), interpolation=cv2.INTER_NEAREST)

    # 7. Convert to 3-channel for video
    pixelated = cv2.cvtColor(pixelated, cv2.COLOR_GRAY2BGR)

    # 8. Subtle rotation drift (break camera identity)
    angle = math.sin(written * 0.05) * ROTATION_DRIFT
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

print("Edge-only silhouette animation created:", OUTPUT_VIDEO)
