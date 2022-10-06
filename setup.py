# -*- This python file uses the following encoding : coding:utf-8 -*-

# ======================================= BUILD THE WINDOWS .EXE FILE ==================================================

from cx_Freeze import setup, Executable

setup(name="AR Intercom",
      version="1.0",
      description="AR Intercom",
      executables=[Executable("main.py")])

# NO TRYING IN THIS
# ===================================================== END ============================================================