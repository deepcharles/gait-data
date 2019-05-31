import sys
import json
import os
from urllib.request import URLopener
import tarfile

import pandas as pd


DATA_HOME = "GaitData"
CODE_LIST_FNAME = "code_list.json"
DOWNLOAD_URL = "http://dev.ipol.im/~truong/GaitData.tar.gz"
DOWNLOAD_URL = "https://mycore.core-cloud.net/index.php/s/Yq3QkYO0LAvAsLv/download"
ARCHIVE_FNAME = "GaitData.tar.gz"


def download_data():
    """This function downloads the data, extract them and remove the archive."""
    if not os.path.exists(DATA_HOME):
        print("Data are missing. Downloading them now...", end="", flush=True)
        datafile = URLopener()
        datafile.retrieve(DOWNLOAD_URL, ARCHIVE_FNAME)
        print("Ok.")
        print("Extracting now...", end="", flush=True)
        tf = tarfile.open(ARCHIVE_FNAME)
        tf.extractall()
        print("Ok.")
        print("Removing the archive...", end="", flush=True)
        os.remove(ARCHIVE_FNAME)
        print("Ok.")


def get_filename(code):
    """Returns the filename of the signal file and the metadata file.

    Parameters
    ----------
    code : str
        Code of the trial ("Patient-Trial").

    Returns
    -------
    str
        Filename.
    """
    subject_str, trial_str = code.split("-")
    subject = int(subject_str)
    trial = int(trial_str)
    filename = os.path.join(DATA_HOME, code)
    assert os.path.exists(
        filename + ".csv"), "The code {} cannot be found in the data set.".format(code)
    return filename


def load_trial(code):
    """Returns the signal of the trial.

    Parameters
    ----------
    code : str
        Code of the trial ("Patient-Trial")

    Returns
    -------
    panda array
        Signal of the the trial, shape (n_sample, n_dimension).
    """
    fname = get_filename(code)
    df = pd.read_csv(fname + ".csv", sep=",")
    return df


def load_metadata(code):
    """Returns the metadata of the trial.

    Parameters
    ----------
    code : str
        Code of the trial ("Patient-Trial").

    Returns
    -------
    dict
        Metadata dictionary.
    """
    fname = get_filename(code)
    with open(fname + ".json", "r") as f:
        metadata = json.load(f)
    return metadata


def get_code_list():
    """Returns the list of all available codes.

    Returns
    -------
    list
        List of codes.
    """
    with open(CODE_LIST_FNAME, "r") as f:
        code_list = json.load(f)
    return code_list


if __name__ == "__main__":
    download_data()
    all_codes = get_code_list()
    print("There are {} trials.".format(len(all_codes)))
    for code in all_codes:
        signal = load_trial(code)
        metadata = load_metadata(code)
        # Do something.
        # ...
