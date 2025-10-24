"""Common specifications for source data files."""

colspecs_2018 = [
    (8, 12),     #   0   DOB_YY         Birth Year
    (12, 14),    #   1   DOB_MM         Birth Month
    (31, 32),    #   2   BFACIL         Birth Place
    (32, 33),    #   3   F_BFACIL       Reporting Flag for Birth Place
    (72, 73),    #   4   MAGE_IMPFLG    Mother's Age Imputed
    (73, 74),    #   5   MAGE_REPFLG    Reported Age of Mother Used Flag
    (74, 76),    #   6   MAGER          Mother's Single Years of Age
    (76, 78),    #   7   MAGER14        Mother's Age Recode 14
    (78, 79),    #   8   MAGER9         Mother's Age Recode 9
    (83, 84),    #   9   MBSTATE_REC    Mother's Nativity
    (103, 104),  #  10   RESTATUS       Residence Status
    (104, 106),  #  11   MRACE31        Mother's Race Recode 31
    (106, 107),  #  12   MRACE6         Mother's Race Recode 6
    (107, 109),  #  13   MRACE15        Mother's Race Recode 15
    (110, 111),  #  14   MRACEIMP       Mother's Race Imputed Flag
    (111, 112),  #  15   MHISPX         Mother's Hispanic Origin
    (114, 115),  #  16   MHISP_R        Mother's Hispanic Origin Recode
    (115, 116),  #  17   F_MHISP        Reporting Flag for Mother's Origin
    (116, 117),  #  18   MRACEHISP      Mother's Race/Hispanic Origin
    (118, 119),  #  19   MAR_P          Paternity Acknowledged
    (119, 120),  #  20   DMAR           Marital Status
    (120, 121),  #  21   MAR_IMP        Mother's Marital Status Imputed
    (122, 123),  #  22   F_MAR_P        Reporting Flag for Paternity Acknowledged
    (123, 124),  #  23   MEDUC          Mother's Education
    (125, 126),  #  24   F_MEDUC        Reporting Flag for Education of Mother
    (141, 142),  #  25   FAGERPT_FLG    Father's Reported Age Used
    (146, 148),  #  26   FAGECOMB       Father's Combined Age
    (148, 150),  #  27   FAGEREC11      Father's Age Recode 11
    (150, 152),  #  28   FRACE31        Father's Race Recode 31
    (152, 153),  #  29   FRACE6         Father's Race Recode 6
    (153, 155),  #  30   FRACE15        Father's Race Recode 15
    (158, 159),  #  31   FHISPX         Father's Hispanic Origin
    (159, 160),  #  32   FHISP_R        Father's Hispanic Origin Recode
    (160, 161),  #  33   F_FHISP        Reporting Flag for Father's Hispanic Origin
    (161, 162),  #  34   FRACEHISP      Father's Race/Hispanic Origin
    (162, 163),  #  35   FEDUC          Father's Education
    (170, 172),  #  36   PRIORLIVE      Number of Previous Live Births
    (172, 174),  #  37   PRIORDEAD      Number of Previous Other Pregnancy Outcomes
    (174, 176),  #  38   PRIORTERM      Number of Previous Terminations
    (178, 179),  #  39   LBO_REC        Live Birth Order Recode
    (181, 182),  #  40   TBO_REC        Total Birth Order Recode
    (223, 225),  #  41   PRECARE        Month Prenatal Care Began
    (434, 435),  #  42   PAY            Payment Source for Delivery
    (435, 436),  #  43   PAY_REC        Payment Recode
    (436, 437),  #  44   F_PAY          Reporting Flag for Source of Payment
    (437, 438),  #  45   F_PAY_REC      Reporting Flag for Payment Recode
    (474, 475),  #  46   SEX            Sex of Infant
    (475, 476),  #  47   IMP_SEX        Imputed Sex
    (536, 537),  #  48   CA_ANEN        Anencephaly
    (537, 538),  #  49   CA_MNSB        Meningomyelocele / Spina Bifida
    (538, 539),  #  50   CA_CCHD        Cyanotic Congenital Heart Disease
    (539, 540),  #  51   CA_CDH         Congenital Diaphragmatic Hernia
    (540, 541),  #  52   OMPH           Omphalocele
    (541, 542),  #  53   CA_GAST        Gastroschisis
    (542, 543),  #  54   F_CA_ANEN      Reporting Flag for Anencephaly
    (543, 544),  #  55   F_CA_MENIN     Reporting Flag for Meningomyelocele/Spina Bifida
    (544, 545),  #  56   F_CA_HEART     Reporting Flag for Cyanotic Congenital Heart Disease
    (545, 546),  #  57   F_CA_HERNIA    Reporting Flag for Congenital Diaphragmatic Hernia
    (546, 547),  #  58   F_CA_OMPHA     Reporting Flag for Omphalocele
    (547, 548),  #  59   F_CA_GASTRO    Reporting Flag for Gastroschisis
    (548, 549),  #  60   CA_LIMB        Limb Reduction Defect
    (549, 550),  #  61   CA_CLEFT       Cleft Lip w/ or w/o Cleft Palate
    (550, 551),  #  62   CA_CLPAL       Cleft Palate alone
    (551, 552),  #  63   CA_DOWN        Down Syndrome
    (552, 553),  #  64   CA_DISOR       Suspected Chromosomal Disorder
    (553, 554),  #  65   CA_HYPO        Hypospadias
    (554, 555),  #  66   F_CA_LIMB      Reporting Flag for Limb Reduction Defect
    (555, 556),  #  67   F_CA_CLEFT     Reporting Flag for Cleft Lip with or without Cleft Palate
    (556, 557),  #  68   F_CA_CLPAL     Reporting Flag for Cleft Palate Alone
    (557, 558),  #  69   F_CA_DOWN      Reporting Flag for Down Syndrome
    (558, 559),  #  70   F_CA_DISOR     Reporting Flag for Suspected Chromosomal Disorder
    (559, 560),  #  71   F_CA_HYPO      Reporting Flag for Hypospadias
    (560, 561),  #  72   NO_CONGEN      No Congenital Anomalies Checked
    (225, 226),  #  73   F_MPCB         Reporting Flag for Month Prenatal Care Began
    (226, 227),  #  74   PRECARE5       Month Prenatal Care Began Recode
    (237, 239),  #  75   PREVIS         Number of Prenatal Visits
    (241, 243),  #  76   PREVIS_REC     Number of Prenatal Visits Recode
    (243, 244),  #  77   F_TPCV         Reporting Flag for Total Prenatal Care Visits
    (250, 251),  #  78   WIC            WIC
    (251, 252),  #  79   F_WIC          Reporting Flag for WIC
]

colspecs_2019 = colspecs_2018

colspecs_2020 = colspecs_2019

colspecs_2021 = colspecs_2020

colspecs_2022 = colspecs_2021

colspecs_2023 = colspecs_2022

colspecs_2024 = colspecs_2022

# 2017 does not have MHISPX that appears in later years
colspecs_2017 = colspecs_2018

colspecs_2016 = colspecs_2017

colspecs_2015 = colspecs_2016

colspecs_2014 = colspecs_2015
