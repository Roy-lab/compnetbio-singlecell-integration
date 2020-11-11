[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE) [![Generic badge](https://img.shields.io/badge/python-3.7-blue.svg)](https://shields.io/)

# Integrating single cell gene expression datasets
This repository contains slides, notebook, and datasets for integrating single cell gene expression datasets. The content was created for BMI 826-023 Special Topics in Computational Network Biology (https://compnetbiocourse.discovery.wisc.edu/).

## Set up

The demo code is in Python, and run through a Jupyter notebook in a conda environment. If you don't know what those are, that's fine - we'll step through it in class. If you do have experience with them, and want to run the code and/or follow along during lecture, please follow the steps below.
1. Download or clone this repository: `git clone https://github.com/Roy-lab/compnetbio-singlecell-integration.git`
2. If you don't have Anaconda installed, go ahead and do so: https://docs.anaconda.com/anaconda/install/ (if you have miniconda or another conda installation, all code should still work; note that the code was tested in Anaconda only).
3. Create a new conda environment using the `environment.yml` file included in this repo: 
```
conda env create -f environment.yml
```
4. Go to the downloaded directory (e.g. if downloaded to desktop, something like `cd Desktop/compnetbio-singlecell-integration`)
4. Activate the environment and launch Jupyter notebook:
```
conda activate compnetbio
jupyter notebook
```
5. Open the notebook `20191105_CompNetBio_Notebook.ipynb`.
