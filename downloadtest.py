import os
from six.moves import urllib
import urllib.request
import requests
import subprocess
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.entity.config_entity import DataIngestionConfig
from signLanguage.entity.artifacts_entity import DataIngestionArtifact



dataset_url = "https://github.com/entbappy/Branching-tutorial/raw/master/Sign_language_data.zip"
# "http://github.com/mayankchugh-learning/myDSprojectDataZips/raw/main/Sign_language_data.zip"
# "https://github.com/entbappy/Branching-tutorial/raw/master/Sign_language_data.zip"
# https://github.com/mayankchugh-learning/myDSprojectDataZips/blob/main/Sign_language_data.zip

os.makedirs("test", exist_ok=True)
data_file_name = os.path.basename(dataset_url)
zip_file_path = os.path.join("test", data_file_name)
logging.info(f"Downloading data from {dataset_url} into file {zip_file_path}")


urllib.request.urlretrieve(dataset_url, zip_file_path)
#subprocess.run(['wget', dataset_url, '-O', zip_file_path])
print('File downloaded successfully!')


#urllib.request.urlretrieve(dataset_url, zip_file_path)


# print ("download start!")
# filename, headers = urllib.request.urlretrieve(dataset_url, filename=zip_file_path)
# print ("download complete!")
# print ("download file location: ", filename)
# print ("download headers: ", headers)

logging.info(f"Downloaded data from {dataset_url} into file {zip_file_path}")



        