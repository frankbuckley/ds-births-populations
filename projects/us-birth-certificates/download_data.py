"""Downloads source data and user guides from CDC.

Refer to terms at: https://www.cdc.gov/nchs/data_access/restrictions.htm
"""

import os
import urllib.request

user_guides = [
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/UserGuide2022.pdf",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/UserGuide2021.pdf",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/UserGuide2020.pdf",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/UserGuide2019-508.pdf",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/UserGuide2018-508.pdf",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/UserGuide2017.pdf",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/UserGuide2016.pdf",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/UserGuide2015.pdf",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/UserGuide2014.pdf",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/UserGuide2013.pdf",
]

us_data_files = [
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/DVS/natality/Nat2022us.zip",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/DVS/natality/Nat2021us.zip",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/DVS/natality/Nat2020us.zip",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/DVS/natality/Nat2019us.zip",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/DVS/natality/Nat2018us.zip",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/DVS/natality/Nat2017us.zip",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/DVS/natality/Nat2016us.zip",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/DVS/natality/Nat2015us.zip",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/DVS/natality/Nat2014us.zip",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/DVS/natality/Nat2013us.zip"
]

if not os.path.exists("data"):
    os.makedirs("data")

for user_guide in user_guides:
    filename = "data/" + user_guide.rsplit("/", maxsplit=1)[-1]
    if not os.path.exists(filename):
        print(f"Downloading {user_guide}")
        urllib.request.urlretrieve(user_guide, filename)

for data_file in us_data_files:
    filename = "data/" + data_file.rsplit("/", maxsplit=1)[-1]
    if not os.path.exists(filename):
        print(f"Downloading {data_file}")
        urllib.request.urlretrieve(data_file, filename)

# Python ZipFile module fails with some of the data files
# so see unzip_data.ps1 for a PowerShell script to unzip the files
