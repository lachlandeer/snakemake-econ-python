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

def partial_residuals_cc(df):
    yp_reg_eq = "ln_gdp_growth ~  ln_inv_gdp + ln_ndg"
    xp_reg_eq = "ln_gdp_60 ~  ln_inv_gdp + ln_ndg"
    
    yp_mod = smf.ols(formula = yp_reg_eq, data = df)
    yp_res = yp_mod.fit()
    yp = yp_res.resid

    xp_mod = smf.ols(formula = xp_reg_eq, data = df)
    xp_res = xp_mod.fit()
    xp = xp_res.resid

    frame = {
        'y_partial' : yp,
        'x_partial' : xp
    }

    partial_df = pd.DataFrame(frame)
    return partial_df

def plot_cond_conv(partial_df, outfile):
    
    df = partial_df
    fig, ax = plt.subplots()

    ax.scatter(x = df['x_partial'], y = df['y_partial'], color='black')
    ax.plot(np.unique(df['x_partial']),
            np.poly1d(np.polyfit(df['x_partial'], 
                                 df['y_partial'], 
                                 1)
                        )
            (np.unique(df['x_partial'])),
            color='r')
    ax.set_title("B: Conditional on Saving and Population Growth")
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

    logging.info('Run partial regressions - return partialled out y and x')
    partials = partial_residuals_cc(mrw_subset)

    logging.info('Create Figure')
    plot_cond_conv(partials, args.out)
