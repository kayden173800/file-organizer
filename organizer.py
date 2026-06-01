from pathlib import Path
import shutil

# path to Downloads folder
DOWNLOADS_PATH = Path.home() / "downloads"

# categories and file extensions
FILE_CATEGORIES = {
    "images": [".png", "jpg", "jpeg", "gif"],
    "PDFs": ["pdf"],
    "Videos":[".mp4", ".mov"],
    "Documents": [".docx", "txt"],
    "zip_Files": [".zip", ".rar"]
}

def get_category(extension):
    """
    Return matching folder catergory
    based on file extension
    """
    
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    return None

def organize_downloads():
    """
    organize files in Downloads folder.
    """

    for file in DOWNLOADS_PATH.iterdir():

        # skip folders
        if file.is_dir():
            continue

        # get file extension 
        extension = file.suffix.lower()

        # Find matching category
        category = get_category(extension)

        if category:
            # create category folder
            folder_path = DOWNLOADS_PATH / category
            folder_path.mkdir(exist_ok=True)

            # Destination path
            destination = folder_path / file.name

            try:
                shutil.move(str(file), str(destination))
                print(f"moved: {file.name} ==> {category}")
            except Exception as error:
                print(f"Error moving {file.name}: {error}")
if __name__ == "__main__":
    organize_downloads()