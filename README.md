Here is your updated README file with the Installation section at the top and the new functionality of Folder Creation added:

```markdown
# ❤️❤️ EXTRACTOR

## Installation

Ensure you have Python installed on your machine. The application requires the following libraries: `tkinter`, `rarfile`, `zipfile`, and `ttkthemes`. You can install the necessary libraries using the following commands:

```bash
pip install rarfile zipfile ttkthemes
```

### Download

You can download the application file from [here](<https://www.playbook.com/s/harjot15/k34gq92hgExnmZSWxMKCnQUF?assetToken=5kcZsS42bYubmj89Hr4kuX17>).

## Features

### Archive Extractor, File Mover, and Folder Renamer

This application provides a GUI for three main operations: extracting archives, moving files and deleting subdirectories, and renaming folders.

#### Usage

1. **Archive Extraction**:
   - Select the source folder containing the archives and the destination folder where the archives will be extracted.
   - Click on "Start Extraction".

```bash
# Snippet to run the extraction function
python script_name.py --extract <source_folder> <destination_folder>
```

2. **File Moving and Subdirectory Deletion**:
   - Select the source folder from where files will be moved and subdirectories will be deleted.
   - Click on "Start Moving and Deleting".

```bash
# Snippet to run the move and delete function
python script_name.py --move-and-delete <source_folder>
```

3. **Folder Renaming**:
   - Select the source folder containing the folders to be renamed.
   - Click on "Start Renaming".

```bash
# Snippet to run the renaming function
python script_name.py --rename <source_folder>
```

### Folder Creation

This feature allows you to create a hierarchy of folders in a specified destination folder based on a JSON structure.

#### Usage

1. **Folder Creation**:
   - Select the destination folder where the folders will be created.
   - Specify the folder structure in JSON format in the designated text area.
   - Click on "Create Folders".

```bash
# Snippet to run the folder creation function
python script_name.py --create-folders <destination_folder> <folder_structure.json>
```

Replace `script_name.py` with the name of your script file, and `<source_folder>`, `<destination_folder>` with the paths to your folders. `<folder_structure.json>` is the path to a JSON file containing your folder structure.
```

In the Folder Creation section, I've added a new snippet for running the folder creation function from the command line, assuming that you might have a corresponding command-line interface for this function. Replace `<folder_structure.json>` with the path to a JSON file containing your folder structure, if applicable. If not, feel free to remove or modify this snippet to match your application's actual functionality.
