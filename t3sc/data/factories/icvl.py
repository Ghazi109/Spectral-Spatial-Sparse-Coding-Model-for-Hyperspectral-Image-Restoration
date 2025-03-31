import logging
import os
import subprocess
import torch
import h5py
import numpy as np
import requests


from t3sc.data.normalizers import GlobalMinMax
from .base_factory import DatasetFactory
from .utils import check_filesize, touch
from t3sc.data.splits import (
    icvl_train,
    icvl_val,
    icvl_test,
    icvl_crops,
    icvl_rgb,
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class ICVL(DatasetFactory):
    NAME = "ICVL"
    IMG_SHAPE = (31, 1024, 1024)
    CROPS = icvl_crops
    RGB = icvl_rgb

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        assert self.split == 0

        self.f_train = icvl_train
        self.f_val = icvl_val
        self.f_test = icvl_test

    @classmethod
    # This function has been modified to update the URL as the old one is no longer valid. 
    # We are now using the 'requests' library to download files instead of 'subprocess' 
    # as it was causing errors.


    def download(cls, path_data):
        BASE_URL = "https://huggingface.co/datasets/danaroth/icvl/resolve/main/mat"
        path_dataset = os.path.join(path_data, cls.NAME)
        path_raw = os.path.join(path_dataset, "raw")
        path_dl_complete = os.path.join(path_raw, ".download_complete")

        # Check if the dataset has already been downloaded
        if os.path.exists(path_dl_complete):
            logger.info("Dataset already downloaded.")
            return

        logger.info(f"{path_dl_complete!r} not found, starting download...")
        os.makedirs(path_raw, exist_ok=True)

        # List of all the files to be downloaded
        icvl_all = icvl_train + icvl_val + icvl_test
        icvl_all = [f"{fn}.mat" for fn in icvl_all]

        # Download each file
        for i, filename in enumerate(icvl_all):
            target = os.path.join(path_raw, filename)
            url = os.path.join(BASE_URL, filename)

            logger.info(f"Checking file ({i + 1}/{len(icvl_all)}): {filename}")

            # Check if the file already exists and has the correct size
            if os.path.exists(target) and check_filesize(target, url):
                logger.info("File already exists.")
                continue

            # Download the file
            logger.info("Downloading...")
            try:
                response = requests.get(url, stream=True)
                if response.status_code == 200:
                    with open(target, "wb") as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    logger.info(f"File {filename} downloaded successfully.")
                else:
                    logger.error(f"Download failed for {filename}. Error code: {response.status_code}")
            except Exception as e:
                logger.error(f"Error during download of {filename}: {e}")

        # Create the .download_complete file to indicate that the download is complete
        touch(path_dl_complete)
        logger.info("Download complete.")


    def preprocess(self):
        path_source = os.path.join(self.path_data, self.NAME, "raw")
        path_dest = os.path.join(self.path_data, self.NAME, "clean")
        path_complete = os.path.join(path_dest, ".complete")
        if os.path.exists(path_complete):
            return

        os.makedirs(path_dest, exist_ok=True)

        normalizer = GlobalMinMax()
        icvl_all = list(set(self.f_train + self.f_test + self.f_val))

        for i, fn in enumerate(icvl_all):
            path_out = os.path.join(path_dest, f"{fn}.pth")
            if os.path.exists(path_out):
                continue
            logger.info(f"Preprocessing {fn}")
            path_in = os.path.join(path_source, f"{fn}.mat")
            with h5py.File(path_in, "r") as f:
                img = np.array(f["rad"], dtype=np.float32)
            img_torch = torch.tensor(img, dtype=torch.float32)
            img_torch = normalizer.transform(img_torch).clone()
            logger.info(f"shape : {tuple(img_torch.shape)} ")

            torch.save(img_torch, path_out)
            logger.info(
                f"Saved normalized image {i + 1}/{len(icvl_all)} "
                f"to {path_out}"
            )
        touch(path_complete)
        logger.info(f"Dataset preprocessed")
