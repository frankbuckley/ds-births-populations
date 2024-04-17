# US Birth Certificates

**Analysis of US birth certificate data.**

This project is exploring trends in live births of babies with Down syndrome in the US using data from the [National Vital Statistics System (NVSS)](https://www.cdc.gov/nchs/nvss/births.htm) which is provided by the [National Center for Health Statistics](https://www.cdc.gov/nchs/index.htm).

Information about the release of this data is [available from the NVSS](https://www.cdc.gov/nchs/nvss/dvs_data_release.htm).

Use of the data is subject to the [National Center for Health Statistics (NCHS) Data Use Agreement](https://www.cdc.gov/nchs/data_access/restrictions.htm).

## Getting started

### Requirements

- [Python](https://www.python.org/downloads/) (tested so far on Windows and MacOS with version 3.12.3)
- [PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell) (tested so far on Windows and MacOS with version 7.4.2)

To install Python packages:

```bash
pip install -r .\requirements.txt --upgrade
```

### Download data

The source data files are large and are subject to the [National Center for Health Statistics (NCHS) Data Use Agreement](https://www.cdc.gov/nchs/data_access/restrictions.htm) and are therefore not included in this repository.

The data files can be downloaded and extracted using the scripts described below.

To download the data files and user guides:

```bash
python ./prepare/download_data.py
```

This will place the downloads in a `data` folder.

To unzip the data files:

```bash
pwsh ./prepare/unzip_data.zip
```

**Note**: there is an issue unzipping 2015 data. This can be completed manually using [7-Zi](https://www.7-zip.org/)

This will extract the data files into subfolders: `data/Nat2015us`, `data/Nat2016us` and so on.
