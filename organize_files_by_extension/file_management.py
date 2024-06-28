import os
import shutil

def organize_files_by_extension(directory):
    """
    Organizes files in the given directory by their extensions.

    :param directory: Path to the directory to organize.
    """
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Ignore directories
        if os.path.isdir(os.path.join(directory, filename)):
            continue
        
        # Extract file extension
        ext = filename.split('.')[-1]
        ext_dir = os.path.join(directory, ext)
        
        # Create a directory for the extension if it doesn't exist
        os.makedirs(ext_dir, exist_ok=True)
        
        # Construct full file paths
        src_path = os.path.join(directory, filename)
        dest_path = os.path.join(ext_dir, filename)
        
        # Move file to the new directory
        shutil.move(src_path, dest_path)
        print(f'Moved {filename} to {ext_dir}')

# Example usage
organize_files_by_extension('/path/to/your/directory')