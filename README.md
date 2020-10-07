# A Reproducible Workflow for Economics Research Using Snakemake and Python

[![Build Status](https://travis-ci.org/lachlandeer/snakemake-econ-python.svg?branch=master)](https://travis-ci.org/lachlandeer/snakemake-econ-python)
[![lifecycle](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://www.tidyverse.org/lifecycle/#experimental)
[![lifecycle](https://img.shields.io/badge/version-0.0.1-red.svg)]()

## Introduction

We provide a template for a reproducible research project using `Snakemake` and the `python` programming language.
We use `Snakemake` to construct a set of *rules* that form a DAG that implements the entire research pipeline, starting with some data cleaning, running some regressions, constructung figures and tables, and then finishing with compiling a pdf article and slides.
We believe this mimics an approximate workflow of most empirical research in economics.
The `python` language is used to perform all steps of our analysis.
We use markdown and pandoc to to compile our pdf documents.
`Snakemake` allows us to construct a set of interconnect rules to build our workflow from start to finish - and to partially update the build where required when we update our scripts, data and parameters.

## Motivating Example

Our example project involves replicating the main tables and figures of Mankiw, Romer and Weil's classic 1992 QJE article "[A Contribution to the Empirics of Economic Growth.](https://eml.berkeley.edu/~dromer/papers/MRW_QJE1992.pdf)"
We hope by using an example that is simple in its methods readers focus on how we have chosen to assemble both pure R codes and the Snakemake rules that build our project, rather than getting lost on econometric methodologies.

## Installation Instructions

Follow these Steps to install the necessary software on your system

You need to have the following software and packages installed:

1. Python 3 (Python 3.6 or higher)
2. Snakemake (we'll install the correct version in a couple of lines time!)

### Installing Python

Either:

1. Install Anaconda Python:
    - We provide instructions on how to install anaconda python [here](https://pp4rs.github.io/2020-uzh-installation-guide/python/)
2. Install Python using the deadsnakes ppa:
    - Here's how to add the deadsnakes ppa and install Python 3.8
    ```bash
    $ sudo apt-get install software-properties-common
    $ sudo add-apt-repository ppa:deadsnakes/ppa
    $ sudo apt-get update
    $ sudo apt-get install python3.8
    ```

### Installing Snakemake

We have included a `requirements.txt` file that we can use to install a specific version of snakemake.
This makes sure that our example runs on your machine (or at least won't break because you use a different version of snakemake than we do)

``` bash
pip3 install -r requirements.txt
```

you may need to replace `pip3` with `pip`

**Note:** In recent versions of Snakemake you must state how many cores you want to use when executing rules. 
In this example, we encourage the use of a single core, so when we use snakemake we will always write it as `snakemake --cores 1 <something>`.
More cores speeds things up, but our example is quite light so it seems unnecessary.


### Installing pandoc and LaTeX

TBD

### Install the Required `python` libraries

TBD

## Running the Example

Once the installation instructions are complete, we can run the project.
The result will be 2 pdfs: (1) mrw_replication.pdf - a pdf with some figures and tables of results included; and
(2) mrw_replication slides - a beamer slide deck that also contains some figures and pdfs that were produced by the workflow.

To run the project, enter the following into the terminal:

``` bash
snakemake --cores 1 all
```

This will run through all the R scripts in order to complete the build of the project.

## Visualization of the Workflow

Snakemake workflows are a directed acyclic graph (DAG).
We can visualize the relationship between the rules (a simplified view of the DAG) in our workflow:

![Rulegraph for MRW Workflow](./assets/rulegraph.png)

Check out the rules in `./rules/dag.smk` for various visualizations of the workflow. 
You will need to install `graphviz` to run these rules - we have included a rule inside `dag.smk` to install this for you. 

## Archiving `python` packages in a new project

TBD

## Updates to Workflow Example

We plan to periodically update the workflow as we find better/simpler ways to do things and as our opinions on best practice evolve.
Major changes are tracked in the [NEWS file](./NEWS.md) with brief descriptions of the changes implemented.

## Comments / Suggestions / Issues

We'd love to hear your comments, suggestions or installation issues encountered when running the example.
[Post an issue on Github.](https://github.com/lachlandeer/snakemake-econ-r/issues)

## Suggested Citation

Deer, Lachlan and Julian Langer and Ulrich Bergmann. 2020. A Reproducible Workflow for Economics Research Using Snakemake and Python.