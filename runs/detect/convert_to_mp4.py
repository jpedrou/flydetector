import os
from moviepy import VideoFileClip

input_folder = "runs/detect/predict"
output_folder = "videos"
os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.lower().endswith(".avi"):
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, f"predicted{file.replace(".avi", ".mp4")}")
        clip = VideoFileClip(input_path)
        clip.write_videofile(output_path, codec="libx264")
        print(f"{file} convertido para MP4")