import requests
import shutil
import zipfile
import os

def download_file_from_google_drive(file_id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()
    response = session.get(URL, params={'id': file_id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)

    return True

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def save_response_content(response, destination, chunk_size=32768):
    with open(destination, "wb") as f:
        for chunk in response.iter_content(chunk_size):
            if chunk:
                f.write(chunk)

# ==== USAGE ====

file_id = "1ykvdJv9t5w6ct-ndPEteXkNre2pCZ167"
zip_destination = "update.zip"

updated = download_file_from_google_drive(file_id, zip_destination)

if updated:
    try:
        shutil.rmtree('bin-main')
    except:
        pass
    with zipfile.ZipFile("./update.zip", 'r') as zip_ref:
        zip_ref.extractall("./")
    try:
        os.remove("./update.zip")
    except:
        pass

file_path = os.path.realpath(__file__)
os.remove(file_path)