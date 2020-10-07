"""
Estimate Regression Model on Subset of Data
"""

import sys
import argparse
import logging
from pathlib import Path
import json
import pandas as pd
import statsmodels.formula.api as smf

def read_mrw(file_name):
    """ Imports a Stata data set containing MRW data """
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

def create_reg_formula(formula_dict):
    "Transform dictionary with regression pieces into single formula"
    
    reg_str = formula_dict["DEPVAR"] + '~' + formula_dict["EXOG"] 
    return reg_str

def run_regression(formula_dict, df):

    reg_eq = create_reg_formula(formula_dict)
    mod = smf.ols(formula = reg_eq, data = df)
    res = mod.fit()

    return res

if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", 
                        "--data",
                        help = "input data file name"
                        )
    parser.add_argument("-m", 
                        "--model",
                        help = "a file name containing a regression model"
                        )
    parser.add_argument("-s", 
                        "--subset",
                        help = "a file name containing a regression model"
                        )
    parser.add_argument("-o", 
                        "--out",
                        help = "output file name"
                        )

    args = parser.parse_args()
    
    # Logging info
    fname = Path(__file__).resolve().stem
    dname = Path(__file__).parent.name
    subset_name = Path(args.subset).resolve().stem
    model_name  = Path(args.model).resolve().stem
    logfile = Path.cwd() / 'logs' / dname / (model_name + '_' + fname + '_' + subset_name + '.txt')
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
    model   = read_dict(args.model)

    logging.info('Subset Data')
    mrw_subset = reg_sample(mrw, filters)

    logging.info('Run regression')
    res = run_regression(model, mrw_subset)

    print(res.summary())

    # Save regression
    logging.info('Saving data')
    res.save(args.out)