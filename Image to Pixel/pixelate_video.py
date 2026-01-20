import cv2

INPUT_VIDEO = "Input.mp4"
OUTPUT_VIDEO = "output_pixel.mp4"
PIXEL_SIZE = 12

cap = cv2.VideoCapture(INPUT_VIDEO)

if not cap.isOpened():
    raise IOError("Error opening video file")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(OUTPUT_VIDEO, fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    small_w = max(1, width // PIXEL_SIZE)
    small_h = max(1, height // PIXEL_SIZE)

    temp = cv2.resize(frame, (small_w, small_h), interpolation=cv2.INTER_LINEAR)
    pixelated = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

    out.write(pixelated)

cap.release()
out.release()
cv2.destroyAllWindows()

print("Pixelated video saved:", OUTPUT_VIDEO)
