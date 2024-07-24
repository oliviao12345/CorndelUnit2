import os


def create_project_readme():
    valid_image_formats = [".png", ".jpeg", ".jpg", ".svc", ".gif"]
    project_title = input("Enter the title of your project: ")

    readme_text = f"# {project_title}\n\n"
    while True:
        try:
            number_of_sections = int(input("How many sections do you want in the README?: "))
            break
        except ValueError:
            print("That's not a valid number. Please enter an integer.")

    for _ in range(number_of_sections):
        section_title = input("Enter the title of the section: ")
        print(f"### {section_title}")
        section_content = input(f"Enter content for the {section_title} section: ")
        readme_text += f"## {section_title}\n{section_content}\n"

        number_of_images = None
        while True:
            try:
                number_of_images = int(input(f"How many images do you want to add to the {section_title} section?: "))
                break
            except ValueError:
                print("That's not a valid number. Please enter an integer.")

        if number_of_images is not None:
            for image_index in range(number_of_images):
                image_found = False
                image_path_from_user = None
                while not image_found:
                    image_path_from_user = input(
                        f"Enter the path for image {image_index + 1} to be linked in the {section_title} section "
                        f"(e.g., image_folder/example.png) - Ensure image(s) have been uploaded to the image_folder: ")

                    if os.path.isfile(image_path_from_user):
                        print("Image has been found in the folder and added to the README.")
                        image_found = True
                    else:
                        print("Image has not been found in the folder. Please check and try again.")

                    if any(image_path_from_user.endswith(format) for format in valid_image_formats):
                        print("Image format is valid.")
                    else:
                        print("Invalid image format. Accepted formats: .png, .jpeg, .jpg, .svc, .gif")

                image_alt_text = input(f"Enter alt text for image {image_index + 1}: ")
                readme_img_add = f"<br>![{image_alt_text}]({image_path_from_user})\n"  # Initialize the variable with an empty string
                readme_text += readme_img_add

    with open("README.md", "w") as readme_file:
        readme_file.write(readme_text)

    print("README.md file created successfully!")


if __name__ == "__main__":
    create_project_readme()
