import os


def create_image_folder():
    user_decision = input("Do you want to create an image folder for storing images? (yes/no): ")
    if user_decision.lower() == "yes":
        if not os.path.exists("image_folder"):
            os.makedirs("image_folder")


def create_project_readme():
    project_title = input("Enter the title of your project: ")
    create_image_folder()
    print("Image folder has been created. Please Upload Your Images")
    readme_text = f"# {project_title}\n\n"
    number_of_sections = int(input("How many sections do you want in the README?: "))

    for _ in range(number_of_sections):
        section_title = input("Enter the title of the section: ")
        print(f"### {section_title}")
        section_content = input(f"Enter content for the {section_title} section: ")
        readme_text += f"## {section_title}\n{section_content}\n"

        number_of_images = int(input(f"How many images do you want to add to the {section_title} section?: "))

        for image_index in range(number_of_images):
            image_path_from_user = input(
                f"Enter the path for image {image_index + 1} to be linked in the {section_title} section (e.g example.png) - Ensure image(s) have been uploaded to the image_folder: ")
            image_name = os.path.basename(image_path_from_user)
            readme_image_path = "image_folder/" + image_name
            image_alt_text = input(f"Enter alt text for image {image_index + 1}: ")
            readme_img_add = f"![{image_alt_text}]({readme_image_path})\n"  # Initialize the variable with an empty string

            readme_text += readme_img_add

            with open("README.md", "w") as readme_file:
                readme_file.write(readme_text)

    print("README.md file created successfully!")


if __name__ == "__main__":
    create_project_readme()
