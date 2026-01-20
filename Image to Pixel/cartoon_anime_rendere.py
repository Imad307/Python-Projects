import cv2
import numpy as np

# ==========================
# CONFIG
# ==========================
INPUT_VIDEO = "input.mp4"
OUTPUT_VIDEO = "output_anime_style.mp4"

K_COLORS = 8            # number of colors per frame
SMOOTHING = 5           # bilateral filter strength
EDGE_THRESHOLD = 80     # for major edges
PIXELATE_SIZE = 1       # optional downscale/upscale for soft pixelization

# ==========================
# HELPERS
# ==========================
def quantize_kmeans(frame, k=8):
    Z = frame.reshape((-1,3))
    Z = np.float32(Z)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, labels, centers = cv2.kmeans(Z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    res = centers[labels.flatten()]
    return res.reshape(frame.shape)

# ==========================
# LOAD VIDEO
# ==========================
cap = cv2.VideoCapture(INPUT_VIDEO)
if not cap.isOpened():
    raise IOError("Cannot open video")

width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(OUTPUT_VIDEO, fourcc, fps, (width, height))

# ==========================
# PROCESS FRAMES
# ==========================
while True:
    ret, input_frame = cap.read()
    if not ret:
        break

    # 1. Smooth frame for anime-like flat colors
    smooth = cv2.bilateralFilter(input_frame, d=SMOOTHING, sigmaColor=150, sigmaSpace=150)

    # 2. Optional downscale/upscale for soft pixelization
    if PIXELATE_SIZE > 1:
        small = cv2.resize(smooth, (width//PIXELATE_SIZE, height//PIXELATE_SIZE), interpolation=cv2.INTER_LINEAR)
        smooth = cv2.resize(small, (width, height), interpolation=cv2.INTER_NEAREST)

    # 3. Color quantization (soft anime palette)
    cartoon_colors = quantize_kmeans(smooth, k=K_COLORS)

    # 4. Edge detection on grayscale
    gray = cv2.cvtColor(input_frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, EDGE_THRESHOLD, EDGE_THRESHOLD*2)
    edges = cv2.dilate(edges, np.ones((2,2), np.uint8), iterations=1)  # thicken edges
    edges_inv = cv2.bitwise_not(edges)
    edges_inv_colored = cv2.cvtColor(edges_inv, cv2.COLOR_GRAY2BGR)

    # 5. Combine colors + soft edges
    cartoon_frame = cv2.bitwise_and(cartoon_colors, edges_inv_colored)

    out.write(cartoon_frame)

# ==========================
# CLEANUP
# ==========================
cap.release()
out.release()
cv2.destroyAllWindows()
print("Anime-style video generated:", OUTPUT_VIDEO)
