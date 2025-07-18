"""
Challenge: Batch Rename Files in a Folder

Goal:
- Scan all files in a selected folder
- Rename them with a consistent pattern:
    e.g., "image_1.jpg", "image_2.jpg", ...
- Ask the user for:
    - A base name (e.g., "image")
    - A file extension to filter (e.g., ".jpg")
- Preview before renaming
- Optional: allow undo (save original names in a file)

Teaches: File iteration, string formatting, renaming, user input
"""
import os

def batch_rename(folder, base_name, extension):
    files = [f for f in os.listdir(folder) if f.lower().endswith(extension.lower())]
    files.sort() # this will not do much

    if not files:
        print("NO files found in dir")
        return
    
    for i, file in enumerate(files, start=1):
        new_name = f"{base_name}_{i}{extension}"
        print(f"{file} => {new_name}")
    confirm = input("Press (y) to confirm or (n) to reject").strip().lower()

    if confirm != 'y':
        print("Cancel")
        return
    
    for i, file in enumerate(files, start=1):
        src = os.path.join(folder, file)
        new_name = f"{base_name}_{i}{extension}"
        dest = os.path.join(folder, new_name)
        os.rename(src, dest)
    print(f"Renamed {len(files)} files successfully")

if __name__ == "__main__":
    folder = input("Enter folder path or learn blank for current folder: ").strip() or os.getcwd()

    if not os.path.isdir(folder):
        print("Invalid folder")
    else:
        base_name = input("Enter base name for files: ").strip()
        extension = input("Enter extension name for files: ").strip()

        batch_rename(folder, base_name, extension)
