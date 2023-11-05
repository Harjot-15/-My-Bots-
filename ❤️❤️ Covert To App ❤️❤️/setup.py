import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["os", "tkinter", "shutil", "zipfile", "rarfile", "ttkthemes"],  # List any required packages here
    "include_files": ["Rabab.ico"]  # Include your icon file
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use this for GUI applications

setup(
    name="Archive Extractor, File Mover, and Folder Renamer",
    version="0.1",
    description="Your description",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, icon="Rabab.ico")]
)
