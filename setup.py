# -*- coding:utf-8 -*-

# ======================================= BUILD THE WINDOWS .EXE FILE ==================================================

from cx_Freeze import setup, Executable

files = ['resources/popup.ico', 'resources/popup.png', 'build/plyer/']

target = Executable(
      script="main.py",
      base="Console",
      icon="popup.ico")

setup(name="AR Intercom",
      version="0.1",
      description="AR Intercom",
      author="Antares",
      executables=[target]
      )
