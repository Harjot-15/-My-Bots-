# ❤️ Archive Extractor, File Mover, Folder Renamer, and Folder Creator Tool

## Overview
This tool is designed to streamline file management tasks. It provides functionalities for extracting archives, moving and deleting files, renaming folders, and creating folder structures based on JSON configuration.

---

## Section 1: Top Control Buttons

`Refresh Button:`
```markdown
- **Function:** Clears all input fields, resets progress bars to 0%, and reinstates the default JSON folder structure in the text field.
- **Background Color:** Green (#00df1f)
```

`Close Button:`
```markdown
- **Function:** Closes the application window.
- **Background Color:** Red (#e00000)
```

---

## Section 2: Archive Extraction

`Source Folder Input:`
```markdown
- **Purpose:** To specify the directory from which archives will be extracted.
- **Interaction:** A path can be entered manually or selected by clicking the "Browse" button.
```

`Destination Folder Input:`
```markdown
- **Purpose:** To define the destination path for the extracted files.
- **Interaction:** A path can be entered manually or chosen using the "Browse" button.
```

`Start Extraction Button:`
```markdown
- **Function:** Initiates the extraction of files from archives found in the source directory into the destination directory.
- **Background Color:** Light blue (#7af7ff)
```

---

## Section 3: File Moving and Deleting

`Source Folder for Moving Input:`
```markdown
- **Purpose:** To indicate the directory from where files should be moved and subdirectories be deleted.
- **Interaction:** A path can be entered manually or picked by the "Browse" button.
```

`Start Moving and Deleting Button:`
```markdown
- **Function:** Begins the process of moving files from subdirectories to the source folder and removes the now-empty subdirectories.
- **Background Color:** Light blue (#7af7ff)
```

---

## Section 4: Folder Renaming

`Source Folder for Renaming Input:`
```markdown
- **Purpose:** To input the directory containing folders to be renamed.
- **Interaction:** A path can be typed in or selected through the "Browse" button.
```

`Start Renaming Button:`
```markdown
- **Function:** Commences the renaming of folders in the specified source directory, formatting names to a readable form.
- **Background Color:** Light blue (#7af7ff)
```

---

## Section 5: Folder Structure Creation

`Destination Folder for Creation Input:`
```markdown
- **Purpose:** To enter the directory path where the new folder structure will be created.
- **Interaction:** Paths can be manually inputted or set via the "Browse" button.
```

`Folder Structure (in JSON format) Text Field:`
```markdown
- **Purpose:** Allows users to define the folder structure they wish to create in JSON format.
- **Interaction:** Users can manually enter the JSON configuration or modify the existing template.
```

`Create Folders Button:`
```markdown
- **Function:** Uses the JSON configuration from the text field to create the folder structure in the specified destination directory.
- **Background Color:** Light blue (#7af7ff)
```

---

## Progress Bars
```markdown
- **Each section that involves processing (extraction, moving, renaming, creation) has an associated progress bar. This bar visually indicates the progress of the current operation.
```

*Note: This README does not cover the underlying code or software dependencies required to run this tool.*
```
