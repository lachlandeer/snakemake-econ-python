# Rules: paper
#
# article-style: asa
#
# contributors: @lachlandeer, @julianlanger, @bergmul

# --- Dictionaries --- #
MD_FILES   = [
                config["src_paper"] + "index.md",
                config["src_paper"] + "01-intro.md",
                config["src_paper"] + "02-literature.md",
                config["src_paper"] + "03-data.md",
                config["src_paper"] + "04-results.md",
                config["src_paper"] + "05-references.md",
                ]
BIB_FILES  = glob.glob(config["src_paper"] + "*.bib")
TEX_FILES  = glob.glob(config["src_paper"] + "*.tex")

# --- Build Rules --- #
## paper2root:   copy paper to root directory
rule paper2root:
    input:
        pdf  = config["out_paper"] + "my_article.pdf",
    output:
        pdf  = PROJ_NAME + ".pdf",
    shell:
        "cp {input.pdf} {output.pdf}"

## build_pdf: builds pdf using pandoc
rule build_pdf:
    input:
        md_files   = MD_FILES,
        biblo      = BIB_FILES,
        tex_style  = TEX_FILES,
        bib_format = config["src_paper"] + "chicago-fullnote-bibliography.csl",
        # tables     = expand(config["out_tables"] +
        #                     "{iTable}.tex",
        #                     iTable = TABLES),
        figures = expand(config["out_figures"] +
                            "{iPlot}.pdf",
                            iPlot = PLOTS),
    output:
        config["out_paper"] + "my_article.pdf"
    log:
        config["log"] + "paper/build_pdf.out"
    shell:
        "pandoc -s  \
            {input.md_files} \
            --template=src/paper/asa_template.tex \
            --filter pandoc-citeproc \
            --csl {input.bib_format} \
            --bibliography {input.biblo} \
            --pdf-engine=pdflatex -o {output}"
