### Video Frame Extraction Tool

This Python script is designed to extract frames from a video file based on Structural Similarity Index (SSIM) and Peak Signal-to-Noise Ratio (PSNR) thresholds. Blurry frames are saved separately from clear frames.

### Usage

1. **Install Dependencies:**
   ```bash
   pip install opencv-python tqdm scikit-image
   ```

1. **Run the Script:**
   ```bash
   python video_frame_extraction.py
   ```
   Follow the prompt the enter the path of the video file.

2. **Output:**
- Extracted frames meeting SSIM and PSNR thresholds: `output_images/`
- Extracted blurry frames: `blurry_images/`

### Configuration

You can configure the following parameters in the script:

- `ssim_threshold`: SSIM threshold for frame clarity (default: 0.9)
- `psnr_threshold`: PSNR threshold for frame clarity (default: 20.0)
- `max_photos`: Maximum number of frames to extract (default: 200)

### Logging

The script logs information to `extraction_log.log`.

### Dependencies

- OpenCV (cv2)
- TQDM (tqdm)
- scikit-image (scructural_similarity)