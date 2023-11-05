import os
import zipfile
import rarfile
import tkinter as tk
from tkinter import ttk, filedialog
import shutil
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import json

def close_gui():
    root.destroy()

def refresh_gui():
    src_folder_var.set('')
    dest_folder_var.set('')
    progress_var.set(0)
    src_folder_var_renaming.set('')
    progress_var_moving.set(0)
    progress_var_renaming.set(0)
    dest_folder_var_create.set('')
    folder_names_text.delete("1.0", tk.END)
    folder_names_text.insert(tk.END, example_structure.strip())  # re-insert the example structure
    progress_var_create.set(0)


def count_files(src_folder):
    return sum([len(files) for subdir, dirs, files in os.walk(src_folder)])

def extract_files(src_folder, dest_folder, progress_var):
    file_count = count_files(src_folder)
    processed_files = 0
    for root_dir, dirs, files in os.walk(src_folder):
        for file in files:
            file_path = os.path.join(root_dir, file)
            new_folder_name = os.path.splitext(file)[0]
            new_folder_path = os.path.join(dest_folder, new_folder_name)
            os.makedirs(new_folder_path, exist_ok=True)
            if file.endswith('.zip'):
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(new_folder_path)
                    print(f'Extracted {file} to {new_folder_path}')
            elif file.endswith('.rar'):
                with rarfile.RarFile(file_path, 'r') as rar_ref:
                    rar_ref.extractall(new_folder_path)
                    print(f'Extracted {file} to {new_folder_path}')
            processed_files += 1
            progress_var.set(processed_files / file_count * 100)
            root.update_idletasks()

def count_dirs(src_folder):
    return sum([len(dirs) for subdir, dirs, files in os.walk(src_folder)])

def move_files_and_delete_subdirs(src_folder, progress_var):
    dir_count = count_dirs(src_folder)
    processed_dirs = 0
    for root_dir, dirs, files in os.walk(src_folder, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root_dir, dir)
            parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
            if os.path.basename(dir_path) == os.path.basename(parent_dir_path):
                for file in os.listdir(dir_path):
                    file_path = os.path.join(dir_path, file)
                    dest_path = os.path.join(parent_dir_path, file)
                    if not os.path.exists(dest_path):
                        shutil.move(file_path, dest_path)
                os.rmdir(dir_path)
            processed_dirs += 1
            progress_var.set(processed_dirs / dir_count * 100)
            root.update_idletasks()

def browse_src_folder_for_moving():
    src_folder = filedialog.askdirectory(title="Select Source Folder for Moving and Deleting")
    src_folder_var.set(src_folder)

def start_moving_and_deleting():
    src_folder = src_folder_var.get()
    move_files_and_delete_subdirs(src_folder, progress_var_moving)

def browse_src_folder():
    src_folder = filedialog.askdirectory(title="Select Source Folder")
    src_folder_var.set(src_folder)

def browse_dest_folder():
    dest_folder = filedialog.askdirectory(title="Select Destination Folder")
    dest_folder_var.set(dest_folder)

def start_extraction():
    src_folder = src_folder_var.get()
    dest_folder = dest_folder_var.get()
    extract_files(src_folder, dest_folder, progress_var)

def rename_folders(src_folder, progress_var):
    folder_count = len([entry for entry in os.listdir(src_folder) if os.path.isdir(os.path.join(src_folder, entry))])
    processed_folders = 0
    for entry in os.listdir(src_folder):
        entry_path = os.path.join(src_folder, entry)
        if os.path.isdir(entry_path):
            formatted_name = entry.replace('_', ' ').replace('-', ' ')
            formatted_name = ' '.join([word.capitalize() for word in formatted_name.split()])
            formatted_path = os.path.join(src_folder, formatted_name)
            os.rename(entry_path, formatted_path)
            processed_folders += 1
            progress_var.set(processed_folders / folder_count * 100)
            root.update_idletasks()

def browse_src_folder_for_renaming():
    src_folder = filedialog.askdirectory(title="Select Source Folder for Renaming")
    src_folder_var_renaming.set(src_folder)

def start_renaming():
    src_folder = src_folder_var_renaming.get()
    rename_folders(src_folder, progress_var_renaming)
    
# Define function to create folders
def create_folders(dest_folder, folder_structure, progress_var):
    folder_structure_dict = json.loads(folder_structure)
    total_folders = sum(1 + len(subfolders) for subfolders in folder_structure_dict.values())
    created_folders = 0
    for parent_folder, subfolders in folder_structure_dict.items():
        parent_path = os.path.join(dest_folder, parent_folder)
        os.makedirs(parent_path, exist_ok=True)
        created_folders += 1
        progress_var.set(created_folders / total_folders * 100)
        root.update_idletasks()
        for subfolder in subfolders:
            subfolder_path = os.path.join(parent_path, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)
            created_folders += 1
            progress_var.set(created_folders / total_folders * 100)
            root.update_idletasks()

def start_creating_folders():
    dest_folder = dest_folder_var_create.get()
    folder_structure = folder_names_text.get("1.0", tk.END).strip()  # get text from Text widget
    create_folders(dest_folder, folder_structure, progress_var_create)

def browse_dest_folder_for_creation():
    dest_folder = filedialog.askdirectory(title="Select Destination Folder for Creation")
    dest_folder_var_create.set(dest_folder)
    
root = tk.Tk()
root.title("Archive Extractor, File Mover, and Folder Renamer, Folder Creator")

root.configure(bg='#000000')

top_frame = tk.Frame(root, bg='#000000')
top_frame.pack(side=tk.TOP, padx=10, pady=5)  # Pack the frame at the top

tk.Button(top_frame, text="Refresh", command=refresh_gui, bg='#00df1f', fg='#000000').pack(side=tk.LEFT, padx=5)  # Pack button in top_frame
  # Pack button in top_frame
tk.Button(top_frame, text="Close", command=close_gui, bg='#e00000', fg='#000000').pack(side=tk.LEFT)  # Pack button in top_frame

src_folder_var = tk.StringVar()
dest_folder_var = tk.StringVar()
progress_var = tk.DoubleVar()
src_folder_var_renaming = tk.StringVar()
progress_var_moving = tk.DoubleVar()
progress_var_renaming = tk.DoubleVar()

style = ttk.Style()
style.configure("TProgressbar",
                thickness=20,
                troughcolor='#000000',
                background='#7af7ff',
                )


frame1 = tk.Frame(root, bg='#000000')
frame1.pack(fill=tk.X, padx=10, pady=5)

tk.Label(frame1, text="Source Folder:", bg='#000000', fg='#ffffff').pack(side=tk.LEFT)
tk.Entry(frame1, textvariable=src_folder_var, width=50, bg='#222222', fg='#ffffff').pack(side=tk.LEFT, fill=tk.X, expand=True)
tk.Button(frame1, text="Browse", command=browse_src_folder, bg='#7af7ff', fg='#000000').pack(side=tk.LEFT)

frame2 = tk.Frame(root, bg='#000000')
frame2.pack(fill=tk.X, padx=10, pady=5)

tk.Label(frame2, text="Destination Folder:", bg='#000000', fg='#ffffff').pack(side=tk.LEFT)
tk.Entry(frame2, textvariable=dest_folder_var, width=50, bg='#222222', fg='#ffffff').pack(side=tk.LEFT, fill=tk.X, expand=True)
tk.Button(frame2, text="Browse", command=browse_dest_folder, bg='#7af7ff', fg='#000000').pack(side=tk.LEFT)

frame3 = tk.Frame(root, bg='#000000')
frame3.pack(fill=tk.X, padx=10, pady=5)

tk.Button(frame3, text="Start Extraction", command=start_extraction, bg='#7af7ff', fg='#000000').pack()

frame4 = tk.Frame(root, bg='#000000')
frame4.pack(fill=tk.X, padx=10, pady=5)

progressbar = ttk.Progressbar(frame4, variable=progress_var, maximum=100, style="TProgressbar")
progressbar.pack(fill=tk.X, expand=True)

frame5 = tk.Frame(root, bg='#000000')
frame5.pack(fill=tk.X, padx=10, pady=5)

tk.Label(frame5, text="Source Folder for Moving:", bg='#000000', fg='#ffffff').pack(side=tk.LEFT)
tk.Entry(frame5, textvariable=src_folder_var, width=50, bg='#222222', fg='#ffffff').pack(side=tk.LEFT, fill=tk.X, expand=True)
tk.Button(frame5, text="Browse", command=browse_src_folder_for_moving, bg='#7af7ff', fg='#000000').pack(side=tk.LEFT)

frame6 = tk.Frame(root, bg='#000000')
frame6.pack(fill=tk.X, padx=10, pady=5)

tk.Button(frame6, text="Start Moving and Deleting", command=start_moving_and_deleting, bg='#7af7ff', fg='#000000').pack()

frame7 = tk.Frame(root, bg='#000000')
frame7.pack(fill=tk.X, padx=10, pady=5)

progressbar_moving = ttk.Progressbar(frame7, variable=progress_var_moving, maximum=100, style="TProgressbar")
progressbar_moving.pack(fill=tk.X, expand=True)

frame8 = tk.Frame(root, bg='#000000')
frame8.pack(fill=tk.X, padx=10, pady=5)

tk.Label(frame8, text="Source Folder for Renaming:", bg='#000000', fg='#ffffff').pack(side=tk.LEFT)
tk.Entry(frame8, textvariable=src_folder_var_renaming, width=50, bg='#222222', fg='#ffffff').pack(side=tk.LEFT, fill=tk.X, expand=True)
tk.Button(frame8, text="Browse", command=browse_src_folder_for_renaming, bg='#7af7ff', fg='#000000').pack(side=tk.LEFT)

frame9 = tk.Frame(root, bg='#000000')
frame9.pack(fill=tk.X, padx=10, pady=5)

tk.Button(frame9, text="Start Renaming", command=start_renaming, bg='#7af7ff', fg='#000000').pack()

frame10 = tk.Frame(root, bg='#000000')
frame10.pack(fill=tk.X, padx=10, pady=5)

progressbar_renaming = ttk.Progressbar(frame10, variable=progress_var_renaming, maximum=100, style="TProgressbar")
progressbar_renaming.pack(fill=tk.X, expand=True)


# New Tkinter StringVar and DoubleVar
progress_var_create = tk.DoubleVar()
dest_folder_var_create = tk.StringVar()

frame11 = tk.Frame(root, bg='#000000')
frame11.pack(fill=tk.X, padx=10, pady=5)

tk.Label(frame11, text="Destination Folder for Creation:", bg='#000000', fg='#ffffff').pack(side=tk.LEFT)
tk.Entry(frame11, textvariable=dest_folder_var_create, width=50, bg='#222222', fg='#ffffff').pack(side=tk.LEFT, fill=tk.X, expand=True)
tk.Button(frame11, text="Browse", command=browse_dest_folder_for_creation, bg='#7af7ff', fg='#000000').pack(side=tk.LEFT)

frame12 = tk.Frame(root, bg='#000000')
frame12.pack(fill=tk.X, padx=10, pady=5)

tk.Label(frame12, text="Folder Structure (in JSON format):", bg='#000000', fg='#ffffff').pack(side=tk.LEFT)
folder_names_text = tk.Text(frame12, width=50, height=10, bg='#222222', fg='#ffffff')  # set a height to allow multi-line input
folder_names_text.pack(side=tk.LEFT, fill=tk.X, expand=True)

example_structure = """
{
    "Work": ["Project1", "Project2"],
    "Personal": ["Photos", "Documents"],
    "Misc": []
}
"""
folder_names_text.insert(tk.END, example_structure.strip())  # pre-fill the Text widget with the example structure

frame13 = tk.Frame(root, bg='#000000')
frame13.pack(fill=tk.X, padx=10, pady=5)

tk.Button(frame13, text="Create Folders", command=start_creating_folders, bg='#7af7ff', fg='#000000').pack()

frame14 = tk.Frame(root, bg='#000000')
frame14.pack(fill=tk.X, padx=10, pady=5)

style = ttk.Style()
style.configure("TProgressbar",
                thickness=20,
                troughcolor='#000000',
                background='#7af7ff',
                )

progressbar_create = ttk.Progressbar(frame14, variable=progress_var_create, maximum=100, style="TProgressbar")
progressbar_create.pack(fill=tk.X, expand=True)

root.mainloop()