"""
Plot Evidence of conditional convergence
"""

import sys
import argparse
import logging
from pathlib import Path
import json
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

def read_mrw(file_name):
    """ Imports a csv file containing MRW data """
    df = pd.read_csv(file_name)
    return df

def read_dict(fname):
    with open(fname) as json_file: 
        json_dict = json.load(json_file)
    return json_dict

def reg_sample(df, filter_dict):
    filter_condition = filter_dict["KEEP_CONDITION"]
    df = df.query(filter_condition)
    return df

def plot_uncond_conv(df, outfile):
    
    fig, ax = plt.subplots()

    ax.scatter(x = df['ln_gdp_60'], y = df['ln_gdp_growth'], color='black')
    ax.plot(np.unique(df['ln_gdp_60']),
            np.poly1d(np.polyfit(df['ln_gdp_60'], 
                                 df['ln_gdp_growth'], 
                                 1)
                        )
            (np.unique(df['ln_gdp_60'])),
            color='r')
    ax.set_title("A: Unconditional")
    ax.set_ylabel("Log Growth rate: 1960 - 85")
    ax.set_xlabel("Log output per working age adult: 1960")

    print("Saving Figure...")
    plt.savefig(outfile, bb_inches = "tight", dip = 1200)
    print("Saved!")

if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", 
                        "--data",
                        help = "input data file name"
                        )
    parser.add_argument("-s", 
                        "--subset",
                        help = "a file name containing a subset condition"
                        )
    parser.add_argument("-o", 
                        "--out",
                        help = "output file name"
                        )

    args = parser.parse_args()
    
    # Logging info
    fname = Path(__file__).resolve().stem
    dname = Path(__file__).parent.name
    logfile = Path.cwd() / 'logs' / dname / (fname + '.txt')
    ## Create a custom logger
    logger = logging.getLogger(__name__)
    ## Configure Logging
    logging.basicConfig(filename = logfile,
                        format = '%(asctime)s - %(message)s', 
                        level  = logging.INFO)
    logger = logging.getLogger()
    sys.stderr.write = logger.error
    sys.stdout.write = logger.info
    
    # Do it!
    logging.info('Reading data')
    mrw = read_mrw(args.data)

    logging.info('Loading JSON Dictionaries')
    filters = read_dict(args.subset)

    logging.info('Subset Data')
    mrw_subset = reg_sample(mrw, filters)

    logging.info('Create Figure')
    plot_uncond_conv(mrw_subset, args.out)
