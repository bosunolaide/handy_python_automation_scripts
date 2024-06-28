import os
import subprocess

def optimize_video(input_path, output_path, resolution="1280x720", bitrate="1M"):
    """
    Optimize a video file using ffmpeg.

    :param input_path: Path to the input video file.
    :param output_path: Path to save the optimized video file.
    :param resolution: Resolution for the output video (e.g., '1280x720').
    :param bitrate: Bitrate for the output video (e.g., '1M' for 1 Mbps).
    """
    try:
        print(f"Optimizing {input_path}...")

        # Construct the ffmpeg command
        command = [
            'ffmpeg',
            '-i', input_path,
            '-vf', f'scale={resolution}',
            '-b:v', bitrate,
            '-c:a', 'copy',
            output_path
        ]

        # Run the command
        subprocess.run(command, check=True)
        print(f"Saved optimized video to {output_path}")

    except subprocess.CalledProcessError as e:
        print(f"Error optimizing {input_path}: {e}")

def optimize_videos_in_directory(directory, output_directory, resolution="1280x720", bitrate="1M"):
    """
    Optimize all videos in the specified directory.

    :param directory: Directory containing videos to optimize.
    :param output_directory: Directory to save optimized videos.
    :param resolution: Resolution for the output videos (e.g., '1280x720').
    :param bitrate: Bitrate for the output videos (e.g., '1M' for 1 Mbps).
    """
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        input_path = os.path.join(directory, filename)
        output_path = os.path.join(output_directory, filename)

        # Check if the file is a video
        if filename.lower().endswith(('mp4', 'mkv', 'mov', 'avi', 'flv', 'wmv', 'webm')):
            optimize_video(input_path, output_path, resolution, bitrate)

# Example usage
if __name__ == "__main__":
    input_dir = "input_videos"  # Replace with your input directory
    output_dir = "optimized_videos"  # Replace with your output directory
    video_resolution = "1280x720"  # Replace with desired resolution (e.g., '1920x1080')
    video_bitrate = "1M"  # Replace with desired bitrate (e.g., '500K' for 500 kbps)

    optimize_videos_in_directory(input_dir, output_dir, resolution=video_resolution, bitrate=video_bitrate)