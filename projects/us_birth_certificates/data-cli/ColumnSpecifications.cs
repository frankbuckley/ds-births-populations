// Copyright (c) Frank Buckley and Contributors. All Rights Reserved.
// Frank Buckley and Contributors licence this file to you under the MIT license.

using System.Globalization;
using System.Numerics;

namespace Populations.Data.CLI;

/*

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
 */
public static class ColumnSpecifications
{
    public static readonly Range YearOfBirth = 8..12;
    public static readonly Range MonthOfBirth = 12..14;
    public static readonly Range BirthPlace = 31..32;
    public static readonly Range ReportingFlagForBirthPlace = 32..33;
    public static readonly Range MothersAgeImputed = 72..73;
    public static readonly Range ReportedAgeOfMotherUsedFlag = 73..74;
    public static readonly Range MothersSingleYearsOfAge = 74..76;
    public static readonly Range MothersAgeRecode14 = 76..78;
    public static readonly Range MothersAgeRecode9 = 78..79;
    public static readonly Range MothersNativity = 83..84;
    public static readonly Range ResidenceStatus = 103..104;
    public static readonly Range MothersRaceRecode31 = 104..106;
    public static readonly Range MothersRaceRecode6 = 106..107;
    public static readonly Range MothersRaceRecode15 = 107..109;
    public static readonly Range MothersRaceImputedFlag = 110..111;
    public static readonly Range MothersHispanicOrigin = 111..112;
    public static readonly Range MothersHispanicOriginRecode = 114..115;
    public static readonly Range ReportingFlagForMothersOrigin = 115..116;
    public static readonly Range MothersRaceHispanicOrigin = 116..117;
    public static readonly Range PaternityAcknowledged = 118..119;
    public static readonly Range MaritalStatus = 119..120;
    public static readonly Range MothersMaritalStatusImputed = 120..121;
    public static readonly Range ReportingFlagForPaternityAcknowledged = 122..123;
    public static readonly Range MothersEducation = 123..124;
    public static readonly Range ReportingFlagForEducationOfMother = 125..126;
    public static readonly Range FathersReportedAgeUsed = 141..142;
    public static readonly Range FathersCombinedAge = 146..148;
    public static readonly Range FathersAgeRecode11 = 148..150;
    public static readonly Range FathersRaceRecode31 = 150..152;
    public static readonly Range FathersRaceRecode6 = 152..153;
    public static readonly Range FathersRaceRecode15 = 153..155;
    public static readonly Range FathersHispanicOrigin = 158..159;
    public static readonly Range FathersHispanicOriginRecode = 159..160;
    public static readonly Range ReportingFlagForFathersHispanicOrigin = 160..161;
    public static readonly Range FathersRaceHispanicOrigin = 161..162;
    public static readonly Range FathersEducation = 162..163;
    public static readonly Range NumberOfPreviousLiveBirths = 170..172;
    public static readonly Range NumberOfPreviousOtherPregnancyOutcomes = 172..174;
    public static readonly Range NumberOfPreviousTerminations = 174..176;
    public static readonly Range LiveBirthOrderRecode = 178..179;
    public static readonly Range TotalBirthOrderRecode = 181..182;
    public static readonly Range MonthPrenatalCareBegan = 223..225;
    public static readonly Range PaymentSourceForDelivery = 434..435;
    public static readonly Range PaymentRecode = 435..436;
    public static readonly Range ReportingFlagForSourceOfPayment = 436..437;
    public static readonly Range ReportingFlagForPaymentRecode = 437..438;
    public static readonly Range SexOfInfant = 474..475;
    public static readonly Range ImputedSex = 475..476;
    public static readonly Range Anencephaly = 536..537;
    public static readonly Range MeningomyeloceleSpinaBifida = 537..538;
    public static readonly Range CyanoticCongenitalHeartDisease = 538..539;
    public static readonly Range CongenitalDiaphragmaticHernia = 539..540;
    public static readonly Range Omphalocele = 540..541;
    public static readonly Range Gastroschisis = 541..542;
    public static readonly Range ReportingFlagForAnencephaly = 542..543;
    public static readonly Range ReportingFlagForMeningomyeloceleSpinaBifida = 543..544;
    public static readonly Range ReportingFlagForCyanoticCongenitalHeartDisease = 544..545;
    public static readonly Range ReportingFlagForCongenitalDiaphragmaticHernia = 545..546;
    public static readonly Range ReportingFlagForOmphalocele = 546..547;
    public static readonly Range ReportingFlagForGastroschisis = 547..548;
    public static readonly Range LimbReductionDefect = 548..549;
    public static readonly Range CleftLipWithOrWithoutCleftPalate = 549..550;
    public static readonly Range CleftPalateAlone = 550..551;
    public static readonly Range DownSyndrome = 551..552;
    public static readonly Range SuspectedChromosomalDisorder = 552..553;
    public static readonly Range Hypospadias = 553..554;
    public static readonly Range ReportingFlagForLimbReductionDefect = 554..555;
    public static readonly Range ReportingFlagForCleftLipWithOrWithoutCleftPalate = 555..556;
    public static readonly Range ReportingFlagForCleftPalateAlone = 556..557;
    public static readonly Range ReportingFlagForDownSyndrome = 557..558;
    public static readonly Range ReportingFlagForSuspectedChromosomalDisorder = 558..559;
    public static readonly Range ReportingFlagForHypospadias = 559..560;
    public static readonly Range NoCongenitalAnomaliesChecked = 560..561;
    public static readonly Range ReportingFlagForMonthPrenatalCareBegan = 225..226;
    public static readonly Range MonthPrenatalCareBeganRecode = 226..227;
    public static readonly Range NumberOfPrenatalVisits = 237..239;
    public static readonly Range NumberOfPrenatalVisitsRecode = 241..243;
    public static readonly Range ReportingFlagForTotalPrenatalCareVisits = 243..244;
    public static readonly Range WIC = 250..251;
    public static readonly Range ReportingFlagForWIC = 251..252;
}

public record DataRow
{
    public int YearOfBirth { get; set; }
    public int MonthOfBirth { get; set; }
    public int BirthPlace { get; set; }
    public int ReportingFlagForBirthPlace { get; set; }
    public int? MothersAgeImputed { get; set; }
    public int? ReportedAgeOfMotherUsedFlag { get; set; }
    public int MothersSingleYearsOfAge { get; set; }
    public int MothersAgeRecode14 { get; set; }
    public int MothersAgeRecode9 { get; set; }
    public int MothersNativity { get; set; }
    public int ResidenceStatus { get; set; }
    public int MothersRaceRecode31 { get; set; }
    public int MothersRaceRecode6 { get; set; }
    public int MothersRaceRecode15 { get; set; }
    public int? MothersRaceImputedFlag { get; set; }
    public int MothersHispanicOrigin { get; set; }
    public int MothersHispanicOriginRecode { get; set; }
    public int ReportingFlagForMothersOrigin { get; set; }
    public int MothersRaceHispanicOrigin { get; set; }
    public char PaternityAcknowledged { get; set; }
    public int MaritalStatus { get; set; }
    public int? MothersMaritalStatusImputed { get; set; }
    public int ReportingFlagForPaternityAcknowledged { get; set; }
    public int MothersEducation { get; set; }
    public int ReportingFlagForEducationOfMother { get; set; }
    public int? FathersReportedAgeUsed { get; set; }
    public int FathersCombinedAge { get; set; }
    public int FathersAgeRecode11 { get; set; }
    public int FathersRaceRecode31 { get; set; }
    public int FathersRaceRecode6 { get; set; }
    public int FathersRaceRecode15 { get; set; }
    public int FathersHispanicOrigin { get; set; }
    public int FathersHispanicOriginRecode { get; set; }
    public int ReportingFlagForFathersHispanicOrigin { get; set; }
    public int FathersRaceHispanicOrigin { get; set; }
    public int FathersEducation { get; set; }
    public int NumberOfPreviousLiveBirths { get; set; }
    public int NumberOfPreviousOtherPregnancyOutcomes { get; set; }
    public int NumberOfPreviousTerminations { get; set; }
    public int LiveBirthOrderRecode { get; set; }
    public int TotalBirthOrderRecode { get; set; }
    public int MonthPrenatalCareBegan { get; set; }
    public int PaymentSourceForDelivery { get; set; }
    public int PaymentRecode { get; set; }
    public int ReportingFlagForSourceOfPayment { get; set; }
    public int ReportingFlagForPaymentRecode { get; set; }
    public int SexOfInfant { get; set; }
    public int ImputedSex { get; set; }
    public int Anencephaly { get; set; }
    public int MeningomyeloceleSpinaBifida { get; set; }
    public int CyanoticCongenitalHeartDisease { get; set; }
    public int CongenitalDiaphragmaticHernia { get; set; }
    public int Omphalocele { get; set; }
    public int Gastroschisis { get; set; }
    public int ReportingFlagForAnencephaly { get; set; }
    public int ReportingFlagForMeningomyeloceleSpinaBifida { get; set; }
    public int ReportingFlagForCyanoticCongenitalHeartDisease { get; set; }
    public int ReportingFlagForCongenitalDiaphragmaticHernia { get; set; }
    public int ReportingFlagForOmphalocele { get; set; }
    public int ReportingFlagForGastroschisis { get; set; }
    public int LimbReductionDefect { get; set; }
    public int CleftLipWithOrWithoutCleftPalate { get; set; }
    public int CleftPalateAlone { get; set; }
    public int DownSyndrome { get; set; }
    public int SuspectedChromosomalDisorder { get; set; }
    public int Hypospadias { get; set; }
    public int ReportingFlagForLimbReductionDefect { get; set; }
    public int ReportingFlagForCleftLipWithOrWithoutCleftPalate { get; set; }
    public int ReportingFlagForCleftPalateAlone { get; set; }
    public int ReportingFlagForDownSyndrome { get; set; }
    public int ReportingFlagForSuspectedChromosomalDisorder { get; set; }
    public int ReportingFlagForHypospadias { get; set; }
    public int NoCongenitalAnomaliesChecked { get; set; }
    public int ReportingFlagForMonthPrenatalCareBegan { get; set; }
    public int MonthPrenatalCareBeganRecode { get; set; }
    public int NumberOfPrenatalVisits { get; set; }
    public int NumberOfPrenatalVisitsRecode { get; set; }
    public int ReportingFlagForTotalPrenatalCareVisits { get; set; }
    public int WIC { get; set; }
    public int ReportingFlagForWIC { get; set; }

    public static DataRow Read(string line)
    {
        var yearOfBirth = ReadNumber<int>(line[ColumnSpecifications.YearOfBirth]);
        var monthOfBirth = ReadNumber<int>(line[ColumnSpecifications.MonthOfBirth]);
        var birthPlace = ReadNumber<int>(line[ColumnSpecifications.BirthPlace]);
        var reportingFlagForBirthPlace = ReadNumber<int>(line[ColumnSpecifications.ReportingFlagForBirthPlace]);
        var mothersAgeImputed = ReadNullableNumber<int>(line[ColumnSpecifications.MothersAgeImputed]);
        var reportedAgeOfMotherUsedFlag = ReadNullableNumber<int>(line[ColumnSpecifications.ReportedAgeOfMotherUsedFlag]);
        var mothersSingleYearsOfAge = ReadNumber<int>(line[ColumnSpecifications.MothersSingleYearsOfAge]);
        var mothersAgeRecode14 = ReadNumber<int>(line[ColumnSpecifications.MothersAgeRecode14]);
        var mothersAgeRecode9 = ReadNumber<int>(line[ColumnSpecifications.MothersAgeRecode9]);
        var mothersNativity = ReadNumber<int>(line[ColumnSpecifications.MothersNativity]);
        var residenceStatus = ReadNumber<int>(line[ColumnSpecifications.ResidenceStatus]);
        var mothersRaceRecode31 = ReadNumber<int>(line[ColumnSpecifications.MothersRaceRecode31]);
        var mothersRaceRecode6 = ReadNumber<int>(line[ColumnSpecifications.MothersRaceRecode6]);
        var mothersRaceRecode15 = ReadNumber<int>(line[ColumnSpecifications.MothersRaceRecode15]);
        var mothersRaceImputedFlag = ReadNullableNumber<int>(line[ColumnSpecifications.MothersRaceImputedFlag]);
        var mothersHispanicOrigin = ReadNumber<int>(line[ColumnSpecifications.MothersHispanicOrigin]);
        var mothersHispanicOriginRecode = ReadNumber<int>(line[ColumnSpecifications.MothersHispanicOriginRecode]);
        var reportingFlagForMothersOrigin = ReadNumber<int>(line[ColumnSpecifications.ReportingFlagForMothersOrigin]);
        var mothersRaceHispanicOrigin = ReadNumber<int>(line[ColumnSpecifications.MothersRaceHispanicOrigin]);
        var paternityAcknowledged = ReadChar(line[ColumnSpecifications.PaternityAcknowledged]);
        var maritalStatus = ReadNumber<int>(line[ColumnSpecifications.MaritalStatus]);
        var mothersMaritalStatusImputed = ReadNullableNumber<int>(line[ColumnSpecifications.MothersMaritalStatusImputed]);
        var reportingFlagForPaternityAcknowledged = ReadNumber<int>(line[ColumnSpecifications.ReportingFlagForPaternityAcknowledged]);
        var mothersEducation = ReadNumber<int>(line[ColumnSpecifications.MothersEducation]);
        var reportingFlagForEducationOfMother = ReadNumber<int>(line[ColumnSpecifications.ReportingFlagForEducationOfMother]);
        var fathersReportedAgeUsed = ReadNullableNumber<int>(line[ColumnSpecifications.FathersReportedAgeUsed]);
        var fathersCombinedAge = ReadNumber<int>(line[ColumnSpecifications.FathersCombinedAge]);
        var fathersAgeRecode11 = ReadNumber<int>(line[ColumnSpecifications.FathersAgeRecode11]);
        var fathersRaceRecode31 = ReadNumber<int>(line[ColumnSpecifications.FathersRaceRecode31]);
        var fathersRaceRecode6 = ReadNumber<int>(line[ColumnSpecifications.FathersRaceRecode6]);

        return new DataRow
        {
            YearOfBirth = yearOfBirth,
            MonthOfBirth = monthOfBirth,
            BirthPlace = birthPlace,
            ReportingFlagForBirthPlace = reportingFlagForBirthPlace,
            MothersAgeImputed = mothersAgeImputed,
            ReportedAgeOfMotherUsedFlag = reportedAgeOfMotherUsedFlag,
            MothersSingleYearsOfAge = mothersSingleYearsOfAge,
            MothersAgeRecode14 = mothersAgeRecode14,
            MothersAgeRecode9 = mothersAgeRecode9,
            MothersNativity = mothersNativity,
            ResidenceStatus = residenceStatus,
            MothersRaceRecode31 = mothersRaceRecode31,
            MothersRaceRecode6 = mothersRaceRecode6,
            MothersRaceRecode15 = mothersRaceRecode15,
            MothersRaceImputedFlag = mothersRaceImputedFlag,
            MothersHispanicOrigin = mothersHispanicOrigin,
            MothersHispanicOriginRecode = mothersHispanicOriginRecode,
            ReportingFlagForMothersOrigin = reportingFlagForMothersOrigin,
            MothersRaceHispanicOrigin = mothersRaceHispanicOrigin,
            PaternityAcknowledged = paternityAcknowledged,
            MaritalStatus = maritalStatus,
            MothersMaritalStatusImputed = mothersMaritalStatusImputed,
            ReportingFlagForPaternityAcknowledged = reportingFlagForPaternityAcknowledged,
            MothersEducation = mothersEducation,
            ReportingFlagForEducationOfMother = reportingFlagForEducationOfMother,
            FathersReportedAgeUsed = fathersReportedAgeUsed,
            FathersCombinedAge = fathersCombinedAge,
            FathersAgeRecode11 = fathersAgeRecode11,
            FathersRaceRecode31 = fathersRaceRecode31,
            FathersRaceRecode6 = fathersRaceRecode6,
        };
    }

    private static T ReadNumber<T>(string value)
        where T : notnull, INumber<T>, IParsable<T>
    {
        ArgumentException.ThrowIfNullOrWhiteSpace(value);
        return T.Parse(value, CultureInfo.InvariantCulture);
    }

    private static T? ReadNullableNumber<T>(string? value)
        where T : INumber<T>, IParsable<T>
    {
        if (string.IsNullOrWhiteSpace(value))
        {
            return default;
        }

        return T.Parse(value, CultureInfo.InvariantCulture);
    }

    private static char ReadChar(string value)
    {
        ArgumentException.ThrowIfNullOrWhiteSpace(value);
        return value[0];
    }

}
