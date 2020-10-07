"""
Adds meaningful variable names to the original MRW data set
"""

import argparse
import pandas as pd

def read_mrw(file_name):
    """ Imports a Stata data set containing MRW data """
    df = pd.read_stata(file_name)
    return df

def rename_cols(df):
    """ Construct meaningful variable names  """
    df.rename(columns={
                    "n"        : "nonoil", 
                    "o"        : "oecd",
                    "i"        : "intermediate",
                    "rgdpw60"  : "gdp_60",
                    "rgdpw85"  : "gdp_85",
                    "gdpgrowth": "gdp_growth_60_85",
                    "popgrowth": "pop_growth_60_85",
                    "i_y"      : "inv_gdp" 
                    },
          inplace= True
         )
    return df

if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", 
                        "--data",
                        help = "stata dataset file name"
                        )
    
    parser.add_argument("-o", 
                        "--out",
                        help = "output file name"
                        )

    args = parser.parse_args()
    
    # Do data cleaning
    mrw = read_mrw(args.data)
    mrw_clean = rename_cols(mrw)

    # Save to csv
    mrw.to_csv(args.out, index = False)
