# -*- coding:utf-8 -*-

# ======================================= BUILD THE WINDOWS .EXE FILE ==================================================

from cx_Freeze import setup, Executable

files = ['popup.ico', 'popup.png', 'plyer/']

target = Executable(
      script="main.py",
      base="Console",
      icon="popup.ico")

setup(name="AR Intercom",
      version="1.0.0",
      description="AR Intercom",
      author="Antares",
      executables=[target]
      )
