 To bundle your Python script into an executable file with an icon, you can use the `pyinstaller` tool. First, you would need to install `pyinstaller` using pip. Open your command prompt and run the following command:

```bash
pip install pyinstaller
```

Once `pyinstaller` is installed, you can use it to bundle your script into an executable. Place your icon file (e.g., `icon.ico`) in the same directory as your script file (e.g., `script.py`). Then, navigate to the directory containing your script and icon in the command prompt, and run the following command:

```bash
pyinstaller --onefile --windowed --icon=icon.ico script.py
```

Here's a breakdown of the command:

- `--onefile`: Creates a single executable file.
- `--windowed`: Indicates that your script is a GUI application. This option will ensure that no console window is displayed when running your executable.
- `--icon=icon.ico`: Specifies the icon file to use for the executable.

After running the command, `pyinstaller` will create a `dist` directory containing the bundled executable file (`script.exe`). The icon specified by the `--icon` option will be used as the icon for the executable file.