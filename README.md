# Integrating single cell gene expression datasets
Slides, notebook, and datasets for integrating single cell gene expression datasets

## Before class
- On the biostat server (or on your own computer), clone this repository:
```
$ git clone https://github.com/Roy-lab/compnetbio-singlecell-integration.git
```
- Or, if that doesn't work for some reason, simply download the whole repository zip file, and if you want to run code off the biostat server, `scp` the compressed file onto the server, and unzip.

## At the start of class (if you want to run code on the server)
1. Login to the biostat server.
2. __ON THE SERVER__, go to the directory with the notebook and the dataset directories. If you git-cloned with the above command in your home directory and didn't rename any directories, it should just be:
```
$ cd compnetbio-singlecell-integration
```
3. __ON THE SERVER__, start up Jupyter notebook using the specific environment where all dependencies were pre-installed for you. Replace `${port}` with some four-digit number.
```
$ /u/medinfo/bmi776-miniconda3/envs/compnetbio-f19/bin/jupyter notebook --no-browser --port=${port}
```
You should see an output that looks like:
```
[I 14:14:31.377 NotebookApp] Serving notebooks from local directory: /ua/dlee324/compnetbio-singlecell-integration
[I 14:14:31.377 NotebookApp] The Jupyter Notebook is running at:
[I 14:14:31.377 NotebookApp] http://localhost:8512/?token=addfbbb64d3ee87f84d6805f8ba60011d6f31c4147742289
[I 14:14:31.378 NotebookApp]  or http://127.0.0.1:8512/?token=addfbbb64d3ee87f84d6805f8ba60011d6f31c4147742289
[I 14:14:31.378 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 14:14:31.411 NotebookApp] 
    
    To access the notebook, open this file in a browser:
        file:///ua/dlee324/.local/share/jupyter/runtime/nbserver-2279418-open.html
    Or copy and paste one of these URLs:
        http://localhost:8512/?token=addfbbb64d3ee87f84d6805f8ba60011d6f31c4147742289
     or http://127.0.0.1:8512/?token=addfbbb64d3ee87f84d6805f8ba60011d6f31c4147742289
```
4. __BACK ON YOUR COMPUTER__, open command line/terminal, and to claim the port, run the following command and enter password if prompted. 
 - Replace `${port}` with one that was created based on your command in step 3 (in my case it was 8512); 
 - replace `${user}` with your biostat login; 
 - finally replace `${server.ip}` with the biostat server address you logged into, e.g. mi1.biostat.wisc.edu.
```
$ ssh -N -f -L localhost:${port}:localhost:${port} ${user}@${server.ip}
```
5. __ON YOUR COMPUTER__, copy and paste in the localhost:port URL into a browser. In my case it would be `http://localhost:8512/?token=addfbbb64d3ee87f84d6805f8ba60011d6f31c4147742289`.

## If you want to run code on your own computer
1. Install Anaconda or Miniconda on your own computer.
2. Assuming you cloned or downloaded the repo already, create a new environment using the `environment.yml` file included in this repo. 
```
$ conda env create -f environment.yml
```
3. Activate the environment and launch Jupyter and open the notebook included in this repo.
```
$ conda activate compnetbio-f19 #might be source activate compnetbio-f19 if you have an older conda
$ jupyter notebook
```
