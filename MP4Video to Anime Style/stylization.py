import torch
import cv2
import numpy as np
import os

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load AnimeGANv2 generator via Torch Hub
def load_model(style="paprika"):
    print(f"Loading AnimeGANv2 model for style: {style} ...")
    model = torch.hub.load(
        "bryandlee/animegan2-pytorch:main",
        "generator",
        pretrained=style
    ).to(device)
    model.eval()
    return model

def animegan2_cartoonize(model, frame):
    # Convert BGR to RGB
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    tensor = (
        torch.from_numpy(img).float().permute(2, 0, 1).unsqueeze(0) / 255.0
    ).to(device)

    with torch.no_grad():
        out_tensor = model(tensor)[0].permute(1, 2, 0).cpu().numpy()

    out_img = (out_tensor * 255).clip(0, 255).astype(np.uint8)
    return cv2.cvtColor(out_img, cv2.COLOR_RGB2BGR)

def cartoonize_video(input_path, output_path, model):
    cap = cv2.VideoCapture(input_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Processing {total_frames} frames...")

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cartoon_frame = animegan2_cartoonize(model, frame)
        out.write(cartoon_frame)
        frame_count += 1
        if frame_count % 10 == 0:
            print(f"Processed {frame_count}/{total_frames} frames")

    cap.release()
    out.release()
    print(f"Saved cartoon video to {output_path}")
