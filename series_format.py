#! /usr/bin/env python3
# Rename TV series episodes to S00E00 format
# Usage: python series_format.py /path/to/folder
# Trick: 
# 1. Move the script to the folder containing the video files
# 2. Run the script using the command above ( command: python3 series_format.py . )
# 3. All the video files in the folder will be renamed to S00E00 format
# 4. Done!
# This script will rename all the files in the folder to S00E00 format
# For example, "The.Big.Bang.Theory.S01E01.mp4" will be renamed to "S01E01.mp4"
# Author: Kyi Wong (github.com/NihaoKangkang)

import os
import re
import sys

def rename_videos(folder_path):
    # Use regular expressions to match the S00E00 format
    pattern = re.compile(r"S\d{2}E\d{2}")
    
    # Iterate through all the files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        # If current filename is a folder, ignore it
        if not os.path.isfile(file_path):
            continue

        # get file extension
        file_extension = os.path.splitext(filename)[1]
        
        # search for the pattern in the filename
        match = pattern.search(filename)
        if match:
            new_filename = match.group(0) + file_extension
            new_file_path = os.path.join(folder_path, new_filename)

            # rename the file
            os.rename(file_path, new_file_path)
            print(f"Rename: {filename} -> {new_filename}")
        else:
            print(f"Fail: {filename} (No matching format found)")

# Check if the folder path is provided as an argument
if len(sys.argv) < 2:
    print("Error: Please enter the folder path as the first parameter.")
    print("Usage: python script.py /path/to/folder")
else:
    folder_path = sys.argv[1]
    
    # Check if the provided path is a valid folder
    if not os.path.isdir(folder_path):
        print(f"Error: The provided path '{folder_path}' is not a valid folder.")
    else:
        rename_videos(folder_path)
