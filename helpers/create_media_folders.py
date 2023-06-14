# -*- This python file uses the following encoding : utf-8 -*-

import sys
import os


def create_media_folders():
    """
    Create folders in the user's home directory that will contain files sent through the app
    """
    if sys.platform == "win32":
        home = os.environ["USERPROFILE"]
    else:
        home = os.environ["HOME"]

    folders = ["Audios", "Documents", "Images", "Videos", "Voices"]
    for folder in folders:
        path = f"{home}/AR Intercom/Media/{folder}"
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except Exception as e:
                print(f"Failed to create media files : {e}")