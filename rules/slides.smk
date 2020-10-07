# Rules: slides
#
#
# contributors: @lachlandeer, @julianlanger, @bergmul

# --- Build Rules --- #
## slides2root:    move slides to root directory
rule slides2root:
    input:
        pdf  = config["out_slides"] + PROJ_NAME + "_slides.pdf"
    output:
        pdf  = PROJ_NAME + "_slides.pdf",
    shell:
        "cp {input.pdf} {output.pdf}"

rule build_slides:
    input:
        style_tex  = config["src_slides"] + "style.tex",
        template   = config["src_slides"] + "template.beamer" ,
        #biblio = "refs.bib",
        #bibclass = "chicago.csl",
        figures = expand(config["out_figures"] +
                            "{iPlot}.pdf",
                            iPlot = PLOTS),
        metadata = config["src_slides"] + "slide_config.yaml",
        content = config["src_slides"] + "content.md"
    output:
        pdf = config["out_slides"] + PROJ_NAME + "_slides.pdf"
    shell:
        "pandoc -t beamer \
            {input.metadata} \
            {input.content} \
            --filter pandoc-citeproc \
            --slide-level 2 \
            --pdf-engine=pdflatex \
            --template={input.template} \
            -o {output.pdf}"

rule pdf_clean:
    shell:
        "rm out/*.pdf"