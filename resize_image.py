#これはダウンロードフォルダ内のものに対し有効です
from PIL import Image
import os

# Download Folder Path
download_folder = "/Users/sivtheng/Downloads"

# Have the user input the image file name
input_file = input("Enter the file name of the image you want to resize (example: image.jpg): ")

# Create a complete file path
input_path = os.path.join(download_folder, input_file)

# Check image existence
if os.path.isfile(input_path):
    print(f"{input_file} is located in the download folder.")
    
    try:
        # Opening an image
        img = Image.open(input_path)

        # View original size
        original_size = img.size
        print(f"The size of this image is {original_size[0]} x {original_size[1]} pixels.")

        # Ask the user to input the new size
        width = int(input("Enter the new width (in pixels) : "))
        height = int(input("Enter the new height (in pixels) : "))

        # Resize
        img = img.resize((width, height), Image.LANCZOS)

        base_name, ext = os.path.splitext(input_file)
        output_file = f"{base_name}_resize{ext}"
        output_path = os.path.join(download_folder, output_file)
        img.save(output_path)

        # Show resized size
        new_size = img.size
        print(f"{input_file} could be resized without any problems.")
        print(f"The current size is {new_size[0]} x {new_size[1]} pixels.")
        print(f"The resized image has been saved : {output_path}")

    except Exception as e:
        print(f"An error occurred while resizing : {e}")

else:
    print(f"file not found : {input_path}")