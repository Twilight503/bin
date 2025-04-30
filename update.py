import gdown
import zipfile
import os

file_id = "1ykvdJv9t5w6ct-ndPEteXkNre2pCZ167"
destination = "update.zip"
url = f"https://drive.google.com/uc?id={file_id}"

gdown.download(url, destination, quiet=False)

with zipfile.ZipFile("./update.zip", 'r') as zip_ref:
    zip_ref.extractall("./")
try:
    os.remove("./update.zip")
except:
    pass

file_path = os.path.realpath(__file__)
os.remove(file_path)