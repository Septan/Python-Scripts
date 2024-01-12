import os
import cv2
import math
from tqdm import tqdm
import numpy as np
from skimage.metrics import structural_similarity as ssim
import logging

# Set up logging
logging.basicConfig(filename='extraction_log.log', level=logging.INFO)

# Define configurable parameters
ssim_threshold = 0.9
psnr_threshold = 20.0
max_photos = 200  # Expanded the limit

# Ask the user for the video file path
video_file = input("Enter the path of the video file: ")
output_dir = 'output_images'
blurry_dir = 'blurry_images'
os.makedirs(output_dir, exist_ok=True)
os.makedirs(blurry_dir, exist_ok=True)

# Open the video file
cap = cv2.VideoCapture(video_file)

# Get the video's frame rate and total frames
frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Calculate the frame interval to capture approximately max_photos frames
frame_interval = math.ceil(total_frames / max_photos)

# Initialize variables
frame_count = 0
photos_count = 0

# Initialize the progress bar
progress_bar = tqdm(total=max_photos, desc="Extracting Photos")

# Initialize variables for the first frame
prev_frame = None

while True:
    try:
        # Read a frame from the video
        ret, frame = cap.read()

        # Break the loop if we have reached the end of the video
        if not ret:
            break

        # Increase frame counter
        frame_count += 1

        # Capture a frame at the defined frame interval
        if frame_count % frame_interval == 0:
            # Calculate SSIM and PSNR with the previous frame
            if prev_frame is not None:
                current_frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                prev_frame_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
                ssim_score = ssim(current_frame_gray, prev_frame_gray)
                psnr = cv2.PSNR(prev_frame, frame)
            else:
                ssim_score = 1.0  # Set an initial value for the first frame
                psnr = 0.0

            # Check if the frame meets the SSIM and PSNR thresholds
            if ssim_score >= ssim_threshold and psnr >= psnr_threshold:
                # Save the frame as an image in the output directory
                frame_filename = os.path.join(output_dir, f'frame_{frame_count:04d}.jpg')
                cv2.imwrite(frame_filename, frame)
                photos_count += 1
                progress_bar.update(1)
                progress_bar.set_postfix(photos=photos_count)
            else:
                # Save the frame as an image in the blurry directory
                frame_filename = os.path.join(blurry_dir, f'frame_{frame_count:04d}.jpg')
                cv2.imwrite(frame_filename, frame)

            # Update the previous frame
            prev_frame = frame.copy()

        # Break the loop if we've reached the maximum number of photos
        if photos_count >= max_photos:
            break
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        break

# Close the progress bar
progress_bar.close()

# Release the video capture object and close any open windows
cap.release()
cv2.destroyAllWindows()

# Log the information
logging.info(f"Extracted {photos_count} photos to {output_dir}")
logging.info(f"Extracted {frame_count - photos_count} blurry photos to {blurry_dir}")

print(f"Extracted {photos_count} photos to {output_dir}")
print(f"Extracted {frame_count - photos_count} blurry photos to {blurry_dir}")