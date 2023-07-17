import os
import img2pdf
import sys

script_directory = os.path.dirname(os.path.abspath(__file__))
fixed_directory = os.path.join(script_directory, "fixed")
output_directory = os.path.join(script_directory, "output")

# Create the "output" directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Change the current directory to the "fixed" directory
os.chdir(fixed_directory)

# Iterate over all folders in the "fixed" directory
for folder in os.listdir("."):
    if os.path.isdir(folder):
        # Create a corresponding PDF file name
        pdf_file = os.path.join(output_directory, f"{folder}.pdf")

        # Get the path of PNG files inside the folder
        image_paths = [os.path.join(folder, file) for file in os.listdir(folder) if file.endswith(".png")]

        # Sort the image paths to preserve the order
        image_paths.sort()

        if sys.platform.startswith('win'):
            # Windows-specific code
            with open(pdf_file, "wb") as output:
                img2pdf.convert(image_paths, outputstream=output)
        elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
            # Linux and macOS code
            pdf_bytes = img2pdf.convert(image_paths)
            with open(pdf_file, "wb") as output:
                output.write(pdf_bytes)
        else:
            print(f"Unsupported platform: {sys.platform}")
            continue

        print(f"PDF conversion complete for folder {folder}!")

print("All PDF conversions complete!")
