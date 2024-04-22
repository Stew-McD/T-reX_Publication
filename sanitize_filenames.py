import os
from pathvalidate import sanitize_filename, sanitize_filepath

def rename_files_in_directory(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            # Sanitize the filename using pathvalidate
            sanitized = sanitize_filename(filename, platform="universal")
            if sanitized != filename:
                old_filepath = os.path.join(dirpath, filename)
                new_filepath = os.path.join(dirpath, sanitized)
                # Rename the file
                os.rename(old_filepath, new_filepath)
                print(f'Renamed: {old_filepath} \n\t\t-> {new_filepath}')

# Specify the root directory to start from
root_directory = "."
rename_files_in_directory(root_directory)
