# -*- This python file uses the following encoding : utf-8 -*-


import sys
import os


def get_home_directory():
    """"
    Returns user's home directory for Windows, macOS or Linux
    """
    if sys.platform == "win32":
        home = os.environ["USERPROFILE"]
    else:
        home = os.environ["HOME"]

    return home


def create_media_folders():
    """
    Create folders in the user's home directory that will contain files sent through the app
    """
    home_directory = get_home_directory()
    folders = ["Audios", "Documents", "Images", "Videos", "Voices"]

    for folder in folders:
        path = f"{home_directory}/AR Intercom/Media/{folder}"
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except Exception as e:
                print(f"Failed to create media files : {e}")