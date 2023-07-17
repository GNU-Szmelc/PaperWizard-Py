import os
import subprocess
import sys

def fix_images():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    tmp_directory = os.path.join(script_directory, "tmp")
    fixed_directory = os.path.join(script_directory, "fixed")

    # Create the "fixed" directory if it doesn't exist
    os.makedirs(fixed_directory, exist_ok=True)

    # Change the current directory to the "tmp" directory
    os.chdir(tmp_directory)

    # Loop through all folders in the "tmp" directory
    for folder in os.listdir("."):
        if os.path.isdir(folder):
            # Check if the folder contains PNG files
            png_files = [f for f in os.listdir(folder) if f.endswith(".png")]
            if png_files:
                # Create a corresponding folder inside the "fixed" directory
                fixed_folder = os.path.join(fixed_directory, folder)
                os.makedirs(fixed_folder, exist_ok=True)

                # Loop through all PNG files in the folder
                for file in png_files:
                    # Construct the input and output file paths
                    input_file = os.path.join(folder, file)
                    output_file = os.path.join(fixed_folder, file)

                    if sys.platform.startswith('win'):
                        # Windows-specific command
                        subprocess.run(["magick", "convert", input_file, "-deskew", "40%", output_file])
                    elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
                        # Linux and macOS command
                        subprocess.run(["convert", input_file, "-deskew", "40%", output_file])
                    else:
                        print(f"Unsupported platform: {sys.platform}")
                        continue

                    # Print the status message
                    #print(f"Fixed {input_file} -> {output_file}")

# Call the function to fix the images
fix_images()
