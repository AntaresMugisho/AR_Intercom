# -*- This python file uses the following encoding : utf-8 -*-

import sys
import os
import socket
import sqlite3

from PySide6.QtWidgets import QLayout
from PySide6.QtGui import QPixmap, QPainter, QPainterPath
from PySide6.QtCore import Qt


def get_home_directory():
    """"
    Returns user's home directory for Windows, macOS or Linux
    """
    if sys.platform == "win32":
        home = os.environ["USERPROFILE"]
    else:
        home = os.environ["HOME"]

    return home

def get_storage_path():
    return "storage"


def create_media_folders():
    """
    Create folders in the user's home directory that will contain files sent through the app
    """
    home_directory = get_home_directory()
    folders = ["Audios", "Documents", "Images", "Videos", "Voices"]

    for folder in folders:
        path = os.path.join(home_directory, "AR_Intercom", "Media", folder)
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except Exception as e:
                print(f"Failed to create media files : {e}")


def create_databases():
    """
    Create databases and tables if they not exists
    """
    db_path = os.path.join(get_storage_path(), "database.db")

    create_users_table = """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            uuid VARCHAR,
            host_address VARCHAR,
            host_name VARCHAR,
            user_name VARCHAR,
            email VARCHAR,
            phone VARCHAR,
            user_status VARCHAR,
            password VARCHAR,
            image_path VARCHAR DEFAULT('default.png'),
            department VARCHAR,
            role VARCHAR,
            created_at TIMESTAMP,
            updated_at TIMESTAMP,
            deleted_at TIMESTAMP
    )"""

    create_messages_table = """
        CREATE TABLE IF NOT EXISTS messages(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender_id INTEGER,
            receiver_id INTEGER,
            kind VARCHAR,
            body TEXT,
            received BOOLEAN,
            created_at TIMESTAMP, 
            updated_at TIMESTAMP,
            deleted_at TIMESTAMP
    )"""

    with sqlite3.connect(db_path) as connection:
        connection.execute(create_users_table)
        connection.execute(create_messages_table)


def create_rounded_image(image_path, width, height=None, radius=None):
    """
    Create a rounded pixmap from an image with the specified size
    """
    if height is None:
        height = width

    pixmap = QPixmap(image_path).scaled(width, height, Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                                        Qt.TransformationMode.SmoothTransformation)
    rounded_pixmap = QPixmap(width, height)
    rounded_pixmap.fill(Qt.GlobalColor.transparent)

    painter = QPainter(rounded_pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)

    path = QPainterPath()

    if radius is not None:
        path.addRoundedRect(0, 0, width, height, radius, radius)
    else:
        path.addRoundedRect(0, 0, width, height, width/2, height/2)

    painter.setClipPath(path)
    painter.drawPixmap(0, 0, pixmap)

    return rounded_pixmap


def clear_layout(layout: QLayout, start: int = 0, end: int = 1):
    """
    Remove widgets from a layout
    """
    # Remove old list
    count = layout.count()
    for i in reversed(range(start, count - end)):
        item = layout.itemAt(i)
        widget = item.widget()

        if widget:
            widget.setParent(None)
        else:
            print("ERR in utils : No widget to remove")
            clear_layout(item.layout())


def get_private_ip():
    """
    Returns the local IP address
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(("8.8.8.8", 80))
        ip_address = sock.getsockname()[0]
        sock.close()
        return ip_address
    except OSError:
        return "127.0.0.1"


if __name__ == "__main__":
    create_databases()