# Importing PSMSL Revised Local Reference (RLR) Sea Level Data Into Data Commons

Author: Brian Chivers

## Table of Contents

1. [About the Dataset](#about-the-dataset)
1. [About the Import](#about-the-import)

## About the Dataset


### Download URL
RLR Monthly Mean data is available at teh following URL: 
[Download Page](https://psmsl.org/data/obtaining/complete.php)

### Overview

This dataset contains a Sea Level height for a number of Tide Gauge stations across the world, and a number of dates.  [This note page](https://psmsl.org/data/obtaining/notes.php) contains information about the files themselves.  [This page](https://psmsl.org/data/obtaining/rlr.php) also describes how the RLR is created and why it's technically different than actual Sea Level height.  

Please reference the [PSMSL site](https://psmsl.org/) for any additonal information on this data.



## About the Import

### Artifacts

#### Raw Data
- [rlr_monthly.zip](rlr_monthly.zip)
- [rlr_monthly/](rlr_monthly/)

#### Cleaned Data
- [PSMSL_data_commons.csv](output/PSMSL_data_commons.csv)

#### Template MCFs
- [PSMSL_data_commons.tmcf](output/PSMSL_data_commons.tmcf)

#### Scripts
- [process_psmsl_data.py](process_psmsl_data.py)


#### Generating Artifacts:

`PSMSL_data_commons.tmcf` was generated using the [import wizard](https://datacommons.org/import/)

To generate `PSMSL_data_commons.csv`, run:

```bash
python3 preproccess.py
```
