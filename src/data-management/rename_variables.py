"""
Adds meaningful variable names to the original MRW data set
"""

import argparse
import logging
from pathlib import Path
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
    
    # Logging info
    print(Path(__file__).resolve().stem)
    logfile = Path.cwd() / 'logs' / Path(__file__).resolve().stem
    ## Create a custom logger
    logger = logging.getLogger(__name__)
    ## Configure Logging
    logging.basicConfig(filename = logfile,
                        format = '%(asctime)s - %(message)s', 
                        level  = logging.INFO)
    
    # Do data cleaning
    logging.info('Reading Stata data')
    mrw = read_mrw(args.data)
    logging.info('Rename columns')
    mrw_clean = rename_cols(mrw)

    # Save to csv
    logging.info('Saving data')
    mrw.to_csv(args.out, index = False)
