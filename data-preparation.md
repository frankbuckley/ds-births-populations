# Data preparation notes

Race variables include:

#### `MRACE`(1989-2013, though declining from 2003)

```
01 White
02 Black
03 American Indian / Alaskan Native
04 Chinese
05 Japanese
06 Hawaiian(includes part Hawaiian)
07 Filipino
18 Asian Indian
28 Korean
38 Samoan
48 Vietnamese
58 Guamanian
68 Other Asian / Pacific Islander in areas reporting codes 18-58
78 Combined other Asian / Pacific Islander includes 18-68 for areas that do not report them separately
```

#### `MRACEREC`(from 2003-2013)

```
1 White
2 Black
3 American Indian / Alaskan Native
4 Asian / Pacific Islander
```

#### `MBRACE`(2003-2019)

```
1 White
2 Black
3 American Indian or Alaskan Native
4 Asian or Pacific Islander
(Puerto Rico excludes 3 and 4)
```

#### `MRACE15`(from 2014)

```
01 White(only)
02 Black(only)
03 American Indian / Alaskan Native(only)
04 Asian Indian(only)
05 Chinese(only)
06 Filipino(only)
07 Japanese(only)
08 Korean(only)
09 Vietnamese(only)
10 Other Asian(only)
11 Hawaiian(only)
12 Guamanian(only)
13 Samoan(only)
14 Other Pacific Islander(only)
15 More than one race
```

#### `MRACE6`(from 2018) - can be derived from `MRACE15`

```
1 White(only)
2 Black(only)
3 American Indian / Alaskan Native(only)
4 Asian(only)
5 Native Hawaiian or Other Pacific Islander(only)
6 More than one race
```

We combine as follows to get back to 1989:

```
MRACE_C(combined)
1 White
2 Black
3 American Indian or Alaskan Native
4 Asian or Pacific Islander
```

For 2014 on, we have MRACE15, which is summarised in MRACE6 and where more than one race are broken out in MRACE31.

We set `mrace_c` as follows:

- if `mrace15` is available, use `mrace6`, 1:1, 2:2, 3:3, 4-14:4, otherwise,
- if `mracerec` is available, use `mracerec`, 1:1, 2:2, 3:3, 4:4, otherwise,
- if `mbrace` is available, use `mbrace`, 1:1, 2:2, 3:3, 4:4, otherwise,
- if `mrace` is available, use `mrace`, 1:1, 2:2, 3:3, 4-78:4, otherwise,
- missing.


For Hispanic, we have:

MRACEHISP(from 2003)

```
1 Non-Hispanic White(only)
2 Non-Hispanic Black(only)
3 Non-Hispanic AIAN(only)
4 Non-Hispanic Asian(only)
5 Non-Hispanic NHOPI(only)
6 Non-Hispanic more than one race
7 Hispanic
8 Origin unknown or not stated
```

UMHISP(2003-2013) - slightly better counts than MRACEHISP

```
0 Non-Hispanic
1 Mexican
2 Puerto Rican
3 Cuban
4 Central American
5 Other and Unknown Hispanic
9 Origin unknown or not stated
```

ORRACEM(from 1989-2002)

```
1 Mexican
2 Puerto Rican
3 Cuban
4 Central or South American
5 Other and unknown Hispanic
6 Non-Hispanic White
7 Non-Hispanic Black
8 Non-Hispanic other races
9 Origin unknown or not stated
```

MHISP_R(from 2014)

```
0 Non-Hispanic
1 Mexican
2 Puerto Rican
3 Cuban
4 Central and South American
5 Other and Unknown Hispanic origin
9 Hispanic origin not stated
```

MHISPX(from 2018)

```
0 Non-Hispanic
1 Mexican
2 Puerto Rican
3 Cuban
4 Central or South American
5 Dominican
6 Other and Unknown Hispanic
9 Origin unknown or not stated
```

We merge to:

MHISP_C

```
0 Non-Hispanic
1 Mexican
2 Puerto Rican
3 Cuban
4 Other and Unknown Hispanic
5 Origin unknown or not stated
```

Rules:

- if `mhisp_r` is available, then 0:0, 1:1, 2:2, 3:3, 4-5:4, 9:5, otherwise
- if `mhispx` is available, then 0:0, 1:1, 2:2, 3:3, 4-6:4, 9:5, otherwise
- if `umhisp` is available, then 0:0, 1:1, 2:2, 3:3, 4-5:4, 9:5, otherwise
- if `orracem` is available, then 6-8:0, 1:1, 2:2, 3:3, 4-5:4, 9:5, otherwise
- missing
