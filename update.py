
import gdown
import zipfile
import os
import ctypes

url = "https://drive.google.com/uc?id=1iQ66JgdxJQHEePVGwZQvuaveAR0I6aVR&export=download"

destination = "update.zip"

gdown.download(url, destination, quiet=False)

with zipfile.ZipFile("./update.zip", 'r') as zip_ref:
    zip_ref.extractall("./")
try:
    os.remove("./update.zip")
except:
    pass

file_path = os.path.realpath(__file__)
os.remove(file_path)
ctypes.windll.user32.MessageBoxW(None, "Update Finished!", "Info", 0x40 | 0x0 | 0x1000)
