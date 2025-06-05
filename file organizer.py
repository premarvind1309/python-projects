import os
import shutil

# Folder you want to organize
source_folder = input("Enter full path of folder to organize: ").strip()

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css", ".c", ".cpp"],
    "Others": []
}

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def get_category(file_ext):
    for category, extensions in file_types.items():
        if file_ext.lower() in extensions:
            return category
    return "Others"

def organize_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("❌ Invalid folder path.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            category = get_category(ext)
            category_folder = os.path.join(folder_path, category)
            create_folder(category_folder)

            # Move file
            shutil.move(file_path, os.path.join(category_folder, filename))
            print(f"Moved: {filename} ➜ {category}/")

    print("\n✅ Folder organized successfully!")

# Run the organizer
organize_folder(source_folder)
