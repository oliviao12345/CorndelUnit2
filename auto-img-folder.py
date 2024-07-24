import os

def create_image_folder():
    while True:
        user_decision = input("Do you want to create an image folder for storing images? (yes/no): ")
        if user_decision.lower() == "yes":
            print("Image folder has been created. Please Upload Your Images")
            if not os.path.exists("image_folder"):
                os.makedirs("image_folder")
            break
        elif user_decision.lower() == "no":
            print("Image folder has NOT been created.")
            break
        else:
            print("Please enter 'yes' or 'no'")

if __name__ == "__main__":
    create_image_folder()
