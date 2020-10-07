# Rules: data-management
#
# Contributors: @lachlandeer, @julianlanger, @bergmul

# --- Build Rules --- #
## gen_regression_vars: creates the set of variables needed to produce MRW results
rule gen_regression_vars:
    input:
        script = config["src_data_mgt"] + "gen_reg_vars.py",
        data   = config["out_data"] + "mrw_renamed.csv",
        params = config["src_data_mgt"] + "param_solow.json",
    output:
        data = config["out_data"] + "mrw_complete.csv",
    log:
        config["log"] + "data-management/gen_reg_vars.txt"
    shell:
        "python {input.script} --data {input.data} --param {input.params} \
            --out {output.data}"

## rename_vars     : gives meaningful names to variables 
rule rename_vars:
    input:
        script = config["src_data_mgt"] + "rename_variables.py",
        data   = config["src_data"] + "mrw.dta",
    output:
        data = config["out_data"] + "mrw_renamed.csv",
    log:
        config["log"] + "data-management/rename_variables.txt"
    shell:
        "python {input.script} --data {input.data} --out {output.data}"