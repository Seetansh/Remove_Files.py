# script to remove desired files from master folder

import os
from tkinter import Tk, filedialog, simpledialog 

# prompt for extension selection
def input_extension():
    title = "Enter String"
    prompt = "Please enter an extension:"
    string_input = simpledialog.askstring(title, prompt)

# Check if the user canceled or entered a value
    if string_input is not None:
        print("You entered:", string_input)
    else:
        print("User canceled input.")
    return string_input


# prompt for browsing folder
def browse_for_folder():
  # Get the root window (hidden)
  root = Tk()
  root.withdraw()  # Hide the main window
  # Open the folder selection dialog
  folder_path = filedialog.askdirectory(title="Select Folder")
  # Do something with the folder path
  if folder_path is not None:
        print(f"Selected folder: {folder_path}")
        return folder_path
  else:
     print("Choose a folder first!")
     exit


def delete_files(folder_path, extension):
  """
      Args:
      folder_path: Path to the master folder.
      extension: The extension of files to delete (e.g., ".pdf", ".jpg").
  """
  for root, dirs, files in os.walk(folder_path):
    for file in files:
      if file.endswith(extension):
        full_path = os.path.join(root, file)
        os.remove(full_path)

# folder path
master_folder = browse_for_folder()

# Specify the extension (including the doty
# )
extension_to_delete = input_extension()

print("Deletion completed")


# Use this script carefully because it will remove files permanently. So, Keep backup of the files.
# Any advancement you wanna do you can!
# I havn't focused on error handling, My main focus is on 'The work should be done'
# You can add solution for the errors.
# Happy Coding!!!