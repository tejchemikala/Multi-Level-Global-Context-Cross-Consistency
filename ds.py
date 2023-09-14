import os
import shutil

# Define the source folder containing the files to be extracted
source_folder = "data/busi/images/benign"

# Define the two destination folders
folder1 = "images"
folder2 = "masks"

# Create the destination folders if they don't exist
os.makedirs(folder1, exist_ok=True)
os.makedirs(folder2, exist_ok=True)

# Get a list of files in the source folder
files_to_extract = os.listdir(source_folder)


# Iterate through the files and extract them alternatively
for file_name in files_to_extract:
    source_file = os.path.join(source_folder, file_name)

    # Check if the file name contains the word "mask"
    if "mask" in file_name.lower():
        destination_folder = folder2
    else:
        destination_folder = folder1

    # Extract the file into the appropriate destination folder
    shutil.copy(source_file, destination_folder)

print("Files have been alternately extracted into two folders.")
