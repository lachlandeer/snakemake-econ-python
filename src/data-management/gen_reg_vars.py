"""
Creates variables necessary for regression
"""

import argparse
import logging
from pathlib import Path
import json
import pandas as pd
import numpy as np

def read_mrw(file_name):
    """ Imports a Stata data set containing MRW data """
    df = pd.read_csv(file_name)
    return df

def create_vars(df, delta_gamma = 0.05):
    """ Creates regression variables  """
    df1 = df.assign(
                ln_gdp_85     = lambda x: np.log(x.gdp_85),
                ln_gdp_60     = lambda x: np.log(x.gdp_60),
                ln_gdp_growth = lambda x: x.ln_gdp_85 - x.ln_gdp_60,
                ln_inv_gdp    = lambda x: np.log(x.inv_gdp/100),
                ln_ndg        = lambda x: np.log(x.pop_growth_60_85/100 + delta_gamma),
                ln_school     = lambda x: np.log(x.school/100)
                
                )
    return df

if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", 
                        "--data",
                        help = "input data file name"
                        )
    parser.add_argument("-p", 
                        "--params",
                        help = "json file that has parametrization"
                        )
    
    parser.add_argument("-o", 
                        "--out",
                        help = "output data file name"
                        )

    args = parser.parse_args()
    
    # Logging info
    fname = Path(__file__).resolve().stem
    dname = Path(__file__).parent.name
    print(dname)
    logfile = Path.cwd() / 'logs' / dname / (fname + '.txt')
    ## Create a custom logger
    logger = logging.getLogger(__name__)
    ## Configure Logging
    logging.basicConfig(filename = logfile,
                        format = '%(asctime)s - %(message)s', 
                        level  = logging.INFO)
    
    # Do it!
    logging.info('Reading parametrization from JSON')
    with open(args.params) as json_file: 
        params = json.load(json_file)

    logging.info('Reading data')
    mrw = read_mrw(args.data)
    logging.info('Creating Variables')
    mrw_clean = create_vars(mrw, params['DELTA_GAMMA'])

    # Save to csv
    logging.info('Saving data')
    mrw.to_csv(args.out, index = False)