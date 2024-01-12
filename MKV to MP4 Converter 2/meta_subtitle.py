import os

# Ask the user to input the folder path
folder_path = input("Enter the folder path: ")

for filename in os.listdir(folder_path):
    if filename.endswith(".mkv"):
        input_file = os.path.join(folder_path, filename)
        output_file = os.path.join(folder_path, os.path.splitext(filename)[0] + ".mp4")
        
        # Extracting title from filename (removing extension)
        title = os.path.splitext(filename)[0]
        
        # FFmpeg command to copy video, audio, and subtitle streams, add metadata for title, audio, and subtitles
        command = f'ffmpeg -i "{input_file}" -c:v copy -c:a copy -c:s mov_text -metadata title="{title}" -metadata:s:a:0 language=eng -metadata:s:s:0 language=eng "{output_file}"'
        
        os.system(command)