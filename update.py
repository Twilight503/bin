
import gdown
import zipfile
import os

url = "https://drive.google.com/uc?id=1tDdTft3_EGy_ui8qCCu5jg8wq5xfz4IO&export=download"

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
