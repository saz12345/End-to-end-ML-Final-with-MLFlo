import os
import urllib.request as request
import zipfile
from src.mlProject.utils._init_ import logger
from src.mlProject.utils.common import get_size
from pathlib import Path
from src.mlProject.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    
    def download_file(self):
        os.makedirs(Path(self.config.local_data_file).parent, exist_ok=True)


        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,             # <-- use source_URL
                filename=str(self.config.local_data_file)    # <-- save to local path
        )
            logger.info(f"{filename} downloaded with headers:\n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)