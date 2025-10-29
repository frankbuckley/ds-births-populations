"""Downloads source data and user guides from CDC.

Refer to terms at: https://www.cdc.gov/nchs/data_access/restrictions.htm
"""

import os
import urllib.request
import truststore

truststore.inject_into_ssl()  # avoids SSL: CERTIFICATE_VERIFY_FAILED on MacOS


user_guides = [
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/UserGuide2023.pdf",
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
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/UserGuide2012.pdf",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/UserGuide2011.pdf",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/UserGuide2010_Addendum.pdf",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/UserGuide2010.pdf",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/UserGuide2009_Addendum.pdf",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/UserGuide2009.pdf",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/UserGuide2008.pdf",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/UserGuide2007.pdf",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/UserGuide2006.pdf",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/UserGuide2005.pdf",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/Nat2004doc.pdf",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/Nat2003doc.pdf",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/Nat2002doc.pdf",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/Nat2001doc.pdf",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/Nat2000doc.pdf",
]

# 1989 is the first year DOWNS is included to 2002; UCA_DOWNS in 2003; UCA_DOWNS and CA_DOWNS in 2004; from 2004 this is coded as CA_DOWNS
us_data_files_sas = [
    "https://data.nber.org/nvss/natality/sas/1989/natality1989us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/1990/natality1990us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/1991/natality1991us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/1992/natality1992us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/1993/natality1993us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/1994/natality1994us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/1995/natality1995us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/1996/natality1996us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/1997/natality1997us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/1998/natality1998us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/1999/natality1999us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2000/natality2000us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2001/natality2001us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2002/natality2002us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2003/natality2003us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2004/natality2004us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2005/natality2005us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2006/natality2006us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2007/natality2007us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2008/natality2008us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2009/natality2009us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2010/natality2010us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2011/natality2011us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2012/natality2012us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2013/natality2013us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2014/natality2014us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2015/natality2015us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2016/natality2016us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2015/natality2015us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2018/natality2018us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2019/natality2019us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2020/natality2020us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2021/natality2021us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2022/natality2022us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2023/natality2023us.sas7bdat",
    "https://data.nber.org/nvss/natality/sas/2024/natality2024us.sas7bdat",
]

us_data_files_stata = [
    "https://data.nber.org/nvss/natality/dta/2012/natality2012us.dta"
]

if not os.path.exists("data"):
    os.makedirs("data")

for user_guide in user_guides:
    filename = "data/" + user_guide.rsplit("/", maxsplit=1)[-1]
    if not os.path.exists(filename):
        print(f"Downloading {user_guide}")
        urllib.request.urlretrieve(user_guide, filename)

for data_file in us_data_files_sas:
    filename = "data/" + data_file.rsplit("/", maxsplit=1)[-1]
    if not os.path.exists(filename):
        print(f"Downloading {data_file}")
        urllib.request.urlretrieve(data_file, filename)
