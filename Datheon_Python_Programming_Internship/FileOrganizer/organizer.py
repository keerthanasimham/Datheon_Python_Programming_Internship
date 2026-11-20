import os
import shutil

EXTENSIONS = {
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".zip": "Archives",
    ".rar": "Archives",
    ".py": "Code",
    ".java": "Code",
    ".html": "Code",
    ".css": "Code"
}

def organize_files(folder):
    if not os.path.isdir(folder):
        print("Invalid folder path!")
        return

    moved = 0
    skipped = 0
    errors = 0

    for entry in os.scandir(folder):
        if not entry.is_file():
            continue

        extension = os.path.splitext(entry.name)[1].lower()
        category = EXTENSIONS.get(extension, "Others")

        destination_folder = os.path.join(folder, category)
        os.makedirs(destination_folder, exist_ok=True)

        destination = os.path.join(destination_folder, entry.name)

        # Avoid overwriting files with the same name
        if os.path.exists(destination):
            skipped += 1
            print("Skipped duplicate:", entry.name)
            continue

        try:
            shutil.move(entry.path, destination)
            moved += 1
            print("Moved:", entry.name, "->", category)

        except PermissionError:
            errors += 1
            print("Permission denied:", entry.name)

        except OSError as error:
            errors += 1
            print("Error:", error)

    print("\n===== ORGANIZATION SUMMARY =====")
    print("Files moved:", moved)
    print("Files skipped:", skipped)
    print("Errors:", errors)
    print("Organization completed!")


print("===== AUTOMATED FILE ORGANIZER =====")

folder_path = input("Enter folder path to organize: ").strip().strip('"')

organize_files(folder_path)