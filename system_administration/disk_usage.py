import shutil
import os
import platform

def check_disk_usage(threshold):
    """
    Checks the disk usage and alerts if free space is below the given threshold.

    :param threshold: The minimum free space percentage allowed before an alert is raised.
    """
    # Get disk usage statistics
    total, used, free = shutil.disk_usage('/')

    # Calculate percentage of free space
    free_percent = free / total * 100

    # Print the disk usage details
    print(f"Total: {total / (1024**3):.2f} GB")
    print(f"Used: {used / (1024**3):.2f} GB")
    print(f"Free: {free / (1024**3):.2f} GB ({free_percent:.2f}%)")

    # Check if free space is below the threshold
    if free_percent < threshold:
        print(f"Warning: Only {free_percent:.2f}% free space left!")
    else:
        print(f"Sufficient disk space available ({free_percent:.2f}% free).")

# Example usage
threshold = 20  # Set threshold for free space percentage
check_disk_usage(threshold)