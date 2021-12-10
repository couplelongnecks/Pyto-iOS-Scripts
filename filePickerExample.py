#Example for using the FilePicker
import sharing

filePicker = sharing.FilePicker()
filePicker.file_types = ["public.data"]
filePicker.allows_multiple_selection = True

def files_picked() -> None:
    files = sharing.picked_files()
    
    #Default example to share.
    #sharing.share_items(files)
    return files

filePicker.completion = files_picked
sharing.pick_documents(filePicker)

files = files_picked()
print (files)