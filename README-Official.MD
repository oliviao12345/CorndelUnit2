# Project README Generator

This Python script is designed to automate the process of creating a README file for your project. It allows you to add sections, content, and images to your README file interactively.

## Features

1. **Interactive README creation**: The script prompts you to enter the title of your project, the number of sections you want in the README, and the title and content for each section.

2. **Image folder creation**: The script offers you the option to create an image folder for storing images that will be linked in the README file.

3. **Image linking**: For each section, you can specify the number of images you want to add. You will be prompted to enter the path for each image and the alt text for the image. The images will be displayed in the README under the relevant sections.

## How to Use

### Step 1:

1. Run the auto-img-folder script in your terminal with the command `python auto-img-folder.py`.

2. Follow the prompts and decide whether you would like an image folder to be created.

3. If you choose to create an image folder, ensure that you upload your images to the `image_folder` directory created by the script **before** pasting the image name(s) into the terminal.


### Step 2: 

1. Run the auto-readme script in your terminal with the command `python auto-readme.py`.

2. Follow the prompts to enter information about your project and the sections you want in your README. 

3. For each image you want to add to a section, enter the relative path of the image (e.g. image_folder/example.png, image_folder/example.jpg etc.) and then any unique name for the alt text for each image.

4. Once you've entered all the information, the script will create a `README.md` file in the same directory.

## Note

- The script overwrites the `README.md` file each time it's run. If you have an existing `README.md` file in the same directory, make sure to back it up before running the script.

- The script does not upload images to the `image_folder` directory. You need to do this manually.

- Acceptable image formats are .png", ".jpeg", ".jpg", ".svc", ".gif"

## Requirements

- Python 3.6 or higher

## Limitations

- The script does not support adding links, code blocks, or other special formatting to the README. It's designed for simple README files with text and images. For more complex README files, you may need to manually edit the file after it's generated.

## Future Improvements

- Add support for adding links, code blocks, and other special formatting to the README.
- Add error checking for image paths.
- Add an option to append to an existing README instead of overwriting it.