"""This script processes the raw Revised Local Reference Sea Level data from 
PSMSL into a suitable format for Data Commons
"""
import numpy as np
import pandas as pd
import glob
import calendar

#These paths are based on the unzipped rlr_monthly.zip file obtained from:
# https://psmsl.org/data/obtaining/complete.php
catalogue_file = "rlr_monthly/filelist.txt"
data_dir = "rlr_monthly/data/"


## Start by transforming the Catalogue File with station information

#A list to hold dicts in prep for a DataFrame
catalogue_prep_list = []

#For every line in the catalogue file...
with open(catalogue_file,'r') as opened_file:
    for line in opened_file:
        # Grab the data as such
        catalogue_prep_list.append({
            "id":int(line[0:5].strip()),
            "latitude":float(line[6:17]),
            "longitude":float(line[18:30]),
            "name":str(line[31:72].strip()),
            "coastline":str(line[73:77].strip()),
            "stationcode":str(line[78:82].strip()),
            "flag":bool(line[83:].strip()=='1')
        })

#Convert to data frame
catalogue_df = pd.DataFrame(catalogue_prep_list)

# Next, we process all the mean sea level information
file_list = glob.glob("../rlr_monthly/data/*")

# A list to hold dicts for a data frame
data_prep_list = []

#For every line in every file...
for file in file_list:
    with open(file,'r') as open_data_file:
        for line in open_data_file:
            
            #Process the year and month
            year = int(np.floor(float(line[0:11])))
            month = int((np.round((float(line[0:11])-year)*24)+1)/2)
            
            # Grab the rest of the data as shown below
            data_prep_list.append({
                "id":int(file.split("/")[-1].split(".")[0]),
                "year":year,
                "month":month,
                "height":int(line[12:18]),
                "missing":bool(line[19:21].strip()=='1'),
                "isMtl":bool(line[23]=='1'),
                "dataflag":bool(line[24]=='1')
            })

#Convert to Data Frame
data_df = pd.DataFrame(data_prep_list)

#Merge the station info on the sea level information
merged_df = data_df.merge(catalogue_df, on="id")

#Prep for Data Commons

# Create single Date Column
merged_df['day'] = 1
merged_df['date'] = pd.to_datetime(merged_df[['year','month','day']])

# Unit Column
merged_df['unit'] = 'mm'

#TideGaugeStation DCID
merged_df['dcid:TideGaugeStation'] = np.repeat("psmslId/",len(merged_df))+merged_df['id'].apply(lambda x: str(x))

# Filter out missing flags, data flags, and values less than 0
filtered_df = merged_df[~merged_df['missing'] & ~merged_df['dataflag'] & merged_df['height']>-1]

# Drop unnecessary columns
filtered_df.drop(['year','month','missing','isMtl','dataflag','flag','day'], axis=1, inplace=True)

#Save final output
filtered_df.to_csv("output/PMSML_data_commons.csv",index=False)