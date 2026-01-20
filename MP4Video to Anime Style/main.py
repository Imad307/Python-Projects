import os
from stylization import load_model, cartoonize_video

# User configuration
STYLE = "paprika"  # change to "hayao" or "face_paint_512_v2"
INPUT_FOLDER = "input_videos"
OUTPUT_FOLDER = "output_videos"

# Load model once
model = load_model(STYLE)

# Process all videos in input folder
for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith((".mp4", ".mov", ".avi")):
        input_path = os.path.join(INPUT_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, f"cartoon_{filename}")
        print(f"Cartoonizing {filename} ...")
        cartoonize_video(input_path, output_path, model)

print("All videos processed!")
