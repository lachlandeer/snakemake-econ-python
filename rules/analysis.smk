# Rules: analysis
#
# Contributors: @lachlandeer, @julianlanger, @bergmul

# --- Build Rules --- #
## estimate_models  : Helper rule that runs all regression models by expanding wildcards
rule estimate_models:
    input:
        expand(config["out_analysis"] +
                            "{iModel}_ols_{iSubset}.pickle",
                            iModel = MODELS,
                            iSubset = DATA_SUBSET)

## ols_model        : Estimate an OLS regression model on MRW data      
rule ols_model:
    input:
        script = config["src_analysis"] + "estimate_ols.py",
        data   = config["out_data"] + "mrw_complete.csv",
        model  = config["src_model_specs"] + "{iModel}.json",
        subset = config["src_data_specs"] + "{iSubset}.json"
    output:
        model_est = config["out_analysis"] + "{iModel}_ols_{iSubset}.pickle",
    log:
        #config["log"] + "analysis/estimate_ols.txt"
    shell:
        "python {input.script} --data {input.data} --model {input.model} \
            --subset {input.subset} --out {output.model_est}"