# Project README Generator

This Python script is designed to automate the process of creating a README file for your project. It allows you to add sections, content, and images to your README file interactively.

## Features

1. **Interactive README creation**: The script prompts you to enter the title of your project, the number of sections you want in the README, and the title and content for each section.

2. **Image folder creation**: The script offers you the option to create an image folder for storing images that will be linked in the README file.

3. **Image linking**: For each section, you can specify the number of images you want to add. You will be prompted to enter the path for each image and the alt text for the image. The images will be displayed in the README under the relevant sections.

## How to Use

1. Run the script in your terminal with the command `python <script_name>.py`, replacing `<script_name>` with the name of this script.

2. Follow the prompts to enter information about your project and the sections you want in your README.

3. If you choose to create an image folder, ensure that you upload your images to the `image_folder` directory created by the script **before** pasting the image name into the terminal.

4. For each image you want to add to a section, enter the path to the image (e.g. Example.png) (relative to the `image_folder` directory) and the alt text for the image.

5. Once you've entered all the information, the script will create a `README.md` file in the same directory.

## Note

- The script overwrites the `README.md` file each time it's run. If you have an existing `README.md` file in the same directory, make sure to back it up before running the script.

- The script does not check whether the image paths you enter are valid. Make sure to enter the correct paths to avoid broken image links in your README.

- The script does not upload images to the `image_folder` directory. You need to do this manually.

## Requirements

- Python 3.6 or higher

## Limitations

- The script does not support adding links, code blocks, or other special formatting to the README. It's designed for simple README files with text and images. For more complex README files, you may need to manually edit the file after it's generated.

## Future Improvements

- Add support for adding links, code blocks, and other special formatting to the README.
- Add error checking for image paths.
- Add an option to append to an existing README instead of overwriting it.
