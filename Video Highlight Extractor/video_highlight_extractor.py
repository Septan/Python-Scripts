import os
import cv2
import warnings
from scenedetect import VideoManager, SceneManager
from scenedetect.detectors import ContentDetector
from tqdm import tqdm

# Suppress the deprecation warning
warnings.filterwarnings("ignore", message="VideoManager is deprecated and will be removed.")

def extract_highlights(input_video_path, output_folder):
    # Create a video manager
    video_manager = VideoManager([input_video_path])
    
    # Create a scene manager and add the ContentDetector
    scene_manager = SceneManager()
    scene_manager.add_detector(ContentDetector())
    
    # Set the video manager options
    video_manager.set_downscale_factor()
    
    # Start the video manager
    video_manager.start()
    
    # Perform content-aware scene detection
    scene_manager.detect_scenes(frame_source=video_manager)
    
    # Get the list of detected scenes
    scene_list = scene_manager.get_scene_list()
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Extract and save the highlight clips with audio
    extracted_scenes = []
    for i, scene in enumerate(tqdm(scene_list, desc="Extracting Scenes")):
        start_time = scene[0].get_timecode()
        end_time = scene[1].get_timecode()
        input_filename = os.path.basename(input_video_path)
        scene_name = f"{os.path.splitext(input_filename)[0]}_highlight_{i + 1}.mp4"
        output_path = os.path.join(output_folder, scene_name)
        
        # Check if the output file already exists
        if not os.path.exists(output_path):
            print(f"Extracting Scene {i + 1}: Start Time = {start_time}, End Time = {end_time}")
            
            # Use ffmpeg to extract the scene as a separate video with audio
            cmd = (
                f"ffmpeg -i {input_video_path} -ss {start_time} -to {end_time} -c:v copy -c:a aac -strict experimental {output_path}"
            )
            
            os.system(cmd)
            
            extracted_scenes.append((start_time, end_time))
    
    return extracted_scenes

if __name__ == "__main__":
    input_folder = input("Enter the folder path where the videos are located: ")
    output_folder = os.path.join(input_folder, "highlight_clips")  # Modify this line
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Process each video file in the input folder
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".mp4"):
                input_video = os.path.join(root, file)
                extracted_scenes = extract_highlights(input_video, output_folder)
                print(f"Extracted highlight clips for {file}:")
                for i, (start_time, end_time) in enumerate(extracted_scenes):
                    input_filename = os.path.basename(input_video)
                    scene_name = f"{os.path.splitext(input_filename)[0]}_highlight_{i + 1}.mp4"
                    print(f"Clip {i + 1}: File Name = {scene_name}, Start Time = {start_time}, End Time = {end_time}")