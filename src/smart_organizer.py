import os
import shutil

# directories needed to manage files
images = "/IMAGES/"
audios = "/AUDIOS/"
videos = "/VIDEOS/"
documents = "/DOCUMENTS/"
zip_files = "/ZIP_FILES/"

# file extensions used to assign to a directory
image_extensions = ["apng", "avif", "gif", "jpg", "jpeg", "png", "svg", "webp"]
audio_extensions = ["mp3", "wav", "m4a"]
video_extensions = ["mp4", "mov", "m4p", "avi"]
document_extensions = ["pdf", "html", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "txt"]
zip_extensions = ["zip", "rar"]

# list of all the directories
directories_list = [images, audios, videos, documents, zip_files]

# get directory of file
path = os.path.dirname(__file__)

# list of all files
files = os.listdir()

# create needed directories if they dont exist
def create_directories():
    for directory in directories_list:
        if not os.path.exists(path + directory):
            os.mkdir(path + directory)

# get the file name without extension
def extension(file):
    return file.split(".")[-1].lower()

# loop through files and move files according to type
def organize_files():
    for file in files:
        if extension(file) in image_extensions:
            shutil.move(file, path + images)
        elif extension(file) in audio_extensions:
            shutil.move(file, audios)
        elif extension(file) in video_extensions:
            shutil.move(file, videos)
        elif extension(file) in document_extensions:
            shutil.move(file, documents)
        elif extension(file) in zip_extensions:
            shutil.move(file, zip_files)
           
# call functions to create directories and move files
create_directories()
organize_files()