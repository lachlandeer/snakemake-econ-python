import json
import statsmodels.api as sm
from distutils.util import strtobool
from stargazer.stargazer import Stargazer, LineLocation

def publish_table(tbl, format_json):

    tbl.dep_var_name = format_json["DEP_VAR"]
    tbl.custom_columns(format_json["MODEL_NAMES"], format_json["NAME_LENGTHS"])
    tbl.covariate_order(format_json["VAR_ORDER"])
    tbl.rename_covariates(format_json["VAR_NAMES"])    
    tbl = table_formatter(tbl)

    if bool(strtobool(format_json["RESTR_LOGICAL"])) == True: 
        tbl.add_line('Restricted Model', format_json["RESTRICTIONS"], LineLocation.FOOTER_TOP)

    return tbl

def table_formatter(tbl):
    tbl.significant_digits(2)
    tbl.show_degrees_of_freedom(False)
    tbl.show_residual_std_err = False
    tbl.show_adj_r2 = False
    tbl.show_f_statistic = False
    tbl.show_notes = True

    return tbl


###

fname = "src/tablespecs/table_01.json"

with open(fname) as json_file: 
    json_dict = json.load(json_file)

models = json_dict['MODELS']

models = [json_dict["MODEL_PATH"] + i for i in models]

reg = []

for iModel in models:
    reg.append(sm.load(iModel))
    

stargazer = Stargazer(reg)

stargazer2 = publish_table(stargazer, json_dict) 

print('---')
print(json_dict["RESTRICTIONS"])
print('---')

print(stargazer2.render_latex(only_tabular=True))