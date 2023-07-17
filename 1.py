import os
import sys
from datetime import datetime

# Directory path containing PDF files
directory_path = "feed"
print("") 
print("Files in 'feed' folder:")
file_list = os.listdir(directory_path)
for file in file_list:
    print(file)

# Get the path of the 'tmp' directory in the same folder as the code
current_directory = os.path.dirname(os.path.abspath(__file__))
tmp_directory = os.path.join(current_directory, 'tmp')

print(" ")

# Create the 'tmp' directory if it doesn't exist
os.makedirs(tmp_directory, exist_ok=True)

# Get a list of all PDF files in the directory
pdf_files = [f for f in os.listdir(directory_path) if f.endswith(".pdf")]

# Check if there are any PDF files in the directory
if not pdf_files:
    print("No PDF files found in the directory!")
    sys.exit(1)

# Process each PDF file
for pdf_file in pdf_files:
    # Check if the PDF file exists
    pdf_path = os.path.join(directory_path, pdf_file)
    if not os.path.isfile(pdf_path):
        print(f"PDF file not found: {pdf_file}")
        continue
    print(f"Processing file: {pdf_file}")

    # Create a new folder inside the 'tmp' directory with the same name as the PDF file (without the extension)
    folder_name = os.path.splitext(pdf_file)[0]
    folder_path = os.path.join(tmp_directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Convert each page of the PDF to PNG
    if sys.platform.startswith("win"):
        # Windows-specific command
        command = ["pdftoppm", "-png", pdf_path, os.path.join(folder_path, "page")]
    else:
        # Linux-specific command
        command = ["pdftoppm", "-png", pdf_path, os.path.join(folder_path, "page")]

    # Execute the command
    result = os.system(" ".join(command))

    if result != 0:
        print(f"Error converting PDF file: {pdf_file}")
    else:
        print(f"Conversion complete! PNG images saved in folder: {folder_name}")
