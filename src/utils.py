import os


def ensure_directory_exists(directory_path):
    """
    Ensures the specified directory exists. Creates it if it doesn't exist.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def get_file_name_without_extension(file_path):
    """
    Extracts the file name without its extension from a given path.
    """
    return os.path.splitext(os.path.basename(file_path))[0]


def is_image_file(file_name):
    """
    Checks if a given file is an image based on its extension.
    """
    valid_extensions = (".jpg", ".jpeg", ".png")
    return file_name.lower().endswith(valid_extensions)